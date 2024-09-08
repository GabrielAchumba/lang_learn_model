from fastapi import APIRouter, Depends
from ..controllers.metric_controller import MetricController, get_metric_controller
from ..dtos.metric_dto import CreateMetricDTO

# Create an APIRouter instance
metric_router = APIRouter()


@metric_router.post("/metrics")
async def create_metric(metric_data: CreateMetricDTO, controller: MetricController = Depends(get_metric_controller)):
    return await controller.create_metric_controller(metric_data)


@metric_router.get("/metrics")
async def get_all_metrics(controller: MetricController = Depends(get_metric_controller)):
    print("seen")
    return await controller.get_all_metrics_controller()


@metric_router.get("/metrics/{metric_id}")
async def get_llm(metric_id: str, controller: MetricController = Depends(get_metric_controller)):
    return await controller.get_metric_controller(metric_id)


@metric_router.put("/metrics/{metric_id}")
async def update_llm(metric_id: str, metric_data: CreateMetricDTO, controller: MetricController = Depends(get_metric_controller)):
    return await controller.update_metric_controller(metric_id, metric_data)


@metric_router.delete("/metrics/{metric_id}")
async def delete_llm(metric_id: str, controller: MetricController = Depends(get_metric_controller)):
    return await controller.delete_metric_controller(metric_id)