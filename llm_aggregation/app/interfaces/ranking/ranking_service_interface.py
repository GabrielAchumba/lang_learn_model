from abc import ABC, abstractmethod
from ...dtos.ranking_input_dto import RankingInputDTO
from typing import Optional, List

class IRankingService(ABC):
    
    @abstractmethod
    async def ranking_by_metric(self, ranking_input_data : RankingInputDTO):
        pass