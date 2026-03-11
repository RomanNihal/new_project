from fastapi import APIRouter
from app.api.schema.chat import ChatRequest, ChatResponse
from app.services.chat.chat import llm_service
import uuid

router = APIRouter()

@router.post('/chat', response_model=ChatResponse, tags=['Chat'])
def chat(request: ChatRequest):
    if not request.session_id:
        request.session_id = str(uuid.uuid4())
        
    response_data = llm_service(request)
    return response_data
