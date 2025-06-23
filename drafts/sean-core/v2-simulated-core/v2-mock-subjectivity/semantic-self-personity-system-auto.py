import time
import os
import subprocess

structure_path = '../semantic-structure.json'
check_interval = 2  # 每2秒檢查一次

print("啟動語義自我語氣系統，自動監控結構變動...")

# 記錄初始修改時間
last_mtime = os.path.getmtime(structure_path)

while True:
    current_mtime = os.path.getmtime(structure_path)
    
    if current_mtime != last_mtime:
        print("偵測到語義結構變動，自我語義輸出啟動...")

        # 執行語氣輸出系統（此處呼叫 v2 版本，您可改為其他版本）
        subprocess.run(["python", "semantic-self-personality-system-v2.py"])
        
        last_mtime = current_mtime

    time.sleep(check_interval)
