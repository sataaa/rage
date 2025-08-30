from fastapi import FastAPI
import uvicorn
from api.v1.endpoints.chat import chat_router
from api.v1.endpoints.embeddings import embeddings_router

print("Loaded class main.py")

app = FastAPI(title="Rage AI Server")

app.include_router(chat_router, tags=["Chat"])
app.include_router(embeddings_router, tags=["Embeddings"])