from abc import ABC, abstractmethod
from ...dtos.metric_dto import CreateMetricDTO
from ...models.metric_model import MetricModel
from typing import Optional, List

class IMetricService(ABC):
    
    @abstractmethod
    async def create_metric(self, metric_data : CreateMetricDTO) -> MetricModel:
        pass

    @abstractmethod
    async def get_metrics(self) -> List[MetricModel]:
        pass

    @abstractmethod
    async def get_metric(self, metric_id: str) -> Optional[MetricModel]:
        pass

    @abstractmethod
    async def update_metric(self, metric_id: str, metric_data: CreateMetricDTO) -> Optional[MetricModel]:
        pass

    @abstractmethod
    async def delete_metric(self, metric_id: str) -> bool:
        pass