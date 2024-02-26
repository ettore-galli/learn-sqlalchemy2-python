from sqlalchemy import (
    CheckConstraint,
    Column,
    ForeignKey,
    Integer,
    Numeric,
    PrimaryKeyConstraint,
    String,
    MetaData,
)

from sqlalchemy import Table

db_metadata = MetaData()

customer = Table(
    "customer",
    db_metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("address", String(100), nullable=True),
)

item = Table(
    "item",
    db_metadata,
    Column("id", Integer),
    Column("description", String(50), nullable=False),
    PrimaryKeyConstraint("id"),
)


price_list = Table(
    "price_list",
    db_metadata,
    Column("item_id", ForeignKey(item.c.id), nullable=False),
    Column(
        "price",
        Numeric(30, 9, asdecimal=True),
        nullable=False,
    ),
)
CheckConstraint(
    price_list.c.price > 0,
    name="check_price",
    table=price_list,
)
