from abc import ABC, abstractmethod
from ...dtos.llm_dto import CreateLLMDTO
from ...models.llm_model import LLMModel
from typing import Optional, List

class ILLMService(ABC):
    
    @abstractmethod
    async def create_llm(self, llm_dto : CreateLLMDTO) -> LLMModel:
        pass

    @abstractmethod
    async def get_llms(self) -> List[LLMModel]:
        pass

    @abstractmethod
    async def get_llm(self, llm_id: str) -> Optional[LLMModel]:
        pass

    @abstractmethod
    async def update_llm(self, llm_id: str, llm_dto: CreateLLMDTO) -> Optional[LLMModel]:
        pass

    @abstractmethod
    async def delete_llm(self, llm_id: str) -> bool:
        pass