from sqlalchemy import select
from sqlalchemy.orm import aliased
from demo_ecommerce.connection.connection import create_session_maker
from demo_ecommerce.connection.connection_base import Connections
from demo_ecommerce.models.models import InvoiceDetail
from demo_ecommerce.query.query_base import render_query


def query_data(connection_string: str):
    with create_session_maker(connection_string)() as session:

        detail = aliased(InvoiceDetail)

        # pylint: disable=not-callable
        query = select(
            detail.item_code.label("articolo"),
            detail.quantity.label("quantita"),
        )

        print(render_query(session, query))

        for record in session.execute(query):
            print(record.articolo, record.quantita)


if __name__ == "__main__":
    query_data(Connections.MYSQL_TUTORIAL.value)
