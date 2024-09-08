from fastapi import APIRouter, Depends
from ..controllers.simulation_controller import SimulationController, get_simulation_controller
from ..dtos.metric_dto import CreateMetricDTO

# Create an APIRouter instance
metric_router = APIRouter()


@metric_router.post("/simulations")
async def simulate(simulation_input_data: CreateMetricDTO, controller: SimulationController = Depends(get_simulation_controller)):
    return await controller.simulate_controller(simulation_input_data)