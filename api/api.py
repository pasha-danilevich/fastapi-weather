from fastapi import APIRouter
from .endpoints import weather, user

api_router = APIRouter()

api_router.include_router(weather.router, prefix="/weather")
api_router.include_router(user.router, prefix="/user")