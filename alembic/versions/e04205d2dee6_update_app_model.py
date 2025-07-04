"""update_app_model

Revision ID: e04205d2dee6
Revises: 12870ffca7c6
Create Date: 2025-06-20 15:03:13.911550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e04205d2dee6'
down_revision = '12870ffca7c6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('apps', sa.Column('environment', sa.String(), nullable=False))
    op.drop_column('apps', 'enviroment')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('apps', sa.Column('enviroment', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('apps', 'environment')
    # ### end Alembic commands ###