"""init

Revision ID: 0aea787a081d
Revises: 
Create Date: 2022-08-04 21:07:07.721821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0aea787a081d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('price_in_rub', sa.Float(), nullable=False),
    sa.Column('delivery_time', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    pass
