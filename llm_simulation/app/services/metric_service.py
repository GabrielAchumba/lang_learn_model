import motor.motor_asyncio
from bson import ObjectId
from ..models.metric_model import MetricModel
from ..dtos.metric_dto import CreateMetricDTO
from typing import List, Optional
import os
from dotenv import load_dotenv
from ..interfaces.metric.metric_service_interface import IMetricService

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")

# Initialize MongoDB client
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]
metrics_collection = db['metrics']


class MetricService(IMetricService):
    async def create_metric(self, metric_data: CreateMetricDTO) -> MetricModel:
        new_metric_data = metric_data.dict()
        result = await metrics_collection.insert_one(new_metric_data)
        created_metric = await metrics_collection.find_one({"_id": result.inserted_id})
        return MetricModel(**created_metric)

    async def get_metrics(self) -> List[MetricModel]:
        metrics = []
        async for metric in metrics_collection.find():
            metrics.append(MetricModel(**metric))
        return metrics

    async def get_metric(self, metric_id: str) -> Optional[MetricModel]:
        metric = await metrics_collection.find_one({"_id": ObjectId(metric_id)})
        if metric:
            return MetricModel(**metric)
        return None

    async def update_metric(self, metric_id: str, metric_data: CreateMetricDTO) -> Optional[MetricModel]:
        update_data = {k: v for k, v in metric_data.dict().items() if v is not None}
        await metrics_collection.update_one({"_id": ObjectId(metric_id)}, {"$set": update_data})
        update_metric = await metrics_collection.find_one({"_id": ObjectId(metric_id)})
        if update_metric:
            return MetricModel(**update_metric)
        return None

    async def delete_metric(self, metric_id: str) -> bool:
        result = await metrics_collection.delete_one({"_id": ObjectId(metric_id)})
        return result.deleted_count > 0