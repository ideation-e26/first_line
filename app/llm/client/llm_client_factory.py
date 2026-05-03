from app.llm.client.google_gemini_client import GoogleGeminiClient
from app.llm.client.llm_client import LlmClient


class LLmClientFactory:
    @staticmethod
    def create(llm_client_type: str) -> LlmClient:
        if llm_client_type == "google":
            return GoogleGeminiClient()

        raise ValueError(f"Unknow client type : {llm_client_type}")
