from fastapi import FastAPI
from app.api.v1 import health

app = FastAPI()

app.include_router(health.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Atlas backend is running"}
