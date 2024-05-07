from demo_ecommerce.connection.connection import create_session_maker
from demo_ecommerce.connection.connection_base import Connections
from demo_ecommerce.models.models import Customer
from demo_ecommerce.query.query_base import render_query


def query_data(connection_string: str):
    with create_session_maker(connection_string)() as session:

        # Elenco clienti

        # SELECT customer.id, customer.name, customer.address
        # FROM customer
        # WHERE customer.name LIKE '%%oni%%'
        query = session.query(Customer).filter(Customer.name.like("%oni%"))

        print(render_query(session, query))

        for record in query.limit(5).all():
            print(record.name, record.address)


if __name__ == "__main__":
    query_data(Connections.MYSQL_LOCAL.value)
