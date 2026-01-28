from fastapi import FastAPI
from app.api.v1 import health, ping, item, users
from app.db.session import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(health.router, prefix="/api/v1")
app.include_router(ping.router, prefix="/api/v1")
app.include_router(item.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Atlas backend is running"}
