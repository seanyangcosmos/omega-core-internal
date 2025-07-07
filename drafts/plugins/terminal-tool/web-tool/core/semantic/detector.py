from core.semantic.rules import rules

def detect_contradictions(text):
    problems = []
    for rule in rules:
        if all(keyword in text for keyword in rule["keywords"]):
            problems.append(rule["desc"])
    return problems
