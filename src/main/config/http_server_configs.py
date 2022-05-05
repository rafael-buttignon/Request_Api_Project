from fastapi import FastAPI
from src.main.routes import sharships_routes

app = FastAPI()

app.include_router(sharships_routes)