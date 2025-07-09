#!/bin/bash

# 🧠 設定資料夾與頁面檔案
TARGET_DIR="docs"
COMMIT_MSG="Auto-deploy: update GitHub Pages content"

# 🪛 確保在專案根目錄
cd "$(dirname "$0")"

# 🧾 加入所有變動檔案
git add $TARGET_DIR

# 🧾 自動建立 commit（若有變更）
git commit -m "$COMMIT_MSG"

# 🚀 推送到 GitHub（main 分支）
git push origin main

echo "✅ GitHub Pages 自動部署完成"

