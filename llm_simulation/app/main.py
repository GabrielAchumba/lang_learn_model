from fastapi import FastAPI
from typing import AsyncGenerator
from fastapi.middleware.cors import CORSMiddleware
from .routes.llm_routes import llm_router
from .routes.metric_routes import metric_router
from .routes.simulation_routes import simulation_router
from .services.llm_service import seed_llms
from .services.metric_service import seed_metrics

async def lifespan_context(app: FastAPI) -> AsyncGenerator[None, None]:
    await seed_llms()
    await seed_metrics()
    yield

app = FastAPI(lifespan=lifespan_context)
#app = FastAPI()

# Allow CORS for Vue.js frontend
origins = [
    "http://localhost:9000",  # Vue.js local development server
    "http://localhost:8081",  # Vue.js docker development server
    "https://your-production-domain1.comhh"  # Your production domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Register routes
app.include_router(llm_router)
app.include_router(metric_router)
app.include_router(simulation_router)


@app.get("/")
async def root():
    print("seen")
    return {"message": "LLM Simulator!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)