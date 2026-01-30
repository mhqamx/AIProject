<template>
  <div class="todo-container">
    <div class="todo-header">
      <h1>📝 我的待办清单</h1>
      <div class="stats">
        <span class="stat-item">总计: {{ todos.length }}</span>
        <span class="stat-item completed">已完成: {{ completedCount }}</span>
        <span class="stat-item pending">未完成: {{ pendingCount }}</span>
      </div>
    </div>

    <div class="todo-input-wrapper">
      <input
        v-model="newTodo"
        type="text"
        class="todo-input"
        placeholder="添加新任务..."
        @keyup.enter="addTodo"
      />
      <button class="add-btn" @click="addTodo" :disabled="!newTodo.trim()">
        添加
      </button>
    </div>

    <div class="todo-list">
      <transition-group name="todo-list">
        <div
          v-for="todo in todos"
          :key="todo.id"
          class="todo-item"
          :class="{ completed: todo.completed }"
        >
          <div class="todo-content">
            <input
              type="checkbox"
              :checked="todo.completed"
              @change="toggleTodo(todo.id)"
              class="todo-checkbox"
            />
            <span class="todo-text">{{ todo.text }}</span>
          </div>
          <button class="delete-btn" @click="deleteTodo(todo.id)">
            删除
          </button>
        </div>
      </transition-group>

      <div v-if="todos.length === 0" class="empty-state">
        <p>暂无待办事项</p>
        <p class="empty-hint">添加第一个任务开始吧！</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

// 响应式状态
const newTodo = ref('')
const todos = ref([
  { id: 1, text: '学习 Vue 3 Composition API', completed: false },
  { id: 2, text: '完成 TodoList 项目', completed: false },
  { id: 3, text: '提交代码到 GitHub', completed: false }
])

// 计算属性
const completedCount = computed(() => {
  return todos.value.filter(todo => todo.completed).length
})

const pendingCount = computed(() => {
  return todos.value.filter(todo => !todo.completed).length
})

// 方法
const addTodo = () => {
  const text = newTodo.value.trim()
  if (!text) return

  todos.value.push({
    id: Date.now(),
    text,
    completed: false
  })
  newTodo.value = ''
}

const toggleTodo = (id) => {
  const todo = todos.value.find(t => t.id === id)
  if (todo) {
    todo.completed = !todo.completed
  }
}

const deleteTodo = (id) => {
  const index = todos.value.findIndex(t => t.id === id)
  if (index !== -1) {
    todos.value.splice(index, 1)
  }
}
</script>

<style scoped>
.todo-container {
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.todo-header {
  margin-bottom: 2rem;
  text-align: center;
}

.todo-header h1 {
  margin: 0 0 1rem 0;
  color: #2c3e50;
  font-size: 2rem;
}

.stats {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.stat-item {
  padding: 0.5rem 1rem;
  background: #f0f0f0;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 500;
}

.stat-item.completed {
  background: #d4edda;
  color: #155724;
}

.stat-item.pending {
  background: #fff3cd;
  color: #856404;
}

.todo-input-wrapper {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.todo-input {
  flex: 1;
  padding: 0.75rem 1rem;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.todo-input:focus {
  outline: none;
  border-color: #42b983;
}

.add-btn {
  padding: 0.75rem 1.5rem;
  background: #42b983;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s;
  font-weight: 500;
}

.add-btn:hover:not(:disabled) {
  background: #33a06f;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(66, 185, 131, 0.3);
}

.add-btn:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.todo-list {
  min-height: 200px;
}

.todo-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  margin-bottom: 0.75rem;
  background: #f8f9fa;
  border-radius: 8px;
  border-left: 4px solid #42b983;
  transition: all 0.3s;
}

.todo-item:hover {
  transform: translateX(4px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.todo-item.completed {
  border-left-color: #95a5a6;
  opacity: 0.7;
}

.todo-content {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex: 1;
}

.todo-checkbox {
  width: 20px;
  height: 20px;
  cursor: pointer;
}

.todo-text {
  font-size: 1rem;
  color: #2c3e50;
  transition: all 0.3s;
}

.todo-item.completed .todo-text {
  text-decoration: line-through;
  color: #95a5a6;
}

.delete-btn {
  padding: 0.5rem 1rem;
  background: #e74c3c;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.3s;
  font-weight: 500;
}

.delete-btn:hover {
  background: #c0392b;
  transform: scale(1.05);
}

.empty-state {
  text-align: center;
  padding: 3rem 1rem;
  color: #95a5a6;
}

.empty-state p {
  margin: 0.5rem 0;
  font-size: 1.1rem;
}

.empty-hint {
  font-size: 0.9rem;
}

/* 过渡动画 */
.todo-list-enter-active,
.todo-list-leave-active {
  transition: all 0.3s ease;
}

.todo-list-enter-from {
  opacity: 0;
  transform: translateX(-30px);
}

.todo-list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}
</style>
