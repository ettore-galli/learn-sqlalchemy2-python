from sqlalchemy import select
from demo_ecommerce.connection.connection import create_session_maker
from demo_ecommerce.connection.connection_base import Connections
from demo_ecommerce.models.models import Customer
from demo_ecommerce.query.query_base import render_query


def query_data(connection_string: str):
    with create_session_maker(connection_string)() as session:

        query = select(Customer).where(Customer.name.like("%oni%"))

        print(render_query(session, query))

        for record in session.execute(query.limit(5)):
            print(record[0].name, record[0].address)


if __name__ == "__main__":
    query_data(Connections.MYSQL_TUTORIAL.value)
