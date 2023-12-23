"""Add unique id

Revision ID: dfc8cd8487fd
Revises: 927a773be59d
Create Date: 2021-05-13 17:41:52.402473

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "dfc8cd8487fd"
down_revision = "927a773be59d"
branch_labels = None
depends_on = None


def create_constraints():
    op.create_foreign_key(None, "discountsxproducts", "discounts", ["discount_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "discountsxproducts", "products", ["product_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "discounts", "users", ["user_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "paymentmethods", "invoices", ["invoice_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "productsxinvoices", "invoices", ["invoice_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "invoices", "stores", ["store_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "invoices", "users", ["user_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "notificationsxstores", "notifications", ["notification_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "notifications", "users", ["user_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "notificationsxstores", "stores", ["store_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "productsxinvoices", "products", ["product_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "products", "stores", ["store_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "products", "users", ["user_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "walletsxstores", "stores", ["store_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "stores", "users", ["user_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "templates", "users", ["user_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "wallets", "users", ["user_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "tokens", "users", ["user_id"], ["id"], ondelete="SET NULL")
    op.create_foreign_key(None, "walletsxstores", "wallets", ["wallet_id"], ["id"], ondelete="SET NULL")


def drop_constraints():
    op.drop_constraint("discountsxproducts_discount_id_discounts_fkey", "discountsxproducts")
    op.drop_constraint("discountsxproducts_product_id_products_fkey", "discountsxproducts")
    op.drop_constraint("discounts_user_id_users_fkey", "discounts")
    op.drop_constraint("paymentmethods_invoice_id_invoices_fkey", "paymentmethods")
    op.drop_constraint("productsxinvoices_invoice_id_invoices_fkey", "productsxinvoices")
    op.drop_constraint("invoices_store_id_stores_fkey", "invoices")
    op.drop_constraint("invoices_user_id_users_fkey", "invoices")
    op.drop_constraint("notificationsxstores_notification_id_notifications_fkey", "notificationsxstores")
    op.drop_constraint("notifications_user_id_users_fkey", "notifications")
    op.drop_constraint("notificationsxstores_store_id_stores_fkey", "notificationsxstores")
    op.drop_constraint("productsxinvoices_product_id_products_fkey", "productsxinvoices")
    op.drop_constraint("products_store_id_stores_fkey", "products")
    op.drop_constraint("products_user_id_users_fkey", "products")
    op.drop_constraint("walletsxstores_store_id_stores_fkey", "walletsxstores")
    op.drop_constraint("stores_user_id_users_fkey", "stores")
    op.drop_constraint("templates_user_id_users_fkey", "templates")
    op.drop_constraint("wallets_user_id_users_fkey", "wallets")
    op.drop_constraint("tokens_user_id_users_fkey", "tokens")
    op.drop_constraint("walletsxstores_wallet_id_wallets_fkey", "walletsxstores")


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    drop_constraints()
    op.alter_column("discounts", "id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=False)
    op.alter_column("discounts", "user_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    op.alter_column("discountsxproducts", "discount_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    op.alter_column("discountsxproducts", "product_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    op.alter_column(
        "invoices",
        "id",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
        existing_server_default=sa.text("nextval('invoices_id_seq'::regclass)"),
    )
    op.alter_column("invoices", "store_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    op.alter_column("invoices", "user_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    op.alter_column(
        "notifications",
        "id",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
        existing_server_default=sa.text("nextval('notifications_id_seq'::regclass)"),
    )
    op.alter_column("notifications", "user_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    op.alter_column(
        "notificationsxstores", "notification_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True
    )
    op.alter_column("notificationsxstores", "store_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    op.alter_column(
        "paymentmethods",
        "id",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
        existing_server_default=sa.text("nextval('paymentmethods_id_seq'::regclass)"),
    )
    op.alter_column("paymentmethods", "invoice_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    op.alter_column(
        "products",
        "id",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
        existing_server_default=sa.text("nextval('products_id_seq'::regclass)"),
    )
    op.alter_column("products", "store_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    op.alter_column("products", "user_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    op.alter_column("productsxinvoices", "invoice_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    op.alter_column("productsxinvoices", "product_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    op.alter_column("settings", "id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=False)
    op.alter_column(
        "stores",
        "id",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
        existing_server_default=sa.text("nextval('stores_id_seq'::regclass)"),
    )
    op.alter_column("stores", "user_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    op.alter_column("templates", "id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=False)
    op.alter_column("templates", "user_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    op.create_index(op.f("tokens_id_idx"), "tokens", ["id"], unique=False)
    op.alter_column(
        "users",
        "id",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
        existing_server_default=sa.text("nextval('users_id_seq'::regclass)"),
    )
    op.alter_column(
        "wallets",
        "id",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
        existing_server_default=sa.text("nextval('wallets_id_seq'::regclass)"),
    )
    op.alter_column("wallets", "user_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    op.alter_column("walletsxstores", "store_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    op.alter_column("walletsxstores", "wallet_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    op.alter_column("tokens", "user_id", existing_type=sa.INTEGER(), type_=sa.String(), existing_nullable=True)
    # Add deleted foreign keys
    create_constraints()
    # ### end Alembic commands ###


def int_alter_column(table, column, **kwargs):
    op.alter_column(table, column, postgresql_using=f"{column}::integer", **kwargs)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    drop_constraints()
    int_alter_column("walletsxstores", "wallet_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True)
    int_alter_column("walletsxstores", "store_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True)
    int_alter_column("wallets", "user_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True)
    int_alter_column(
        "wallets",
        "id",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=False,
        existing_server_default=sa.text("nextval('wallets_id_seq'::regclass)"),
    )
    int_alter_column(
        "users",
        "id",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=False,
        existing_server_default=sa.text("nextval('users_id_seq'::regclass)"),
    )
    op.drop_index(op.f("tokens_id_idx"), table_name="tokens")
    int_alter_column("templates", "user_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True)
    int_alter_column("templates", "id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=False)
    int_alter_column("stores", "user_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True)
    int_alter_column(
        "stores",
        "id",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=False,
        existing_server_default=sa.text("nextval('stores_id_seq'::regclass)"),
    )
    int_alter_column("settings", "id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=False)
    int_alter_column("productsxinvoices", "product_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True)
    int_alter_column("productsxinvoices", "invoice_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True)
    int_alter_column("products", "user_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True)
    int_alter_column("products", "store_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True)
    int_alter_column(
        "products",
        "id",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=False,
        existing_server_default=sa.text("nextval('products_id_seq'::regclass)"),
    )
    int_alter_column("paymentmethods", "invoice_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True)
    int_alter_column(
        "paymentmethods",
        "id",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=False,
        existing_server_default=sa.text("nextval('paymentmethods_id_seq'::regclass)"),
    )
    int_alter_column("notificationsxstores", "store_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True)
    int_alter_column(
        "notificationsxstores", "notification_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True
    )
    int_alter_column("notifications", "user_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True)
    int_alter_column(
        "notifications",
        "id",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=False,
        existing_server_default=sa.text("nextval('notifications_id_seq'::regclass)"),
    )
    int_alter_column("invoices", "user_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True)
    int_alter_column("invoices", "store_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True)
    int_alter_column(
        "invoices",
        "id",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=False,
        existing_server_default=sa.text("nextval('invoices_id_seq'::regclass)"),
    )
    int_alter_column("discountsxproducts", "product_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True)
    int_alter_column(
        "discountsxproducts", "discount_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True
    )
    int_alter_column("discounts", "user_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True)
    int_alter_column("discounts", "id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=False)
    int_alter_column("tokens", "user_id", existing_type=sa.String(), type_=sa.INTEGER(), existing_nullable=True)
    create_constraints()
    # ### end Alembic commands ###
