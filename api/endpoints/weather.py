from fastapi import APIRouter

router = APIRouter()


@router.post('/')
def get_weather(city: str, country: str) -> dict:
    return {'city': city, 'country': country}