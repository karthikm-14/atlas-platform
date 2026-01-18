from pydantic import BaseModel


class PingRequest(BaseModel):
    message: str

class PingResponse(BaseModel):
    reply: str
    
