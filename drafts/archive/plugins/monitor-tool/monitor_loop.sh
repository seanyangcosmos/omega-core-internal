#!/bin/zsh

cd "$(dirname "$0")"

echo "開始語義監控，每 10 秒檢測一次"

while true; do
    python3 semantic_batch.py
    sleep 10
done
