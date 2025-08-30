from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    """
    Represents the input for a chat request.
    """
    prompt: str

class EmbeddingRequest(BaseModel):
    """
    Represents the input for an embeddings request.
    """
    text: str

class EmbeddingResponse(BaseModel):
    """
    Represents the output for an embeddings request.
    """
    embeddings: List[float]
    model: str
