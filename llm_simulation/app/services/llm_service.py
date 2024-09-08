import motor.motor_asyncio
from bson import ObjectId
from ..models.llm_model import LLMModel
from ..dtos.llm_dto import CreateLLMDTO
from typing import List, Optional
import os
from dotenv import load_dotenv
from ..interfaces.llm.llm_service_interface import ILLMService



load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")

# Initialize MongoDB client
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]
llms_collection = db['llms']


class LLMService(ILLMService):
    async def create_llm(self, create_llm_dto: CreateLLMDTO) -> LLMModel:
        new_create_llm_dto = create_llm_dto.dict()
        result = await llms_collection.insert_one(new_create_llm_dto)
        created_llm = await llms_collection.find_one({"_id": result.inserted_id})
        return LLMModel(**created_llm)

    async def get_llms(self) -> List[LLMModel]:
        llms = []
        async for llm in llms_collection.find():
            llms.append(LLMModel(**llm))
        return llms

    async def get_llm(self, llm_id: str) -> Optional[LLMModel]:
        llm = await llms_collection.find_one({"_id": ObjectId(llm_id)})
        if llm:
            return LLMModel(**llm)
        return None

    async def update_llm(self, llm_id: str, create_llm_dto: CreateLLMDTO) -> Optional[LLMModel]:
        update_data = {k: v for k, v in create_llm_dto.dict().items() if v is not None}
        await llms_collection.update_one({"_id": ObjectId(llm_id)}, {"$set": update_data})
        updated_llm = await llms_collection.find_one({"_id": ObjectId(llm_id)})
        if updated_llm:
            return LLMModel(**updated_llm)
        return None

    async def delete_llm(self, llm_id: str) -> bool:
        result = await llms_collection.delete_one({"_id": ObjectId(llm_id)})
        return result.deleted_count > 0