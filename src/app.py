from fastapi import FastAPI
from config import settings
from services.database import sessionmanager
from api.client import router as client_router

from fastapi.middleware.cors import CORSMiddleware

sessionmanager.init(settings.DB_CONFIG)

app = FastAPI(title="Restaurant Table Reservation Server")

app.include_router(client_router, prefix="/api")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

