<script setup>
import { ref } from "vue";
import { deleteTodo, toggleTodo, updateTodo } from "../api/todos.js";

const props = defineProps({ todo: { type: Object, required: true } });
const emit = defineEmits(["updated", "deleted"]);

const isEditing = ref(false);
const editTitle = ref("");
const editDescription = ref("");
const isBusy = ref(false);
const errorMessage = ref("");

function startEdit() {
  isEditing.value = true;
  editTitle.value = props.todo.title;
  editDescription.value = props.todo.description;
}

function cancelEdit() {
  isEditing.value = false;
  errorMessage.value = "";
}

async function toggleCompleted() {
  isBusy.value = true;
  errorMessage.value = "";
  try {
    const updated = await toggleTodo(props.todo.id, !props.todo.completed);
    emit("updated", updated);
  } catch {
    errorMessage.value =
      "상태를 변경하지 못했습니다. 잠시 후 다시 시도해 주세요.";
  } finally {
    isBusy.value = false;
  }
}

async function remove() {
  isBusy.value = true;
  errorMessage.value = "";
  try {
    await deleteTodo(props.todo.id);
    emit("deleted", props.todo.id);
  } catch {
    errorMessage.value = "삭제하지 못했습니다. 잠시 후 다시 시도해 주세요.";
  } finally {
    isBusy.value = false;
  }
}

async function saveEdit() {
  if (!editTitle.value.trim()) {
    errorMessage.value = "제목을 입력해 주세요.";
    return;
  }
  isBusy.value = true;
  errorMessage.value = "";
  try {
    const updated = await updateTodo(props.todo.id, {
      title: editTitle.value,
      description: editDescription.value,
    });
    emit("updated", updated);
    isEditing.value = false;
  } catch (error) {
    const fieldMessage = error.fieldErrors?.title?.[0];
    errorMessage.value =
      fieldMessage ?? "변경을 저장하지 못했습니다. 잠시 후 다시 시도해 주세요.";
  } finally {
    isBusy.value = false;
  }
}
</script>

<template>
  <li class="todo-item">
    <template v-if="isEditing">
      <input v-model="editTitle" type="text" />
      <input v-model="editDescription" type="text" placeholder="설명 (선택)" />
      <span class="actions">
        <button type="button" :disabled="isBusy" @click="saveEdit">저장</button>
        <button type="button" :disabled="isBusy" @click="cancelEdit">취소</button>
      </span>
    </template>
    <template v-else>
      <span class="todo-title" :class="{ done: todo.completed }">{{ todo.title }}</span>
      <span v-if="todo.description" class="todo-description">{{ todo.description }}</span>
      <span class="todo-completed" :class="{ done: todo.completed }">
        {{ todo.completed ? "완료" : "미완료" }}
      </span>
      <span class="actions">
        <button type="button" :disabled="isBusy" @click="toggleCompleted">
          {{ todo.completed ? "미완료로 변경" : "완료로 변경" }}
        </button>
        <button type="button" :disabled="isBusy" @click="startEdit">수정</button>
        <button type="button" :disabled="isBusy" @click="remove">삭제</button>
      </span>
    </template>
    <p v-if="errorMessage" class="item-error">{{ errorMessage }}</p>
  </li>
</template>

<style scoped>
.todo-item {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem;
  padding: 0.6rem 0.8rem;
  border-bottom: 1px solid #dfe3e8;
}
.todo-item input {
  flex: 1 1 160px;
  min-width: 0;
}
.todo-title {
  font-weight: 600;
}
.todo-title.done {
  text-decoration: line-through;
  color: #888;
}
.todo-completed {
  flex-shrink: 0;
  color: #888;
}
.todo-completed.done {
  color: #1d7d5f;
  font-weight: 700;
}
.todo-description {
  flex: 1;
  min-width: 0;
  overflow-wrap: anywhere;
  color: #666;
}
.actions {
  margin-left: auto;
  display: flex;
  gap: 0.4rem;
}
.item-error {
  flex-basis: 100%;
  color: #c0392b;
  margin: 0;
}
@media (max-width: 480px) {
  .actions {
    width: 100%;
    justify-content: flex-end;
  }
}
</style>
