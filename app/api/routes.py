from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.container import Container
from app.core.schemas import UserInput
from app.llm.client.llm_client import LlmClient

router = APIRouter()


@router.get("/heartbeat")
def root():
    return {"status": "running"}


@router.post("/pre-triage")
@inject
async def pretriage(
    input: UserInput, llm_client: LlmClient = Depends(Provide[Container.llm_client])
):
    response = llm_client.call(input.text)
    return {"response": response}
