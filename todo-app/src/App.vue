<script setup>
import TodoList from './components/TodoList.vue'
</script>

<template>
  <div id="app">
    <TodoList />
  </div>
</template>

<style scoped>
#app {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 1rem;
}
</style>
