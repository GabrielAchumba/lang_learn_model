from pydantic import BaseModel
from typing import List

class SimulationInputDTO(BaseModel):
    data_points: int
    start_number: float
    end_number: float

    class Config:
        json_schema_extra = {
            "example": {
                "data_points": 100,
                "start_number": 0.1,
                "end_number": 1.0
            }
        }