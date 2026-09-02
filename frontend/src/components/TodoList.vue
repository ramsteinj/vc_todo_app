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
    <TodoForm @created="onCreated" />
    <p v-if="isLoading" class="status">불러오는 중...</p>
    <p v-else-if="errorMessage" class="status error">
      {{ errorMessage }}
      <button type="button" @click="loadTodos">다시 시도</button>
    </p>
    <p v-else-if="todos.length === 0" class="status">등록된 할 일이 없습니다.</p>
    <ul v-else>
      <TodoItem
        v-for="todo in todos"
        :key="todo.id"
        :todo="todo"
        @updated="onUpdated"
        @deleted="onDeleted"
      />
    </ul>
  </section>
</template>

<style scoped>
.todo-list ul {
  list-style: none;
  margin: 0;
  padding: 0;
  background: #fff;
  border: 1px solid #dfe3e8;
  border-radius: 8px;
  overflow: hidden;
}
.status {
  background: #fff;
  border: 1px dashed #c9ced6;
  border-radius: 8px;
  padding: 1rem;
  color: #666;
}
.status.error {
  color: #c0392b;
  border-color: #e6b0aa;
}
</style>
