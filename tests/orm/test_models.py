from decimal import Decimal
from sqlalchemy import select
from sqlalchemy.orm import Session
from tests.utils.engine import setup_orm_db_engine

from tutorial.orm.models import Customer, Item, PriceList


def test_db_models():
    with Session(setup_orm_db_engine()) as session:
        data = [
            Customer(name="Ettore", address="Via dei Tigli"),
            Item(code="P001", description="Pinza manico rosso"),
            Item(code="L001", description="Lampadina piccola"),
            Item(code="L002", description="Lampadina media"),
            PriceList(item_code="L001", price=Decimal("2.30")),
            PriceList(item_code="L002", price=Decimal("2.50")),
        ]
        for item in data:
            session.add(item)
        session.commit()

        query = select(Customer)
        result = session.execute(query).all()
        assert result[0].Customer.name == "Ettore"

        query = select(Item)
        result = session.execute(query).all()
        assert [item.Item.code for item in result] == ["P001", "L001", "L002"]
        assert [
            item.Item.price_list.price if item.Item.price_list else "<none>"
            for item in result
        ] == ["<none>", Decimal("2.30"), Decimal("2.50")]
