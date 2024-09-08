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
    

class SimulationResultModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    llm: str
    metric: str
    data_points: List[float]

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "llm": "TTFT",
                "metric": "TTFT",
                "data_points": [0.1, 0.2, 0.3]
            }
        }