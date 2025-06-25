
import argparse
import json
import yaml
import os

# 假設的語義規則，後續可擴充
SEMANTIC_RULES = [
    "必須包含 '主體性'",
    "不得出現 '矛盾語法'",
    "語句結構需保持完整"
]

def load_file(file_path):
    if file_path.endswith(".json"):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    elif file_path.endswith(".yaml") or file_path.endswith(".yml"):
        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        raise ValueError("不支援的檔案格式。請使用 .txt, .json, .yaml")

def check_semantics(content, strict=False):
    issues = []

    # 簡單檢測
    if isinstance(content, dict) or isinstance(content, list):
        content_str = json.dumps(content, ensure_ascii=False)
    else:
        content_str = str(content)

    if "主體性" not in content_str:
        issues.append("缺少關鍵詞 '主體性'。")

    if "矛盾語法" in content_str:
        issues.append("發現不合規的 '矛盾語法'。")

    if strict:
        if len(content_str.strip()) < 20:
            issues.append("嚴格模式下，語義內容過短，結構不完整。")

    return issues

def main():
    parser = argparse.ArgumentParser(description="Sean Yang Core 語義檢測工具")
    parser.add_argument("--input", required=True, help="輸入檔案路徑（txt, json, yaml）")
    parser.add_argument("--output", default="semantic-check-result.json", help="結果輸出檔案")
    parser.add_argument("--strict", action="store_true", help="啟用嚴格檢測模式")

    args = parser.parse_args()

    try:
        content = load_file(args.input)
        issues = check_semantics(content, strict=args.strict)

        result = {
            "input_file": args.input,
            "issues_found": len(issues),
            "issues": issues
        }

        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print(f"語義檢測完成，結果已輸出至 {args.output}")
        if issues:
            print("發現問題：")
            for issue in issues:
                print(f"- {issue}")
        else:
            print("未發現語義問題。")

    except Exception as e:
        print(f"檢測過程出錯：{e}")

if __name__ == "__main__":
    main()
