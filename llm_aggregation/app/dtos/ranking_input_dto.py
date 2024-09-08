from pydantic import BaseModel

class RankingInputDTO(BaseModel):
    metric: str
    first_set_numbers: int

    class Config:
        json_schema_extra = {
            "example": {
                "metric": "TTFT",
                "first_set_numbers": 3
            }
        }