from fastapi import APIRouter, Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from typing import List
from .nlpapi.classifier import classify
from .nlpapi.config import Config
from .nlpapi.preprocess import preprocess
from .nlpapi.textData import InferenceText
from ..model import NLPModelName, validate_model_name


router = APIRouter(tags=["nlp"], prefix="/nlp")
templates = Jinja2Templates(directory="views")


@router.get("/")
async def get_web_for_nlp(request: Request):
    return templates.TemplateResponse("nlp.html")

@router.post("/inference/{model_name}")
async def get_inference_nlp(request: Request, model_name: NLPModelName, text_list: List[InferenceText]):
    if validate_model_name(model_name):
        #TODO set proper model_fn
        pass
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Invalid model_name")

    text_list = sorted(text_list, key=lambda text: text.id)
    lines_for_predict = []
    for inference_text in text_list:
        lines_for_predict.append(preprocess(inference_text.text))
    
    config = Config(model_fn="./trained_model/bert_clean.tok.slice.pth", lines=lines_for_predict, gpu_id=-1, batch_size=8)
    classified_lines = classify(config)
    
    # classify all lines
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
