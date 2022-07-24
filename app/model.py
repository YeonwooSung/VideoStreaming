from enum import Enum


class NLPModelName(str, Enum):
    bert = "bert"
    kobert = "kobert"
    roberta = "roberta"

def validate_model_name(model_name: str):
    if model_name not in NLPModelName:
        return False
    return True
