from fastapi import APIRouter, Depends
from ..controllers.llm_controller import LLMController, get_llm_controller
from ..dtos.llm_dto import CreateLLMDTO

# Create an APIRouter instance
llm_router = APIRouter()



@llm_router.post("/llms")
async def create_llm(llm_data: CreateLLMDTO, controller: LLMController = Depends(get_llm_controller)):
    return await controller.create_llm_controller(llm_data)


@llm_router.get("/llms")
async def get_all_llms(controller: LLMController = Depends(get_llm_controller)):
    print("seen")
    return await controller.get_all_llms_controller()


@llm_router.get("/llms/{llm_id}")
async def get_llm(llm_id: str, controller: LLMController = Depends(get_llm_controller)):
    return await controller.get_llm_controller(llm_id)


@llm_router.put("/llms/{llm_id}")
async def update_llm(llm_id: str, llm_data: CreateLLMDTO, controller: LLMController = Depends(get_llm_controller)):
    return await controller.update_llm_controller(llm_id, llm_data)


@llm_router.delete("/llms/{llm_id}")
async def delete_llm(llm_id: str, controller: LLMController = Depends(get_llm_controller)):
    return await controller.delete_llm_controller(llm_id)