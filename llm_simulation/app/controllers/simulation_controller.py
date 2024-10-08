from fastapi import Depends
from ..interfaces.simulation.simulation_service_interface import ISimulationService
from ..services.simulation_service import SimulationService, get_dependecy_services
from ..dtos.simulation_input_dto import SimulationInputDTO
from ..interfaces.simulation.simulation_controller_interface import ISimulationController

# Inject the SimulationService using the ISimulationService interface
async def get_simulation_service(
    service: ISimulationService = Depends(get_dependecy_services)
) -> ISimulationService:
    return service

# Inject the SimulationController with the get_simulation_service as dependency
async def get_simulation_controller(service: ISimulationService = Depends(get_simulation_service)):
    return SimulationController(service)


class SimulationController(ISimulationController):
    def __init__(self, simulation_service: ISimulationService):
        self.simulation_service = simulation_service

    async def simulate_controller(self, simulation_input_data: SimulationInputDTO) -> str:
        return await self.simulation_service.simulate(simulation_input_data)