from infra.adapters.llm_adapter import LLMAdapter

# Instantiate the LLMAdapter as a singleton. 
llm_adapter = LLMAdapter()

def get_llm_adapter() -> LLMAdapter:
    """
    Dependency injector for the LLMAdapter.
    """
    return llm_adapter

