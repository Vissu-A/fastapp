from fastapi import FastAPI
from src.api.v1 import userapi

app = FastAPI()

app.include_router(userapi.router)
