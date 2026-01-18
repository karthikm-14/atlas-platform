from fastapi import APIRouter
from app.schemas.ping import PingRequest, PingResponse

router = APIRouter()

@router.post("/ping", response_model=PingResponse)
def ping(data: PingRequest):
    return PingResponse(
        reply=f"{data.message} from atlas"
    )