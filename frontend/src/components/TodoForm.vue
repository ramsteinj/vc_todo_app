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
    <input
      v-model="title"
      type="text"
      class="form-control-custom"
      placeholder="할 일 제목"
    />
    <input
      v-model="description"
      type="text"
      class="form-control-custom"
      placeholder="설명 (선택)"
    />
    <button
      type="submit"
      class="btn-custom btn-custom-primary"
      :disabled="isSubmitting"
    >
      <i class="bi bi-plus-lg"></i>
      {{ isSubmitting ? "저장 중..." : "추가" }}
    </button>
    <p v-if="errorMessage" class="form-feedback-custom form-error">
      {{ errorMessage }}
    </p>
  </form>
</template>

<style scoped>
.todo-form {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin-bottom: 1.25rem;
}
.todo-form .form-control-custom {
  flex: 1 1 160px;
  width: auto;
  min-width: 0;
}
.todo-form .btn-custom {
  flex-shrink: 0;
}
.form-error {
  flex-basis: 100%;
  margin: 0;
}
@media (max-width: 576px) {
  .todo-form .form-control-custom,
  .todo-form .btn-custom {
    flex-basis: 100%;
  }
}
</style>
