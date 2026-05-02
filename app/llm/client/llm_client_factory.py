from app.llm.client.llm_client import LlmClient
from app.llm.client.google_gemini_client import GoogleGeminiClient

class LLmClientFactory:
    @staticmethod
    def create(llm_client_type: str) -> LlmClient:
        if llm_client_type == "google":
            return GoogleGeminiClient()
        
        raise ValueError(f"Unknow client type : {llm_client_type}")