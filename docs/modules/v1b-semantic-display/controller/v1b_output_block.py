from core_engine.core_judgement import analyse_subject_type
from gpt_module.gpt_advice_generator import generate_advice
from display.formatter import format_result

def run_v1b_pipeline(sentence):
    subject_type = analyse_subject_type(sentence)
    advice = generate_advice(sentence, subject_type)
    return format_result(sentence, subject_type, advice)
