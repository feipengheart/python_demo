from fastapi import FastAPI
from app.api.v1 import router as v1_router

app = FastAPI(
    title="Python API Demo",
    description="Standardized API Demo Framework",
    version="0.1.0",
    openapi_url="/api/v1/openapi.json"
)

app.include_router(v1_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=15080)