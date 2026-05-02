from google import genai

from app.llm.client.llm_client import LlmClient


class GoogleGeminiClient(LlmClient):
    def __init__(self):
        self.client = genai.Client()

    def call(self, input):
        response = self.client.models.generate_content(
            model="gemini-3-flash-preview", contents=f"{input}"
        )
        return response.text
