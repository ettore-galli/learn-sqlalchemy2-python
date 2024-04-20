from __future__ import annotations

from decimal import Decimal
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from sqlalchemy import ForeignKey, Integer, Numeric, String


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
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String(30), index=True)
    description: Mapped[str] = mapped_column(String(50), nullable=False)
    price_list: Mapped[PriceList] = relationship(back_populates="item")


class PriceList(BaseModel):
    __tablename__ = "price_list"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    item_code: Mapped[int] = mapped_column(ForeignKey(Item.code))
    item: Mapped[Item] = relationship(back_populates="price_list")
    price: Mapped[Decimal] = mapped_column(Numeric(30, 9), nullable=False)


class Invoice(BaseModel):
    __tablename__ = "invoice"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey(Customer.id))
    # customer: Mapped[Customer] = relationship(back_populates="invoice")

class InvoiceDetail(BaseModel):
    __tablename__ = "invoice_detail"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    invoice_id: Mapped[int] = mapped_column(ForeignKey(Invoice.id))
    item_code: Mapped[int] = mapped_column(ForeignKey(Item.code))
    item: Mapped[Item] = relationship()
    quantity: Mapped[Decimal] = mapped_column(Numeric(30, 9), nullable=False)
    unit_price: Mapped[Decimal] = mapped_column(Numeric(30, 9), nullable=False)
