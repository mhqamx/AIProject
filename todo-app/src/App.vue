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
  background:
    radial-gradient(ellipse at top, rgba(0, 255, 249, 0.15) 0%, transparent 50%),
    radial-gradient(ellipse at bottom, rgba(176, 0, 255, 0.15) 0%, transparent 50%),
    linear-gradient(180deg, #0a0a0f 0%, #1a0a1f 50%, #0a0a0f 100%);
  padding: 1rem;
  position: relative;
  overflow-x: hidden;
}

#app::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background:
    radial-gradient(2px 2px at 20% 30%, rgba(0, 255, 249, 0.3), transparent),
    radial-gradient(2px 2px at 60% 70%, rgba(255, 0, 255, 0.3), transparent),
    radial-gradient(1px 1px at 50% 50%, rgba(176, 0, 255, 0.2), transparent),
    radial-gradient(1px 1px at 80% 10%, rgba(0, 255, 249, 0.2), transparent);
  background-size: 200px 200px, 300px 300px, 250px 250px, 150px 150px;
  background-position: 0 0, 40px 60px, 130px 270px, 70px 100px;
  opacity: 0.4;
  pointer-events: none;
  z-index: 0;
  animation: stars-move 60s linear infinite;
}

@keyframes stars-move {
  from {
    transform: translateY(0);
  }
  to {
    transform: translateY(-200px);
  }
}
</style>
