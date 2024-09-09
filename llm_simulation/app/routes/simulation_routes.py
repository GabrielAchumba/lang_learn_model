from fastapi import APIRouter, Depends
from ..controllers.simulation_controller import SimulationController, get_simulation_controller
from ..dtos.simulation_input_dto import SimulationInputDTO

# Create an APIRouter instance
simulation_router = APIRouter()

@simulation_router.post("/simulations")
async def simulate(simulation_input_data: SimulationInputDTO, controller: SimulationController = Depends(get_simulation_controller)):
    print("simulations")
    return await controller.simulate_controller(simulation_input_data)