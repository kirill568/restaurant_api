"""init

Revision ID: 4f77ec297c1d
Revises: 
Create Date: 2024-04-16 20:48:23.196421

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f77ec297c1d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('patronymic', sa.String(length=30), nullable=False),
    sa.Column('phone_number', sa.String(length=20), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_client_first_name'), 'client', ['first_name'], unique=False)
    op.create_index(op.f('ix_client_id'), 'client', ['id'], unique=False)
    op.create_index(op.f('ix_client_last_name'), 'client', ['last_name'], unique=False)
    op.create_index(op.f('ix_client_patronymic'), 'client', ['patronymic'], unique=False)
    op.create_index(op.f('ix_client_phone_number'), 'client', ['phone_number'], unique=False)
    op.create_table('type_of_dish',
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_type_of_dish_id'), 'type_of_dish', ['id'], unique=False)
    op.create_index(op.f('ix_type_of_dish_name'), 'type_of_dish', ['name'], unique=False)
    op.create_table('type_of_product',
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_type_of_product_id'), 'type_of_product', ['id'], unique=False)
    op.create_index(op.f('ix_type_of_product_name'), 'type_of_product', ['name'], unique=False)
    op.create_table('unit_of_measurement',
    sa.Column('name_unit_of_measurement', sa.String(length=100), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_unit_of_measurement_id'), 'unit_of_measurement', ['id'], unique=False)
    op.create_index(op.f('ix_unit_of_measurement_name_unit_of_measurement'), 'unit_of_measurement', ['name_unit_of_measurement'], unique=False)
    op.create_table('dish',
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('calories', sa.Float(), nullable=False),
    sa.Column('cooking_time', sa.Time(), nullable=False),
    sa.Column('type_of_dish_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['type_of_dish_id'], ['type_of_product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dish_calories'), 'dish', ['calories'], unique=False)
    op.create_index(op.f('ix_dish_cooking_time'), 'dish', ['cooking_time'], unique=False)
    op.create_index(op.f('ix_dish_cost'), 'dish', ['cost'], unique=False)
    op.create_index(op.f('ix_dish_id'), 'dish', ['id'], unique=False)
    op.create_index(op.f('ix_dish_name'), 'dish', ['name'], unique=False)
    op.create_index(op.f('ix_dish_weight'), 'dish', ['weight'], unique=False)
    op.create_table('order',
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_date'), 'order', ['date'], unique=False)
    op.create_index(op.f('ix_order_id'), 'order', ['id'], unique=False)
    op.create_table('product',
    sa.Column('name_of_product', sa.String(length=30), nullable=False),
    sa.Column('type_of_product_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['type_of_product_id'], ['type_of_product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_id'), 'product', ['id'], unique=False)
    op.create_index(op.f('ix_product_name_of_product'), 'product', ['name_of_product'], unique=False)
    op.create_table('bill',
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('dish_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['dish_id'], ['dish.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bill_id'), 'bill', ['id'], unique=False)
    op.create_table('composition_of_dish',
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('dish_id', sa.Integer(), nullable=True),
    sa.Column('number_of_products', sa.Float(), nullable=False),
    sa.Column('unit_of_measurement_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['dish_id'], ['dish.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['unit_of_measurement_id'], ['unit_of_measurement.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_composition_of_dish_id'), 'composition_of_dish', ['id'], unique=False)
    op.create_index(op.f('ix_composition_of_dish_number_of_products'), 'composition_of_dish', ['number_of_products'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_composition_of_dish_number_of_products'), table_name='composition_of_dish')
    op.drop_index(op.f('ix_composition_of_dish_id'), table_name='composition_of_dish')
    op.drop_table('composition_of_dish')
    op.drop_index(op.f('ix_bill_id'), table_name='bill')
    op.drop_table('bill')
    op.drop_index(op.f('ix_product_name_of_product'), table_name='product')
    op.drop_index(op.f('ix_product_id'), table_name='product')
    op.drop_table('product')
    op.drop_index(op.f('ix_order_id'), table_name='order')
    op.drop_index(op.f('ix_order_date'), table_name='order')
    op.drop_table('order')
    op.drop_index(op.f('ix_dish_weight'), table_name='dish')
    op.drop_index(op.f('ix_dish_name'), table_name='dish')
    op.drop_index(op.f('ix_dish_id'), table_name='dish')
    op.drop_index(op.f('ix_dish_cost'), table_name='dish')
    op.drop_index(op.f('ix_dish_cooking_time'), table_name='dish')
    op.drop_index(op.f('ix_dish_calories'), table_name='dish')
    op.drop_table('dish')
    op.drop_index(op.f('ix_unit_of_measurement_name_unit_of_measurement'), table_name='unit_of_measurement')
    op.drop_index(op.f('ix_unit_of_measurement_id'), table_name='unit_of_measurement')
    op.drop_table('unit_of_measurement')
    op.drop_index(op.f('ix_type_of_product_name'), table_name='type_of_product')
    op.drop_index(op.f('ix_type_of_product_id'), table_name='type_of_product')
    op.drop_table('type_of_product')
    op.drop_index(op.f('ix_type_of_dish_name'), table_name='type_of_dish')
    op.drop_index(op.f('ix_type_of_dish_id'), table_name='type_of_dish')
    op.drop_table('type_of_dish')
    op.drop_index(op.f('ix_client_phone_number'), table_name='client')
    op.drop_index(op.f('ix_client_patronymic'), table_name='client')
    op.drop_index(op.f('ix_client_last_name'), table_name='client')
    op.drop_index(op.f('ix_client_id'), table_name='client')
    op.drop_index(op.f('ix_client_first_name'), table_name='client')
    op.drop_table('client')
    # ### end Alembic commands ###