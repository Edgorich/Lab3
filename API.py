from fastapi import APIRouter
from model import *

apps = APIRouter(prefix="/get-text")


@apps.get("")
async def get_text(text):
    result = classifier(text)
    response = {'label': result[0]["label"], 'score': result[0]["score"]}
    return response

