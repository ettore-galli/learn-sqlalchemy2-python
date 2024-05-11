from sqlalchemy import select
from demo_ecommerce.connection.connection import create_session_maker
from demo_ecommerce.connection.connection_base import Connections
from demo_ecommerce.models.models import Customer
from demo_ecommerce.query.query_base import render_query


def query_data(connection_string: str):
    with create_session_maker(connection_string)() as session:

        # pylint: disable=not-callable
        query = select(Customer, Customer.id.label("duplicated_id")).offset(5).limit(3)

        print(render_query(session, query))

        for record in session.execute(query):
            print(dict(record.Customer.__dict__))


if __name__ == "__main__":
    query_data(Connections.MYSQL_LOCAL.value)
