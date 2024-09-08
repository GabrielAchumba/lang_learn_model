import random
import motor.motor_asyncio
from fastapi import Depends
from bson import ObjectId
from ..models.metric_model import MetricModel
from ..dtos.simulation_input_dto import SimulationInputDTO
from typing import List, Optional
import os
from dotenv import load_dotenv
from ..interfaces.simulation.simulation_service_interface import ISimulationService
from ..interfaces.metric.metric_service_interface import IMetricService
from ..services.metric_service import MetricService
from ..services.llm_service import LLMService
from ..interfaces.llm.llm_service_interface import ILLMService
from ..services.simulation_service import SimulationResultModel

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")

# Initialize MongoDB client
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]
simulations_collection = db['simulations']

# Inject the MetricService using the IMetricService interface
async def get_metric_service() -> IMetricService:
    return MetricService()

# Inject the LLMService using the ILLMService interface
async def get_llm_service() -> ILLMService:
    return LLMService()

# Inject the MetricController with the MetricService as dependency
async def get_dependecy_services(metric_service: IMetricService = Depends(get_metric_service),
                                 llm_service: ILLMService = Depends(get_llm_service)):
    return SimulationService(metric_service, llm_service)


class SimulationService(ISimulationService):

    def __init__(self, metric_service: IMetricService, llm_service: ILLMService):
        self.metric_service = metric_service
        self.llm_service = llm_service


    async def simulate(self,  simulation_input_data : SimulationInputDTO) -> str:

        llms = self.llm_service.get_llms()
        if not llms:
            return "LLMs is an empty list"

        metrics = self.metric_service.get_metrics()
        if not metrics:
            return "Metrics is an empty list"
        
        
        try:
            data_points = simulation_input_data.data_points
            start_number = simulation_input_data.start_number
            end_number = simulation_input_data.end_number

            for llm in llms:
                for metric in metrics:
                    data_points = [random.uniform(start_number, end_number) for _ in range(data_points)]
                    new_simulation_input_data = {
                        "llm": llm,
                        "metric": metric,
                        "data_points": data_points
                    }
                    result = await simulations_collection.insert_one(new_simulation_input_data)
                    result_id = result.inserted_id
                    return  f"LLM simulation completed and stored successfully. Simulation result id = {result_id}"
        except ValueError:
             return "An error occured"