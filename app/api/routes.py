from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from app.container import Container
from app.llm.client.llm_client import LlmClient
from app.core.schemas import UserInput

router = APIRouter()

@router.get("/heartbeat")
def root():
    return {"status": "running"}

@router.post("/pre-triage")
@inject
async def pretriage(input: UserInput, llm_client: LlmClient = Depends(Provide[Container.llm_client])):
    response = llm_client.call(input.text)
    return {"response": response}