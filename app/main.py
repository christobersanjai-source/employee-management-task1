from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.config import settings
from app.db.database import init_db
from app.routes.health import router as health_router
from app.routes.employees import router as employees_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title=settings.app_name, description="REST API for employee records", version="1.0.0", lifespan=lifespan)
app.include_router(health_router)
app.include_router(employees_router)
