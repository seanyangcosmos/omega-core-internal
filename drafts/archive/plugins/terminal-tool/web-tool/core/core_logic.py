from core.semantic.detector import detect_contradictions
from core.gpt_integration.gpt_handler import get_gpt_feedback

def analyze_text(text):
    local_result = detect_contradictions(text)
    gpt_result = get_gpt_feedback(text)
    return local_result, gpt_result
