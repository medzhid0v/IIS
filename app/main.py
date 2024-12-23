from fastapi import FastAPI
from app.routers import rt

app = FastAPI(
    title="Library API",
    description="API для управления библиотекой",
    version='1.0.0'
)

app.include_router(rt)