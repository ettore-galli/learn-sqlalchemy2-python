# pylint: disable=duplicate-code

from sqlalchemy import select
from demo_ecommerce.connection.connection import create_session_maker
from demo_ecommerce.connection.connection_base import Connections
from demo_ecommerce.models.models import Customer, Invoice
from demo_ecommerce.query.query_base import render_query, result_as_dict


# list(inspect(record.Customer).mapper.columns)
def query_data(connection_string: str):
    with create_session_maker(connection_string)() as session:

        # pylint: disable=not-callable
        query = select(Customer, Invoice, Invoice.id.label("duplicated_id"))

        print(render_query(session, query))

        for record in session.execute(query):
            print(result_as_dict(record))


if __name__ == "__main__":
    query_data(Connections.MYSQL_SANDBOX.value)
