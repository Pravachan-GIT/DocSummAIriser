from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AskRequest(BaseModel):
    question: str
    tenant_id: str

class AskResponse(BaseModel):
    answer: str
    sources: list

@router.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    return AskResponse(
        answer=f"You asked: '{request.question}'. AI answer coming in Phase 3!",
        sources=[]
    )