#!/bin/bash

# Git推送脚本
# 使用方法: ./push.sh

echo "准备推送到GitHub..."

# 检查是否有未提交的更改
if [[ -n $(git status -s) ]]; then
    echo "发现未提交的更改:"
    git status -s
    read -p "是否要先提交这些更改? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git add .
        read -p "请输入提交信息: " commit_msg
        git commit -m "$commit_msg"
    fi
fi

# 推送到GitHub
echo "正在推送到GitHub..."
git push origin main

if [ $? -eq 0 ]; then
    echo "✅ 推送成功!"
    echo "在Codespace中查看: https://github.com/mhqamx/AIProject"
else
    echo "❌ 推送失败"
    echo ""
    echo "如果遇到认证问题,请尝试:"
    echo "1. 生成GitHub Personal Access Token"
    echo "2. 运行: git config credential.helper store"
    echo "3. 再次运行: git push origin main"
    echo "4. 输入用户名和Token作为密码"
fi
