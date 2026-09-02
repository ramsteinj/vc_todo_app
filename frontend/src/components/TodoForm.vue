<script setup>
import { ref } from "vue";
import { createTodo } from "../api/todos.js";

const emit = defineEmits(["created"]);

const title = ref("");
const description = ref("");
const isSubmitting = ref(false);
const errorMessage = ref("");

async function submit() {
  if (!title.value.trim()) {
    errorMessage.value = "제목을 입력해 주세요.";
    return;
  }
  isSubmitting.value = true;
  errorMessage.value = "";
  try {
    const todo = await createTodo({
      title: title.value,
      description: description.value,
    });
    title.value = "";
    description.value = "";
    emit("created", todo);
  } catch (error) {
    const fieldMessage = error.fieldErrors?.title?.[0];
    errorMessage.value =
      fieldMessage ?? "할 일을 저장하지 못했습니다. 잠시 후 다시 시도해 주세요.";
  } finally {
    isSubmitting.value = false;
  }
}
</script>

<template>
  <form class="todo-form" @submit.prevent="submit">
    <input v-model="title" type="text" placeholder="할 일 제목" />
    <input v-model="description" type="text" placeholder="설명 (선택)" />
    <button type="submit" :disabled="isSubmitting">
      {{ isSubmitting ? "저장 중..." : "추가" }}
    </button>
    <p v-if="errorMessage" class="form-error">{{ errorMessage }}</p>
  </form>
</template>

<style scoped>
.todo-form {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}
.todo-form input {
  flex: 1 1 160px;
  min-width: 0;
}
.todo-form button {
  flex-shrink: 0;
}
.form-error {
  flex-basis: 100%;
  color: #c0392b;
  margin: 0;
}
@media (max-width: 480px) {
  .todo-form input,
  .todo-form button {
    flex-basis: 100%;
  }
}
</style>
