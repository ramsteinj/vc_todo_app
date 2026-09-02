from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo


class TodoModelTest(TestCase):
    def test_str_returns_title(self):
        todo = Todo.objects.create(title="테스트 제목")
        self.assertEqual(str(todo), "테스트 제목")

    def test_defaults(self):
        todo = Todo.objects.create(title="테스트")
        self.assertEqual(todo.description, "")
        self.assertFalse(todo.completed)
        self.assertIsNotNone(todo.created_at)
        self.assertIsNotNone(todo.updated_at)

    def test_updated_at_changes_on_save(self):
        todo = Todo.objects.create(title="테스트")
        before = todo.updated_at
        todo.title = "변경된 제목"
        todo.save()
        todo.refresh_from_db()
        self.assertGreater(todo.updated_at, before)


class TodoApiTest(APITestCase):
    def create_todo(self, **overrides):
        data = {"title": "새 할 일"}
        data.update(overrides)
        return Todo.objects.create(**data)

    def test_list_empty(self):
        response = self.client.get(reverse("todo-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [])

    def test_list_returns_created_items(self):
        self.create_todo()
        self.create_todo(title="두 번째", description="설명")
        response = self.client.get(reverse("todo-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_create_returns_all_fields(self):
        response = self.client.post(
            reverse("todo-list"), {"title": "새 할 일"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.json()
        self.assertEqual(data["title"], "새 할 일")
        self.assertEqual(data["description"], "")
        self.assertFalse(data["completed"])
        self.assertIn("id", data)
        self.assertIn("created_at", data)
        self.assertIn("updated_at", data)

    def test_create_with_description(self):
        response = self.client.post(
            reverse("todo-list"),
            {"title": "새 할 일", "description": "상세 설명"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["description"], "상세 설명")

    def test_retrieve(self):
        todo = self.create_todo(title="조회 대상")
        response = self.client.get(reverse("todo-detail", args=[todo.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["title"], "조회 대상")

    def test_put_updates_all_editable_fields(self):
        todo = self.create_todo()
        original_created_at = todo.created_at
        payload = {
            "title": "수정된 제목",
            "description": "수정된 설명",
            "completed": True,
        }
        response = self.client.put(
            reverse("todo-detail", args=[todo.id]), payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data["title"], "수정된 제목")
        self.assertEqual(data["description"], "수정된 설명")
        self.assertTrue(data["completed"])
        todo.refresh_from_db()
        self.assertEqual(todo.created_at, original_created_at)

    def test_patch_partial_update(self):
        todo = self.create_todo(title="원래 제목", description="원래 설명")
        response = self.client.patch(
            reverse("todo-detail", args=[todo.id]),
            {"completed": True},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data["completed"])
        self.assertEqual(data["title"], "원래 제목")
        self.assertEqual(data["description"], "원래 설명")

    def test_delete(self):
        todo = self.create_todo()
        response = self.client.delete(reverse("todo-detail", args=[todo.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Todo.objects.filter(id=todo.id).exists())


class TodoApiValidationTest(APITestCase):
    def test_post_empty_title_rejected(self):
        response = self.client.post(
            reverse("todo-list"), {"title": ""}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.json())

    def test_post_whitespace_title_rejected(self):
        response = self.client.post(
            reverse("todo-list"), {"title": "   "}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.json())

    def test_post_missing_title_rejected(self):
        response = self.client.post(
            reverse("todo-list"), {"description": "제목 없음"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.json())

    def test_put_missing_title_rejected(self):
        todo = Todo.objects.create(title="기존 할 일")
        response = self.client.put(
            reverse("todo-detail", args=[todo.id]),
            {"description": "제목 없음"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.json())

    def test_nonexistent_detail_returns_404(self):
        cases = [
            ("get", None),
            ("put", {}),
            ("patch", {}),
            ("delete", None),
        ]
        for method, data in cases:
            response = getattr(self.client, method)(
                reverse("todo-detail", args=[9999]), data, format="json"
            )
            self.assertEqual(
                response.status_code, status.HTTP_404_NOT_FOUND, msg=method
            )
