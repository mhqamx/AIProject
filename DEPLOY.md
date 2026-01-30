# 部署说明

## 推送到GitHub

由于需要身份验证,请使用以下命令推送代码:

```bash
git push origin main
```

如果遇到认证问题,请使用GitHub Personal Access Token:

1. 在GitHub上生成Personal Access Token
2. 使用以下格式推送:
```bash
git push https://YOUR_TOKEN@github.com/mhqamx/AIProject.git main
```

或者配置Git凭证:
```bash
git config credential.helper store
git push origin main
# 然后输入用户名和Personal Access Token
```

## 在GitHub Codespace中查看

1. 打开 https://github.com/mhqamx/AIProject
2. 点击 Code -> Codespaces -> Create codespace on main
3. 等待环境初始化完成
4. 在终端运行:
```bash
cd todo-app
npm install
npm run dev
```

## 本地开发

```bash
cd todo-app
npm install
npm run dev
```

访问 http://localhost:5173 查看应用

## 项目功能

✅ 添加新任务
✅ 标记任务为完成/未完成
✅ 删除任务
✅ 显示任务统计
✅ 美观的UI设计
✅ 流畅的动画效果
