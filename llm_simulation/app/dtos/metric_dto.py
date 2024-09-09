from pydantic import BaseModel
from typing import List

class CreateMetricDTO(BaseModel):
    metric: str

    class Config:
        json_schema_extra = {
            "example": {
                "metric": "TTFT"
            }
        }