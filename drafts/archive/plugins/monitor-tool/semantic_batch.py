import sys
sys.path.append("../rule-manager")
from rule_loader import load_rules

import os
import json
import sys
from datetime import datetime

TARGET_DIR = "../terminal-tool"
LOG_DIR = "./logs"
SEMANTIC_RULES = load_rules()

def check_semantics(text):
    problems = []
    for rule in SEMANTIC_RULES:
        if rule["type"] == "required" and rule["keyword"] not in text:
            problems.append(rule["message"])
        if rule["type"] == "forbidden" and rule["keyword"] in text:
            problems.append(rule["message"])
    return problems

def main():
    for file in os.listdir(TARGET_DIR):
        if file.endswith(".txt"):
            filepath = os.path.join(TARGET_DIR, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            problems = check_semantics(content)
            result = {
                "file": filepath,
                "problems": problems,
                "timestamp": datetime.now().isoformat()
            }
            outname = f"{file}.json"
            outpath = os.path.join(LOG_DIR, outname)
            with open(outpath, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            print(f"檢測完成：{file} → {outpath}")

if __name__ == "__main__":
    main()
