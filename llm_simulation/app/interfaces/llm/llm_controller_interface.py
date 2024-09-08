from abc import ABC, abstractmethod
from ...dtos.llm_dto import CreateLLMDTO
from ...models.llm_model import LLMModel
from typing import List, Optional

class ILLMController(ABC):
    
    @abstractmethod
    async def create_llm_controller(self, llm_data: CreateLLMDTO) -> LLMModel:
        pass

    @abstractmethod
    async def get_all_llms_controller(self) -> List[LLMModel]:
        pass

    @abstractmethod
    async def get_llm_controller(self, llm_id: str) -> Optional[LLMModel]:
        pass

    @abstractmethod
    async def update_llm_controller(self, llm_id: str, llm_data: CreateLLMDTO) -> Optional[LLMModel]:
        pass

    @abstractmethod
    async def delete_llm_controller(self, llm_id: str) -> dict:
        pass