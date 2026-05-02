from fastapi import FastAPI

from app.api.routes import router
from app.container import Container


def create_app() -> FastAPI:
    container = Container()
    container.config.llm_client_type.from_env("LLM_CLIENT_TYPE", required=True)
    container.config.name.from_env("NAME", required=True)

    container.wire(modules=["app.api.routes"])

    app = FastAPI(title=f"{container.config.name} API")

    app.container = container

    app.include_router(router)

    return app


app = create_app()
