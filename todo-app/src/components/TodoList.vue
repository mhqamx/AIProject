<template>
  <div class="cyber-container">
    <!-- 网格背景 -->
    <div class="grid-bg"></div>
    <div class="scanlines"></div>

    <!-- 主界面 -->
    <div class="main-panel">
      <!-- 头部 -->
      <div class="cyber-header">
        <div class="glitch-wrapper">
          <h1 class="glitch" data-text="TASK_PROTOCOL">TASK_PROTOCOL</h1>
        </div>
        <div class="system-info">
          <span class="info-tag">&lt;SYSTEM_ACTIVE&gt;</span>
          <span class="timestamp">{{ currentTime }}</span>
        </div>
      </div>

      <!-- 状态面板 -->
      <div class="stats-panel">
        <div class="stat-box">
          <div class="stat-label">TOTAL</div>
          <div class="stat-value">{{ String(todos.length).padStart(3, '0') }}</div>
          <div class="stat-bar"></div>
        </div>
        <div class="stat-box active">
          <div class="stat-label">ACTIVE</div>
          <div class="stat-value">{{ String(pendingCount).padStart(3, '0') }}</div>
          <div class="stat-bar"></div>
        </div>
        <div class="stat-box complete">
          <div class="stat-label">COMPLETE</div>
          <div class="stat-value">{{ String(completedCount).padStart(3, '0') }}</div>
          <div class="stat-bar"></div>
        </div>
      </div>

      <!-- 输入区域 -->
      <div class="input-zone">
        <div class="input-wrapper">
          <span class="input-prefix">&gt;_</span>
          <input
            v-model="newTodo"
            type="text"
            class="cyber-input"
            placeholder="INITIALIZE_NEW_TASK..."
            @keyup.enter="addTodo"
          />
          <div class="input-glow"></div>
        </div>
        <button
          class="cyber-btn"
          @click="addTodo"
          :disabled="!newTodo.trim()"
        >
          <span class="btn-text">EXECUTE</span>
          <div class="btn-glow"></div>
        </button>
      </div>

      <!-- 任务列表 -->
      <div class="task-list">
        <transition-group name="task" @before-enter="beforeEnter" @enter="enter">
          <div
            v-for="(todo, index) in todos"
            :key="todo.id"
            :data-index="index"
            class="task-item"
            :class="{ 'task-complete': todo.completed }"
          >
            <div class="task-id">#{{ String(index + 1).padStart(3, '0') }}</div>

            <div class="checkbox-wrapper" @click="toggleTodo(todo.id)">
              <div class="cyber-checkbox" :class="{ checked: todo.completed }">
                <div class="checkbox-inner">
                  <svg class="check-icon" viewBox="0 0 24 24">
                    <polyline points="20 6 9 17 4 12"></polyline>
                  </svg>
                </div>
              </div>
            </div>

            <div class="task-content">
              <span class="task-text">{{ todo.text }}</span>
              <div class="task-underline"></div>
            </div>

            <button class="delete-btn" @click="deleteTodo(todo.id)">
              <svg class="delete-icon" viewBox="0 0 24 24">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
              <span>DELETE</span>
            </button>
          </div>
        </transition-group>

        <div v-if="todos.length === 0" class="empty-state">
          <div class="empty-icon">⚠</div>
          <p class="empty-text">NO_ACTIVE_TASKS</p>
          <p class="empty-hint">// Initialize first task to begin protocol</p>
        </div>
      </div>
    </div>

    <!-- 角落装饰 -->
    <div class="corner-deco top-left"></div>
    <div class="corner-deco top-right"></div>
    <div class="corner-deco bottom-left"></div>
    <div class="corner-deco bottom-right"></div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

// 响应式状态
const newTodo = ref('')
const currentTime = ref('')
const todos = ref([
  { id: 1, text: 'INITIALIZE NEURAL NETWORK PROTOCOL', completed: false },
  { id: 2, text: 'COMPILE QUANTUM ALGORITHMS', completed: false },
  { id: 3, text: 'DEPLOY TO CYBERNET', completed: false }
])

// 计算属性
const completedCount = computed(() => {
  return todos.value.filter(todo => todo.completed).length
})

const pendingCount = computed(() => {
  return todos.value.filter(todo => !todo.completed).length
})

// 更新时间
const updateTime = () => {
  const now = new Date()
  const hours = String(now.getHours()).padStart(2, '0')
  const minutes = String(now.getMinutes()).padStart(2, '0')
  const seconds = String(now.getSeconds()).padStart(2, '0')
  currentTime.value = `${hours}:${minutes}:${seconds}`
}

let timeInterval = null

onMounted(() => {
  updateTime()
  timeInterval = setInterval(updateTime, 1000)
})

onUnmounted(() => {
  if (timeInterval) clearInterval(timeInterval)
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

// 动画钩子
const beforeEnter = (el) => {
  el.style.opacity = 0
  el.style.transform = 'translateX(-50px)'
}

const enter = (el) => {
  const delay = el.dataset.index * 100
  setTimeout(() => {
    el.style.transition = 'all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1)'
    el.style.opacity = 1
    el.style.transform = 'translateX(0)'
  }, delay)
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');

/* ===== 配色变量 ===== */
:root {
  --cyan: #00fff9;
  --magenta: #ff00ff;
  --purple: #b000ff;
  --dark-bg: #0a0a0f;
  --panel-bg: rgba(15, 15, 25, 0.9);
  --border-color: rgba(0, 255, 249, 0.3);
}

/* ===== 容器 ===== */
.cyber-container {
  position: relative;
  max-width: 900px;
  margin: 2rem auto;
  padding: 2rem;
  min-height: 80vh;
}

/* ===== 网格背景 ===== */
.grid-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image:
    linear-gradient(var(--cyan) 1px, transparent 1px),
    linear-gradient(90deg, var(--cyan) 1px, transparent 1px);
  background-size: 50px 50px;
  opacity: 0.03;
  pointer-events: none;
  z-index: -1;
}

/* ===== 扫描线 ===== */
.scanlines {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: repeating-linear-gradient(
    0deg,
    rgba(0, 0, 0, 0.15),
    rgba(0, 0, 0, 0.15) 1px,
    transparent 1px,
    transparent 2px
  );
  pointer-events: none;
  z-index: 10;
  animation: scanline-move 8s linear infinite;
}

@keyframes scanline-move {
  0% { transform: translateY(0); }
  100% { transform: translateY(100px); }
}

/* ===== 主面板 ===== */
.main-panel {
  position: relative;
  background: var(--panel-bg);
  border: 2px solid var(--border-color);
  box-shadow:
    0 0 20px rgba(0, 255, 249, 0.2),
    inset 0 0 60px rgba(0, 255, 249, 0.05);
  padding: 2.5rem;
  clip-path: polygon(
    0 0,
    calc(100% - 20px) 0,
    100% 20px,
    100% 100%,
    20px 100%,
    0 calc(100% - 20px)
  );
}

/* ===== 头部 ===== */
.cyber-header {
  margin-bottom: 2.5rem;
  text-align: center;
}

.glitch-wrapper {
  margin-bottom: 1rem;
}

.glitch {
  font-family: 'Orbitron', monospace;
  font-size: 3rem;
  font-weight: 900;
  color: var(--cyan);
  text-shadow:
    0 0 10px var(--cyan),
    0 0 20px var(--cyan),
    0 0 40px var(--cyan);
  letter-spacing: 0.3em;
  margin: 0;
  position: relative;
  animation: glitch-text 3s infinite;
}

.glitch::before,
.glitch::after {
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.glitch::before {
  animation: glitch-before 2s infinite;
  color: var(--magenta);
  z-index: -1;
}

.glitch::after {
  animation: glitch-after 2s infinite;
  color: var(--purple);
  z-index: -2;
}

@keyframes glitch-text {
  0%, 100% { transform: translate(0); }
  20% { transform: translate(-2px, 2px); }
  40% { transform: translate(-2px, -2px); }
  60% { transform: translate(2px, 2px); }
  80% { transform: translate(2px, -2px); }
}

@keyframes glitch-before {
  0%, 100% { clip-path: inset(0 0 0 0); }
  20% { clip-path: inset(20% 0 60% 0); }
  40% { clip-path: inset(60% 0 20% 0); }
  60% { clip-path: inset(40% 0 40% 0); }
  80% { clip-path: inset(80% 0 10% 0); }
}

@keyframes glitch-after {
  0%, 100% { clip-path: inset(0 0 0 0); }
  20% { clip-path: inset(80% 0 10% 0); }
  40% { clip-path: inset(20% 0 60% 0); }
  60% { clip-path: inset(10% 0 80% 0); }
  80% { clip-path: inset(60% 0 20% 0); }
}

.system-info {
  display: flex;
  justify-content: center;
  gap: 2rem;
  font-family: 'Rajdhani', monospace;
  font-size: 0.9rem;
  color: var(--cyan);
  text-transform: uppercase;
  letter-spacing: 0.2em;
}

.info-tag, .timestamp {
  opacity: 0.7;
  animation: pulse-glow 2s ease-in-out infinite;
}

@keyframes pulse-glow {
  0%, 100% { opacity: 0.7; text-shadow: 0 0 5px var(--cyan); }
  50% { opacity: 1; text-shadow: 0 0 15px var(--cyan); }
}

/* ===== 状态面板 ===== */
.stats-panel {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  margin-bottom: 2.5rem;
}

.stat-box {
  background: rgba(0, 255, 249, 0.05);
  border: 1px solid var(--border-color);
  padding: 1.5rem;
  position: relative;
  overflow: hidden;
  transition: all 0.3s ease;
}

.stat-box::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(0, 255, 249, 0.2), transparent);
  transition: left 0.5s;
}

.stat-box:hover::before {
  left: 100%;
}

.stat-box:hover {
  border-color: var(--cyan);
  box-shadow: 0 0 20px rgba(0, 255, 249, 0.3);
  transform: translateY(-3px);
}

.stat-label {
  font-family: 'Rajdhani', monospace;
  font-size: 0.75rem;
  color: var(--cyan);
  letter-spacing: 0.3em;
  margin-bottom: 0.5rem;
  opacity: 0.7;
}

.stat-value {
  font-family: 'Orbitron', monospace;
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--cyan);
  text-shadow: 0 0 10px var(--cyan);
  line-height: 1;
}

.stat-box.active .stat-value {
  color: #ff00ff;
  text-shadow: 0 0 10px #ff00ff;
}

.stat-box.complete .stat-value {
  color: #00ff00;
  text-shadow: 0 0 10px #00ff00;
}

.stat-bar {
  height: 2px;
  background: var(--cyan);
  margin-top: 1rem;
  box-shadow: 0 0 10px var(--cyan);
  animation: bar-pulse 2s ease-in-out infinite;
}

@keyframes bar-pulse {
  0%, 100% { opacity: 0.5; }
  50% { opacity: 1; }
}

/* ===== 输入区域 ===== */
.input-zone {
  display: flex;
  gap: 1rem;
  margin-bottom: 2.5rem;
}

.input-wrapper {
  flex: 1;
  position: relative;
  display: flex;
  align-items: center;
  background: rgba(0, 255, 249, 0.05);
  border: 1px solid var(--border-color);
  padding: 0 1rem;
  transition: all 0.3s ease;
}

.input-wrapper:focus-within {
  border-color: var(--cyan);
  box-shadow: 0 0 20px rgba(0, 255, 249, 0.3);
}

.input-prefix {
  font-family: 'Orbitron', monospace;
  color: var(--cyan);
  margin-right: 0.5rem;
  font-size: 1.2rem;
  animation: cursor-blink 1s infinite;
}

@keyframes cursor-blink {
  0%, 49% { opacity: 1; }
  50%, 100% { opacity: 0.3; }
}

.cyber-input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  color: var(--cyan);
  font-family: 'Rajdhani', monospace;
  font-size: 1.1rem;
  padding: 1rem 0;
  letter-spacing: 0.1em;
}

.cyber-input::placeholder {
  color: rgba(0, 255, 249, 0.3);
  letter-spacing: 0.15em;
}

.input-glow {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--cyan);
  box-shadow: 0 0 10px var(--cyan);
  transition: width 0.3s ease;
}

.input-wrapper:focus-within .input-glow {
  width: 100%;
}

/* ===== 按钮 ===== */
.cyber-btn {
  position: relative;
  background: transparent;
  border: 2px solid var(--cyan);
  padding: 1rem 2rem;
  color: var(--cyan);
  font-family: 'Orbitron', monospace;
  font-size: 0.9rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  cursor: pointer;
  overflow: hidden;
  transition: all 0.3s ease;
  clip-path: polygon(0 0, calc(100% - 10px) 0, 100% 10px, 100% 100%, 10px 100%, 0 calc(100% - 10px));
}

.cyber-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: var(--cyan);
  transition: left 0.3s ease;
  z-index: -1;
}

.cyber-btn:hover:not(:disabled)::before {
  left: 0;
}

.cyber-btn:hover:not(:disabled) {
  color: #0a0a0f;
  box-shadow: 0 0 30px rgba(0, 255, 249, 0.6);
}

.cyber-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.btn-text {
  position: relative;
  z-index: 1;
}

/* ===== 任务列表 ===== */
.task-list {
  min-height: 300px;
}

.task-item {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  background: rgba(0, 255, 249, 0.03);
  border-left: 3px solid var(--cyan);
  padding: 1.25rem;
  margin-bottom: 1rem;
  position: relative;
  transition: all 0.3s ease;
}

.task-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 3px;
  height: 100%;
  background: var(--cyan);
  box-shadow: 0 0 10px var(--cyan);
}

.task-item:hover {
  background: rgba(0, 255, 249, 0.08);
  transform: translateX(5px);
  box-shadow: 0 0 20px rgba(0, 255, 249, 0.2);
}

.task-item.task-complete {
  opacity: 0.5;
  border-left-color: #666;
}

.task-item.task-complete::before {
  background: #666;
  box-shadow: none;
}

.task-id {
  font-family: 'Orbitron', monospace;
  font-size: 0.85rem;
  color: var(--cyan);
  opacity: 0.5;
  min-width: 40px;
}

/* ===== 自定义复选框 ===== */
.checkbox-wrapper {
  cursor: pointer;
}

.cyber-checkbox {
  width: 24px;
  height: 24px;
  border: 2px solid var(--cyan);
  position: relative;
  transition: all 0.3s ease;
  clip-path: polygon(0 0, calc(100% - 4px) 0, 100% 4px, 100% 100%, 4px 100%, 0 calc(100% - 4px));
}

.cyber-checkbox:hover {
  box-shadow: 0 0 15px rgba(0, 255, 249, 0.5);
}

.checkbox-inner {
  position: absolute;
  inset: 2px;
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.cyber-checkbox.checked .checkbox-inner {
  background: var(--cyan);
  box-shadow: 0 0 10px var(--cyan);
}

.check-icon {
  width: 14px;
  height: 14px;
  stroke: #0a0a0f;
  stroke-width: 3;
  fill: none;
  opacity: 0;
  transform: scale(0);
  transition: all 0.3s ease;
}

.cyber-checkbox.checked .check-icon {
  opacity: 1;
  transform: scale(1);
}

/* ===== 任务内容 ===== */
.task-content {
  flex: 1;
  position: relative;
}

.task-text {
  font-family: 'Rajdhani', monospace;
  font-size: 1.1rem;
  color: var(--cyan);
  letter-spacing: 0.05em;
  display: block;
  transition: all 0.3s ease;
}

.task-complete .task-text {
  text-decoration: line-through;
  opacity: 0.5;
}

.task-underline {
  height: 1px;
  background: linear-gradient(90deg, var(--cyan), transparent);
  margin-top: 0.5rem;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.3s ease;
}

.task-item:hover .task-underline {
  transform: scaleX(1);
}

/* ===== 删除按钮 ===== */
.delete-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: transparent;
  border: 1px solid rgba(255, 0, 102, 0.5);
  color: #ff0066;
  padding: 0.5rem 1rem;
  font-family: 'Rajdhani', monospace;
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  cursor: pointer;
  transition: all 0.3s ease;
  clip-path: polygon(5px 0, 100% 0, 100% calc(100% - 5px), calc(100% - 5px) 100%, 0 100%, 0 5px);
}

.delete-btn:hover {
  background: #ff0066;
  color: #0a0a0f;
  border-color: #ff0066;
  box-shadow: 0 0 20px rgba(255, 0, 102, 0.5);
}

.delete-icon {
  width: 16px;
  height: 16px;
  stroke: currentColor;
  stroke-width: 2;
}

/* ===== 空状态 ===== */
.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  opacity: 0.5;
}

.empty-icon {
  font-size: 4rem;
  color: var(--cyan);
  margin-bottom: 1rem;
  animation: pulse-glow 2s ease-in-out infinite;
}

.empty-text {
  font-family: 'Orbitron', monospace;
  font-size: 1.5rem;
  color: var(--cyan);
  letter-spacing: 0.3em;
  margin: 1rem 0;
}

.empty-hint {
  font-family: 'Rajdhani', monospace;
  color: var(--cyan);
  opacity: 0.5;
  font-size: 0.9rem;
  letter-spacing: 0.1em;
}

/* ===== 角落装饰 ===== */
.corner-deco {
  position: fixed;
  width: 100px;
  height: 100px;
  border: 2px solid var(--cyan);
  opacity: 0.3;
  pointer-events: none;
  z-index: 100;
}

.corner-deco.top-left {
  top: 20px;
  left: 20px;
  border-right: none;
  border-bottom: none;
  clip-path: polygon(0 0, 100% 0, 100% 2px, 2px 2px, 2px 100%, 0 100%);
}

.corner-deco.top-right {
  top: 20px;
  right: 20px;
  border-left: none;
  border-bottom: none;
  clip-path: polygon(0 0, 100% 0, 100% 100%, calc(100% - 2px) 100%, calc(100% - 2px) 2px, 0 2px);
}

.corner-deco.bottom-left {
  bottom: 20px;
  left: 20px;
  border-right: none;
  border-top: none;
  clip-path: polygon(0 0, 2px 0, 2px calc(100% - 2px), 100% calc(100% - 2px), 100% 100%, 0 100%);
}

.corner-deco.bottom-right {
  bottom: 20px;
  right: 20px;
  border-left: none;
  border-top: none;
  clip-path: polygon(0 calc(100% - 2px), 100% calc(100% - 2px), 100% 100%, 0 100%, 0 0, calc(100% - 2px) 0, calc(100% - 2px) calc(100% - 2px));
}

/* ===== 过渡动画 ===== */
.task-enter-active {
  transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.task-leave-active {
  transition: all 0.4s ease;
}

.task-enter-from {
  opacity: 0;
  transform: translateX(-50px) scale(0.9);
}

.task-leave-to {
  opacity: 0;
  transform: translateX(50px) scale(0.9);
}

/* ===== 响应式 ===== */
@media (max-width: 768px) {
  .glitch {
    font-size: 2rem;
    letter-spacing: 0.2em;
  }

  .stats-panel {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .input-zone {
    flex-direction: column;
  }

  .task-item {
    flex-wrap: wrap;
  }

  .task-id {
    order: -1;
    width: 100%;
    margin-bottom: 0.5rem;
  }
}
</style>
