"""
This module handles authentication-related API endpoints.
- It initializes a FastAPI APIRouter for grouping auth routes.
- The '/signup' endpoint processes new user registration using the UserCreate schema.
- The '/login' endpoint is defined to handle user authentication (currently implemented with a placeholder service call).
- It leverages a service layer (create_user) to abstract business logic from the route handlers.

"""
from fastapi import APIRouter
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import create_user

router = APIRouter()

@router.post("/signup", response_model=UserOut)
def signup(user: UserCreate):
    return create_user(user)

@router.post("/login", response_model=UserOut)
def login(user: UserCreate):
    return create_user(user)


