from fastapi import APIRouter, Depends
from core.domain.entities import EmbeddingRequest, EmbeddingResponse
from infra.adapters.llm_adapter import LLMAdapter
from api.v1.endpoints.dependencies import get_llm_adapter
import datetime

# Create a FastAPI router for embeddings-related endpoints.
embeddings_router = APIRouter()

@embeddings_router.post("/embeddings", response_model=EmbeddingResponse)
async def create_embeddings(request_body: EmbeddingRequest, llm_adapter: LLMAdapter = Depends(get_llm_adapter)):
    """
    Generates and returns embeddings for the provided text using the embedding model.
    """
    embeddings = llm_adapter.get_embeddings(request_body.text)
    timestamp = datetime.datetime.now().isoformat()
    print(f"[{timestamp}] Received embeddings text: '{request_body.text}'")

    return EmbeddingResponse(embeddings=embeddings, model=llm_adapter.model)
