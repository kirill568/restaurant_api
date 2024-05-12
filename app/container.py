from dependency_injector import containers, providers

from app.config import POSTGRES_DATABASE_URL
from app.database import DatabaseSessionManager
from app.repository import *
from app.services import *

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=[
            "app.routers",
            "app.dependencies",
        ]
    )

    db = providers.Singleton(DatabaseSessionManager, db_url=POSTGRES_DATABASE_URL)

    bill_repository = providers.Factory(BillRepository, session=db.provided.session)
    client_repository = providers.Factory(ClientRepository, session=db.provided.session)
    composition_of_dish_repository = providers.Factory(CompositionOfDishRepository, session=db.provided.session)
    dish_repository = providers.Factory(DishRepository, session=db.provided.session)
    order_repository = providers.Factory(OrderRepository, session=db.provided.session)
    product_repository = providers.Factory(ProductRepository, session=db.provided.session)
    type_of_dish_repository = providers.Factory(TypeOfDishRepository, session=db.provided.session)
    type_of_product_repository = providers.Factory(TypeOfProductRepository, session=db.provided.session)
    unit_of_measurement_repository = providers.Factory(UnitOfMeasurementRepository, session=db.provided.session)

    composition_of_dish_service = providers.Factory(CompositionOfDishService, composition_of_dish_repository = composition_of_dish_repository, product_repository = product_repository, unit_of_measurement_repository = unit_of_measurement_repository)
    dish_service = providers.Factory(DishService, dish_repository = dish_repository, type_of_dish_repository = type_of_dish_repository)
    product_service = providers.Factory(ProductService, product_repository = product_repository, type_of_product_repository = type_of_product_repository)
    order_service = providers.Factory(OrderService, order_repository = order_repository, bill_repository = bill_repository, client_repository = client_repository, dish_repository = dish_repository)