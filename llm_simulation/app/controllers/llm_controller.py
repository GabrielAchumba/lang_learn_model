from fastapi import Depends, HTTPException
from ..services.llm_service import LLMService
from ..interfaces.llm.llm_service_interface import ILLMService
from ..dtos.llm_dto import CreateLLMDTO
from ..models.llm_model import LLMModel
from ..interfaces.llm.llm_controller_interface import ILLMController
from typing import List

# Inject the LLMService using the ILLMService interface
async def get_llm_service() -> ILLMService:
    return LLMService()

# Inject the LLMController with the LLMService as dependency
async def get_llm_controller(service: ILLMService = Depends(get_llm_service)):
    return LLMController(service)

class LLMController(ILLMController):
    def __init__(self, llm_service: ILLMService):
        self.llm_service = llm_service

    async def create_llm_controller(self, llm_data: CreateLLMDTO) -> LLMModel:
        return await self.llm_service.create_llm(llm_data)

    async def get_all_llms_controller(self) -> List[LLMModel]:
        return await self.llm_service.get_llms()

    async def get_llm_controller(self, llm_id: str) -> LLMModel:
        llm = await self.llm_service.get_llm(llm_id)
        if not llm:
            raise HTTPException(status_code=404, detail="LLM not found")
        return llm

    async def update_llm_controller(self, llm_id: str, llm_data: CreateLLMDTO) -> LLMModel:
        updated_llm = await self.llm_service.update_llm(llm_id, llm_data)
        if not updated_llm:
            raise HTTPException(status_code=404, detail="LLM not found")
        return updated_llm

    async def delete_llm_controller(self, llm_id: str) -> dict:
        success = await self.llm_service.delete_llm(llm_id)
        if not success:
            raise HTTPException(status_code=404, detail="LLM not found")
        return {"message": "LLM deleted successfully"}