<script setup>
import TodoList from './components/TodoList.vue'
</script>

<template>
  <div class="main-wrapper">
    <header class="navbar-custom">
      <div class="navbar-left">
        <span class="footer-logo"><i class="bi bi-asterisk"></i> Todo App</span>
      </div>
      <div class="navbar-actions"></div>
    </header>

    <div class="page-header">
      <div>
        <h1 class="page-title">Todo App</h1>
        <p class="page-subtitle">할 일을 빠르게 만들고, 한눈에 확인하고, 완료하세요.</p>
      </div>
    </div>

    <TodoList />

    <footer class="footer-custom">
      <div class="footer-left">
        <span class="footer-logo"><i class="bi bi-asterisk"></i> Todo App</span>
        <span class="footer-separator">|</span>
        <span class="footer-copy">
          UI:
          <a href="https://themewagon.com/themes/spark/" target="_blank" rel="noopener">Spark Admin</a>
          by
          <a href="https://www.themewagon.com/" target="_blank" rel="noopener">ThemeWagon</a>
        </span>
      </div>
    </footer>
  </div>
</template>
