from sqlalchemy import select
from sqlalchemy.orm import Session
from tests.utils.engine import setup_orm_db_engine

from tutorial.orm.models import Customer


def test_db_models():
    with Session(setup_orm_db_engine()) as session:
        session.add(Customer(name="Ettore", address="Via dei Tigli"))
        session.commit()
        query = select(Customer)
        result = session.execute(query).all()
        assert result[0].Customer.name == "Ettore"
