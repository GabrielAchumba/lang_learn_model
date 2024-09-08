from pydantic import BaseModel
from typing import List

class CreateLLMDTO(BaseModel):
    llm: str

    class Config:
        json_schema_extra = {
            "example": {
                "llm": "GPT-4o"
            }
        }