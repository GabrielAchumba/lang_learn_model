from abc import ABC, abstractmethod
from ...dtos.simulation_input_dto import SimulationInputDTO
from typing import Optional, List

class ISimulationService(ABC):
    
    @abstractmethod
    async def simulate(self, simulation_input_data : SimulationInputDTO) -> str:
        pass