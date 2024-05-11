from fastapi import FastAPI

from app.container import Container

from app.routers import unit_of_measurements
from app.routers import product_type
from app.routers import product
from app.routers import dish_type
from app.routers import dish
from app.routers import composition_of_dish
from app.routers import client
from app.routers import order

class AppCreator:
    def __init__(self):
        # set app default
        self.app = FastAPI()

        # set db and container
        self.container = Container()
        self.db = self.container.db()

        # set routes
        @self.app.get("/")
        def root():
            return "service is working"

        self.app.include_router(unit_of_measurements.router)
        self.app.include_router(product_type.router)
        self.app.include_router(product.router)
        self.app.include_router(dish_type.router)
        self.app.include_router(dish.router)
        self.app.include_router(composition_of_dish.router)
        self.app.include_router(client.router)
        self.app.include_router(order.router)

app_creator = AppCreator()
app = app_creator.app
db = app_creator.db
container = app_creator.container