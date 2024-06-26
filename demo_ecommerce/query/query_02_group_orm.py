from sqlalchemy import func
from demo_ecommerce.connection.connection import create_session_maker
from demo_ecommerce.connection.connection_base import Connections
from demo_ecommerce.models.models import InvoiceDetail
from demo_ecommerce.query.query_base import render_query


def query_data(connection_string: str):
    with create_session_maker(connection_string)() as session:

        # pylint: disable=not-callable
        query = session.query(
            InvoiceDetail.item_code, func.count(InvoiceDetail.id).label("occurrences")
        ).group_by(InvoiceDetail.item_code)

        print(render_query(session, query))

        for record in query.all():
            print(record.item_code, record.occurrences)


if __name__ == "__main__":
    query_data(Connections.MYSQL_SANDBOX.value)
