from pydantic import BaseModel
from typing import List

class CreateMetricDTO(BaseModel):
    llm: str

    class Config:
        json_schema_extra = {
            "example": {
                "metric": "TTFT"
            }
        }