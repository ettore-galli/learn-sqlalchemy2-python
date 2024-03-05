from decimal import Decimal
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from sqlalchemy import Integer, Numeric, String


class BaseModel(DeclarativeBase):
    pass


db_orm_metadata = BaseModel.metadata


class Customer(BaseModel):
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    address: Mapped[str] = mapped_column(String(200), nullable=True)


class Item(BaseModel):
    __tablename__ = "item"

    code: Mapped[str] = mapped_column(String(30), primary_key=True)
    description: Mapped[str] = mapped_column(String(50), nullable=False)


class PriceList(BaseModel):
    __tablename__ = "price_list"

    item_code: Mapped[str] = mapped_column(String(30), primary_key=True)
    price: Mapped[Decimal] = mapped_column(Numeric(30, 9), nullable=False)
