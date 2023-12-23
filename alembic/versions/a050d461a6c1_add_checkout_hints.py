"""Add checkout hints

Revision ID: a050d461a6c1
Revises: 850bd53dff02
Create Date: 2022-05-04 18:07:13.685274

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "a050d461a6c1"
down_revision = "850bd53dff02"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("paymentmethods", sa.Column("hint", sa.Text(), nullable=True))
    op.add_column("wallets", sa.Column("hint", sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("wallets", "hint")
    op.drop_column("paymentmethods", "hint")
    # ### end Alembic commands ###
