from fastapi import Depends, HTTPException
from ..interfaces.metric.metric_service_interface import IMetricService
from ..services.metric_service import MetricService
from ..dtos.metric_dto import CreateMetricDTO
from ..models.metric_model import MetricModel
from ..interfaces.metric.metric_controller_interface import IMetricController
from typing import List

# Inject the MetricService using the IMetricService interface
async def get_metric_service() -> IMetricService:
    return MetricService()

# Inject the MetricController with the MetricService as dependency
async def get_metric_controller(service: IMetricService = Depends(get_metric_service)):
    return MetricController(service)

class MetricController(IMetricController):
    def __init__(self, metric_service: IMetricService):
        self.metric_service = metric_service

    async def create_metric_controller(self, metric_data: CreateMetricDTO) -> MetricModel:
        return await self.metric_service.create_metric(metric_data)

    async def get_all_metrics_controller(self) -> List[MetricModel]:
        return await self.metric_service.get_metrics()

    async def get_metric_controller(self, metric_id: str) -> MetricModel:
        metric = await self.metric_service.get_metric(metric_id)
        if not metric:
            raise HTTPException(status_code=404, detail="Metric not found")
        return metric

    async def update_metric_controller(self, metric_id: str, metric_data: CreateMetricDTO) -> MetricModel:
        updated_metric = await self.metric_service.update_metric(metric_id, metric_data)
        if not updated_metric:
            raise HTTPException(status_code=404, detail="Metric not found")
        return updated_metric

    async def delete_metric_controller(self, metric_id: str) -> dict:
        success = await self.metric_service.delete_metric(metric_id)
        if not success:
            raise HTTPException(status_code=404, detail="Metric not found")
        return {"message": "Metric deleted successfully"}