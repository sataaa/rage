from fastapi import APIRouter, Depends
from core.domain.entities import ChatRequest
from infra.adapters.llm_adapter import LLMAdapter
from api.v1.endpoints.dependencies import get_llm_adapter
import datetime
from typing import List

chat_router = APIRouter()

@chat_router.post("/chat")
async def chat_endpoint(request_body: ChatRequest, llm_adapter: LLMAdapter = Depends(get_llm_adapter)):
    """
    Handles chat requests by calling the LLM adapter and logging the interaction.
    """
    timestamp = datetime.datetime.now().isoformat()
    response_message = llm_adapter.get_chat_response(request_body.prompt)
    response_data = {"message": response_message}
    
    print(f"[{timestamp}] Received prompt: '{request_body.prompt}'")
    
    return response_data
