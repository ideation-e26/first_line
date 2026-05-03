from abc import ABC, abstractmethod


class LlmClient(ABC):
    @abstractmethod
    def call(self, input):
        pass
