import re

contradiction_patterns = [
    ["昨天", "整天沒出門"],
    ["很餓", "不想吃東西"],
    ["請假", "來上班"],
    ["不想去", "已經去了"],
    ["今天", "不在家", "在家"],
]

def clean_text(text):
    text = re.sub(r"[^\u4e00-\u9fa5a-zA-Z0-9]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def extract_phrases(text):
    return text.split()

def fuzzy_match(pattern, phrase):
    return pattern in phrase or phrase in pattern

def detect_contradictions(text):
    text = clean_text(text)
    phrases = extract_phrases(text)
    problems = []

    for pattern in contradiction_patterns:
        hit_count = sum(1 for word in pattern if any(fuzzy_match(word, phrase) for phrase in phrases))
        if hit_count >= len(pattern):
            problems.append(f"語義矛盾：同時出現 {', '.join(pattern)}")

    return problems

def format_result(problems):
    if not problems:
        return "語義檢測結果：通順無矛盾"
    return "\n".join(problems)

