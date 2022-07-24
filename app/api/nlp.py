from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from typing import List
from .nlpapi.classifier import classify
from .nlpapi.config import Config
from .nlpapi.preprocess import preprocess
from .nlpapi.textData import InferenceText


router = APIRouter(tags=["nlp"], prefix="/nlp")
templates = Jinja2Templates(directory="views")


@router.get("/")
async def get_web_for_nlp(request: Request):
    return templates.TemplateResponse("nlp.html")

@router.post("/inference")
async def get_inference_nlp(request: Request, text_list: List[InferenceText]):
    text_list = sorted(text_list, key=lambda text: text.id)
    lines_for_predict = []
    for inference_text in text_list:
        lines_for_predict.append(preprocess(inference_text.text))
    config = Config(model_fn="./trained_model/bert_clean.tok.slice.pth", lines=lines_for_predict, gpu_id=-1, batch_size=8)
    classified_lines = classify(config)
    classification_result = []
    for i, classified_line in enumerate(classified_lines):
        inference_text = InferenceText(
            id=text_list[i].id,
            text=classified_line[2]
        )
        inference_text.probability = classified_line[0]
        inference_text.ad = classified_line[1]
        classification_result.append(inference_text)
    return classification_result
