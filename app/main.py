from typing import Union
from fastapi import FastAPI, Response, status, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from app.config import POSTGRES_DATABASE_URL
from app.database import db_manager

from app.routers import unit_of_measurements
from app.routers import product_type
from app.routers import product

db_manager.init(POSTGRES_DATABASE_URL)

app = FastAPI()

app.include_router(unit_of_measurements.router)
app.include_router(product_type.router)
app.include_router(product.router)