"""TelegramNotificationModel

Revision ID: ea77b10ba69a
Revises: 0aea787a081d
Create Date: 2022-08-04 23:01:29.726295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea77b10ba69a'
down_revision = '0aea787a081d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Notification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(), nullable=False),
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    pass
