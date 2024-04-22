from typing import Union
from fastapi import FastAPI, Response, status, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from app.config import POSTGRES_DATABASE_URL
from app.database import db_manager
from app.routers import unit_of_measurements

db_manager.init(POSTGRES_DATABASE_URL)

app = FastAPI()

app.include_router(unit_of_measurements.router)