from fastapi import APIRouter, Depends
from ..controllers.ranking_controller import RankingController, get_ranking_controller
from ..dtos.ranking_input_dto import RankingInputDTO

# Create an APIRouter instance
rankings_router = APIRouter()


@rankings_router.post("/rankings")
async def ranking_by_metric(ranking_input_data: RankingInputDTO, controller: RankingController = Depends(get_ranking_controller)):
    return await controller.ranking_by_metric(ranking_input_data)