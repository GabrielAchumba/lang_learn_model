import motor.motor_asyncio
from bson import ObjectId
from typing import List, Optional
import os
from dotenv import load_dotenv
from ..interfaces.ranking.ranking_service_interface import IRankingService
from ..dtos.ranking_input_dto import RankingInputDTO

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")

# Initialize MongoDB client
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]
simulations_collection = db['simulations']


class RankingService(IRankingService):
    # Implement the required abstract method from IRankingService
    async def ranking_by_metric(self, ranking_input_data: RankingInputDTO):
        metric = ranking_input_data.metric
        pipeline = [
            {"$match": {"metric": metric}},
            {"$project": {"llm": 1, "avg_score": {"$avg": "$data_points"}}},
            {"$sort": {"avg_score": 1}}
        ]

        first_set_numbers = ranking_input_data.first_set_numbers

        results = await simulations_collection.aggregate(pipeline).to_list(length=first_set_numbers)
        # Convert ObjectId to string
        for result in results:
            result["_id"] = str(result["_id"])
        
        return results