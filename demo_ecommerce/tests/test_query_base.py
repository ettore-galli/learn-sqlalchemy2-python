from sqlalchemy import select
from sqlalchemy.orm import Session
from demo_ecommerce.models.models import Customer, Invoice, Item
from demo_ecommerce.query.query_base import result_as_dict
from demo_ecommerce.tests.utils.engine import setup_orm_db_engine


def test_result_as_dict():
    with Session(setup_orm_db_engine()) as session:
        data = [
            Customer(name="Ettore", address="Via dei Tigli"),
            Item(code="P001", description="Pinza manico rosso"),
            Item(code="L001", description="Lampadina piccola"),
            Item(code="L002", description="Lampadina media"),
            Invoice(customer_id=1),
        ]
        for item in data:
            session.add(item)
        session.commit()

        query = select(Customer, Invoice, Invoice.id.label("duplicated_id"))

        records = list(session.execute(query).all())

        assert (result_as_dict(records[0])) == {
            "address": "Via dei Tigli",
            "customer_id": 1,
            "duplicated_id": 1,
            "id": 1,
            "name": "Ettore",
        }
