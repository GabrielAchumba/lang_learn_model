from pydantic import BaseModel, Field
from typing import Optional, List
from bson import ObjectId

# Helper class to handle MongoDB ObjectId conversion
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, field=None):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)
    

class LLMModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    llm: str

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "llm": "GPT-4o"
            }
        }