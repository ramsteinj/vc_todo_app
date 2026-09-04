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
  <li class="transaction-item todo-item">
    <template v-if="isEditing">
      <input
        v-model="editTitle"
        type="text"
        class="form-control-custom"
        placeholder="할 일 제목"
      />
      <input
        v-model="editDescription"
        type="text"
        class="form-control-custom"
        placeholder="설명 (선택)"
      />
      <div class="actions">
        <button
          type="button"
          class="btn-custom btn-custom-sm btn-custom-primary"
          :disabled="isBusy"
          @click="saveEdit"
        >
          <i class="bi bi-check-lg"></i> 저장
        </button>
        <button
          type="button"
          class="btn-custom btn-custom-sm btn-custom-outline-secondary"
          :disabled="isBusy"
          @click="cancelEdit"
        >
          취소
        </button>
      </div>
    </template>
    <template v-else>
      <span
        class="transaction-icon"
        :class="todo.completed ? 'icon-done' : 'bg-forest-light text-lime'"
      >
        <i
          class="bi"
          :class="todo.completed ? 'bi-check-circle-fill' : 'bi-circle'"
        ></i>
      </span>
      <div class="transaction-info">
        <div class="transaction-name" :class="{ done: todo.completed }">
          {{ todo.title }}
        </div>
        <div v-if="todo.description" class="transaction-date">
          {{ todo.description }}
        </div>
      </div>
      <span class="todo-status" :class="{ done: todo.completed }">
        {{ todo.completed ? "완료" : "미완료" }}
      </span>
      <div class="actions">
        <button
          type="button"
          class="btn-custom btn-custom-sm btn-custom-primary"
          :disabled="isBusy"
          @click="toggleCompleted"
        >
          {{ todo.completed ? "미완료로 변경" : "완료로 변경" }}
        </button>
        <button
          type="button"
          class="btn-custom btn-custom-sm btn-custom-outline-secondary"
          :disabled="isBusy"
          @click="startEdit"
        >
          수정
        </button>
        <button
          type="button"
          class="btn-custom btn-custom-sm btn-custom-outline-danger"
          :disabled="isBusy"
          @click="remove"
        >
          삭제
        </button>
      </div>
    </template>
    <p v-if="errorMessage" class="form-feedback-custom item-error">
      {{ errorMessage }}
    </p>
  </li>
</template>

<style scoped>
.todo-item {
  flex-wrap: wrap;
}
.transaction-icon.icon-done {
  background-color: var(--sys-green-bg);
  color: var(--sys-green);
}
.transaction-name.done {
  text-decoration: line-through;
  color: var(--text-muted-green);
}
.todo-status {
  flex-shrink: 0;
  font-size: 0.78rem;
  font-weight: 700;
  border-radius: 50rem;
  padding: 0.2rem 0.7rem;
  background-color: var(--sys-orange-bg);
  color: var(--sys-orange);
}
.todo-status.done {
  background-color: var(--sys-green-bg);
  color: var(--sys-green);
}
.actions {
  margin-left: auto;
  display: flex;
  gap: 0.4rem;
  flex-wrap: wrap;
}
.item-error {
  flex-basis: 100%;
  margin: 0;
}
@media (max-width: 576px) {
  .actions {
    width: 100%;
    margin-left: 0;
    justify-content: flex-end;
  }
  .todo-status {
    order: -1;
  }
}
</style>
