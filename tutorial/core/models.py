from sqlalchemy import Column, Integer, Numeric, String, MetaData

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
    Column("id", Integer, primary_key=True),
    Column("description", String(50), nullable=False),
)

item = Table(
    "price",
    db_metadata,
    Column("item_id", Integer, primary_key=True),
    Column(
        "price",
        Numeric(30, 9, asdecimal=True),
        nullable=False,
    ),
)
