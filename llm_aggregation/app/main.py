from fastapi import FastAPI
from .routes.ranking_routes import rankings_router

app = FastAPI()

# Register routes
app.include_router(rankings_router)

@app.get("/")
async def root():
    print("seen")
    return {"message": "LLM Aggregator!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)