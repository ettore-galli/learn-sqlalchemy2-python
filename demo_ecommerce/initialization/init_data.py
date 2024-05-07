from decimal import Decimal
import sys

from sqlalchemy import insert

from demo_ecommerce.connection.connection import create_session_maker
from demo_ecommerce.models.models import Customer, Item, PriceList


def init_data(connection_string: str):
    with create_session_maker(connection_string)() as session:
        statements = [
            insert(Customer).values(name="Engineering", address="Via Ugo bassi 2"),
            insert(Customer).values(name="Spago", address="Via Ugo bassi 3"),
            insert(Item).values(code="I001", description="Penna nera"),
            insert(Item).values(code="I002", description="Detersivo per piatti"),
            insert(Item).values(code="I003", description="Pile stilo AAA"),
            insert(Item).values(
                code="I004", description="Acqua minerale naturale 1.5 L"
            ),
            insert(PriceList).values(item_code="I001", price=Decimal("3.14")),
            insert(PriceList).values(item_code="I002", price=Decimal("2.71")),
            insert(PriceList).values(item_code="I003", price=Decimal("9.81")),
            insert(PriceList).values(item_code="I004", price=Decimal("1.61")),
        ]

        for statement in statements:
            session.execute(statement)

        session.commit()


if __name__ == "__main__":
    init_data(sys.argv[1])
