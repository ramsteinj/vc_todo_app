const API_BASE = import.meta.env?.VITE_API_URL ?? "http://127.0.0.1:8000";
const TODOS_URL = `${API_BASE}/api/todos/`;

async function request(url, options = {}) {
  const response = await fetch(url, options);
  if (!response.ok) {
    const error = new Error("API 요청이 실패했습니다.");
    error.status = response.status;
    try {
      error.fieldErrors = await response.json();
    } catch {
      error.fieldErrors = null;
    }
    throw error;
  }
  if (response.status === 204) {
    return null;
  }
  return response.json();
}

export function fetchTodos() {
  return request(TODOS_URL);
}

export function createTodo(payload) {
  return request(TODOS_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
}

export function updateTodo(id, payload) {
  return request(`${TODOS_URL}${id}/`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
}

export function toggleTodo(id, completed) {
  return request(`${TODOS_URL}${id}/`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ completed }),
  });
}

export function deleteTodo(id) {
  return request(`${TODOS_URL}${id}/`, { method: "DELETE" });
}
