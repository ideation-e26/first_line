from dependency_injector import containers, providers
from app.llm.client.llm_client_factory import LLmClientFactory

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    llm_client = providers.Singleton(
        LLmClientFactory.create,
        config.llm_client_type
    )
