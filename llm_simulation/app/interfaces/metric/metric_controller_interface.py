from abc import ABC, abstractmethod
from ...dtos.metric_dto import CreateMetricDTO
from ...models.metric_model import MetricModel
from typing import List, Optional

class IMetricController(ABC):
    
    @abstractmethod
    async def create_metric_controller(self, metric_data: CreateMetricDTO) -> MetricModel:
        pass

    @abstractmethod
    async def get_all_metrics_controller(self) -> List[MetricModel]:
        pass

    @abstractmethod
    async def get_metric_controller(self, metric_id: str) -> Optional[MetricModel]:
        pass

    @abstractmethod
    async def update_metric_controller(self, metric_id: str, metric_data: CreateMetricDTO) -> Optional[MetricModel]:
        pass

    @abstractmethod
    async def delete_metric_controller(self, metric_id: str) -> dict:
        pass