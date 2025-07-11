#!/bin/bash

cd "$(dirname "$0")"

echo "🚀 開始推送 V1-B 模組至 GitHub..."

# 確認目錄存在
if [ ! -d "docs/modules/v1b-semantic-display" ]; then
    echo "❌ 錯誤：v1b-semantic-display 資料夾不存在"
    exit 1
fi

# 加入新檔案與變更
git add docs/modules/v1b-semantic-display
git add docs/index.md

# 提交訊息
git commit -m "🧠 推送 V1-B 語義展示模組與連結更新"

# 推送至 GitHub（假設已有 git remote）
git push origin main

echo "✅ 推送完成，V1-B 模組已同步到 GitHub 倉庫"


