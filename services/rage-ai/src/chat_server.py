from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import datetime

app = FastAPI(title="Rage AI Chat Server")

class ChatRequest(BaseModel):
    prompt: str

# In-memory log to keep track of requests for a simple "log"
request_log = []

@app.post("/chat")
async def chat_endpoint(request_body: ChatRequest):
    """
    Handles chat requests and provides a static response.
    Logs the request to an in-memory list.
    """
    timestamp = datetime.datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "received_prompt": request_body.prompt,
        "response": "This is a placeholder response from the FastAPI server."
    }
    
    request_log.append(log_entry)
    if len(request_log) > 100:
        request_log.pop(0)

    print(f"[{timestamp}] Received prompt: '{request_body.prompt}'")
    
    return {"message": "Hello from the FastAPI server! Your prompt was: " + request_body.prompt}

@app.get("/logs")
async def get_logs():
    """
    Returns the in-memory log of the last 100 chat requests.
    """
    return {"logs": request_log}


def main():
    """
    Main function to run the FastAPI application with uvicorn.
    """
    print("Starting FastAPI chat server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
if __name__ == "__main__":
    main()