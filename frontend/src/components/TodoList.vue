<script setup>
import { onMounted, ref } from "vue";
import { fetchTodos } from "../api/todos.js";
import TodoForm from "./TodoForm.vue";
import TodoItem from "./TodoItem.vue";

const todos = ref([]);
const isLoading = ref(false);
const errorMessage = ref("");

async function loadTodos() {
  isLoading.value = true;
  errorMessage.value = "";
  try {
    todos.value = await fetchTodos();
  } catch {
    errorMessage.value =
      "할 일 목록을 불러오지 못했습니다. 잠시 후 다시 시도해 주세요.";
  } finally {
    isLoading.value = false;
  }
}

function onCreated(todo) {
  todos.value.push(todo);
}

function onUpdated(updated) {
  const index = todos.value.findIndex((todo) => todo.id === updated.id);
  if (index !== -1) {
    todos.value[index] = updated;
  }
}

function onDeleted(id) {
  todos.value = todos.value.filter((todo) => todo.id !== id);
}

onMounted(loadTodos);
</script>

<template>
  <section class="todo-list">
    <div class="card">
      <div class="card-header">
        <h2 class="card-title">할 일 목록</h2>
        <span v-if="!isLoading && !errorMessage" class="todo-count">{{
          todos.length
        }}</span>
      </div>

      <TodoForm @created="onCreated" />

      <p v-if="isLoading" class="todo-status-message">
        <i class="bi bi-arrow-repeat"></i> 불러오는 중...
      </p>
      <div v-else-if="errorMessage" class="alert-custom alert-custom-danger">
        <i class="bi bi-exclamation-triangle"></i>
        <div class="alert-custom-content">{{ errorMessage }}</div>
        <button
          type="button"
          class="btn-custom btn-custom-sm btn-custom-outline-secondary retry-btn"
          @click="loadTodos"
        >
          다시 시도
        </button>
      </div>
      <div v-else-if="todos.length === 0" class="alert-custom alert-custom-info">
        <i class="bi bi-inbox"></i>
        <div class="alert-custom-content">등록된 할 일이 없습니다.</div>
      </div>
      <ul v-else class="transaction-list list-unstyled m-0">
        <TodoItem
          v-for="todo in todos"
          :key="todo.id"
          :todo="todo"
          @updated="onUpdated"
          @deleted="onDeleted"
        />
      </ul>
    </div>
  </section>
</template>

<style scoped>
.todo-count {
  background-color: var(--brand-lime-translucent);
  color: var(--brand-forest-medium);
  font-size: 0.8rem;
  font-weight: 700;
  border-radius: 50rem;
  padding: 0.15rem 0.65rem;
}
.todo-status-message {
  color: var(--text-muted-green);
  margin: 0;
}
.todo-status-message .bi {
  display: inline-block;
  animation: todo-spin 1s linear infinite;
}
@keyframes todo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
.retry-btn {
  margin-left: auto;
  flex-shrink: 0;
}
</style>
