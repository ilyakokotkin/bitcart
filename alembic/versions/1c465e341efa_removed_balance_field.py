"""removed balance field

Revision ID: 1c465e341efa
Revises: a27789cb7b2a
Create Date: 2020-10-09 23:29:44.645464

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "1c465e341efa"
down_revision = "a27789cb7b2a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("wallets", "balance")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("wallets", sa.Column("balance", sa.NUMERIC(precision=16, scale=8), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
