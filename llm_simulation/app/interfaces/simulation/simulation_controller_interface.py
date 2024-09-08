from abc import ABC, abstractmethod
from ...dtos.simulation_input_dto import SimulationInputDTO

class ISimulationController(ABC):
    
    @abstractmethod
    async def simulate_controller(self, simulation_input_data : SimulationInputDTO) -> str:
        pass