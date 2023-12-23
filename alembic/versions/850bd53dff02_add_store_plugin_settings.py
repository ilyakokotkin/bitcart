"""Add store plugin settings

Revision ID: 850bd53dff02
Revises: 58f6fcd5af80
Create Date: 2022-05-01 15:11:56.127624

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "850bd53dff02"
down_revision = "58f6fcd5af80"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("stores", sa.Column("plugin_settings", sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("stores", "plugin_settings")
    # ### end Alembic commands ###
