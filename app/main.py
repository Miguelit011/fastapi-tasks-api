from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import tasks

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Tasks API",
    description="API de gestión de tareas",
    version="1.0.0"
)

app.include_router(tasks.router)