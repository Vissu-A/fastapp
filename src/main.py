from fastapi import FastAPI
from src.api.v1 import userapi as uapi1
from src.api.v2 import userapi as uapi2
from src.models import user
from src.db.database import db_engine

app = FastAPI()

# app.include_router(uapi1.router)
app.include_router(uapi2.router)

