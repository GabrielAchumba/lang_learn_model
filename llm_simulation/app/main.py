from fastapi import FastAPI
from .routes.llm_routes import llm_router
from .routes.metric_routes import metric_router
from .routes.simulation_routes import simulation_router

app = FastAPI()

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