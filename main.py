# main.py
from fastapi import FastAPI
from database.connection import init_tortoise
from api.api import api_router
app = FastAPI()
app.include_router(api_router)

init_tortoise(app)