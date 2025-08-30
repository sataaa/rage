from sentence_transformers import SentenceTransformer
from typing import List

class LLMAdapter:
    """
    An adapter class to interact with the LLM and embedding models.
    This encapsulates the details of the model implementation and keeps it separate from the
    application's core logic.
    """

    def __init__(self):
        """
        Initializes the SentenceTransformer model.
        """
        try:
            model = 'Qwen/Qwen3-Embedding-0.6B'
            print(f"Loading SentenceTransformer model ({model})")
            self.embedding_model = SentenceTransformer(model)
            print("Successfully loaded SentenceTransformer model.")
        except Exception as e:
            print(f"Error loading SentenceTransformer model: {e}")
            self.embedding_model = None

    def get_embeddings(self, text: str) -> List[float]:
        """
        Generates and returns embeddings for a given text.
        
        Args:
            text: The input text to embed.
        
        Returns:
            A list of floats representing the embeddings.
        """
        if not self.embedding_model:
            raise RuntimeError("Embedding model is not loaded.")
        
        embeddings = self.embedding_model.encode(text).tolist()
        return embeddings

    def get_chat_response(self, prompt: str) -> str:
        """
        Generates and returns a chat response from the LLM.
        
        Args:
            prompt: The user's input prompt.
            
        Returns:
            The generated chat response.
        """
        # In your final implementation, you would use llama-cpp-python here.
        # For now, we'll return a static, mock response.
        print(f"Generating chat response for prompt: '{prompt}'")
        return f"Hello from the FastAPI server! Your prompt was: {prompt}"