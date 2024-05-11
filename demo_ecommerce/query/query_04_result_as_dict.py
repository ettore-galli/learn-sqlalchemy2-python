from sqlalchemy import select
from demo_ecommerce.connection.connection import create_session_maker
from demo_ecommerce.connection.connection_base import Connections
from demo_ecommerce.models.models import Customer
from demo_ecommerce.query.query_base import render_query


# list(inspect(record.Customer).mapper.columns)
def query_data(connection_string: str):
    with create_session_maker(connection_string)() as session:

        # pylint: disable=not-callable
        query = select(Customer)

        print(render_query(session, query))

        for record in session.execute(query):
            print(record)


if __name__ == "__main__":
    query_data(Connections.MYSQL_LOCAL.value)
