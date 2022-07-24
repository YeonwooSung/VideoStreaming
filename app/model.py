from enum import Enum


class NLPModelName(str, Enum):
    bert_multilingual = "bert-base-multilingual-uncased"
    bert = "klue/bert-base"
    roberta = "klue/roberta-base"
    roberta_large = "klue/roberta-large"

def validate_model_name(model_name: str):
    if hasattr(NLPModelName, model_name):
        return True
    return False
