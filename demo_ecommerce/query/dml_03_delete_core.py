# pylint: disable=R0801
from sqlalchemy import insert, delete
from demo_ecommerce.connection.connection import create_session_maker
from demo_ecommerce.connection.connection_base import Connections
from demo_ecommerce.models.models import Customer
from demo_ecommerce.query.query_base import render_query


def query_data(connection_string: str):
    with create_session_maker(connection_string)() as session:
        session.execute(
            insert(Customer).values(id=271828, name="Ettore", address="Via dei Tigli")
        )

        query = delete(Customer).where(Customer.id == 271828)

        print(render_query(session, query))

        session.execute(query)

        # session.commit()
        session.rollback()


if __name__ == "__main__":
    query_data(Connections.MYSQL_LOCAL.value)
