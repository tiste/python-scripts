from fastapi import APIRouter

from api.services.openai_service import ask_chatgpt

router = APIRouter()


@router.get("/gpt")
def gpt_response(prompt: str = "Dis bonjour"):
    return {"response": ask_chatgpt(prompt)}
