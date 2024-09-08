from fastapi import Depends
from ..interfaces.ranking.ranking_service_interface import IRankingService
from ..services.llm_ranking_service import RankingService
from ..dtos.ranking_input_dto import RankingInputDTO
from ..interfaces.ranking.ranking_controller_interface import IRankingController

# Inject the RankingService using the IRankingService interface
async def get_rankning_service() -> IRankingService:
    return RankingService()

# Inject the RankingController with the get_rankning_service as dependency
async def get_ranking_controller(service: IRankingService = Depends(get_rankning_service)):
    return RankingController(service)

class RankingController(IRankingController):
    
    def __init__(self, ranking_service: IRankingService):
        self.ranking_service = ranking_service

    async def ranking_by_metric(self, ranking_input_data : RankingInputDTO):
        return await self.ranking_service.ranking_by_metric(ranking_input_data)