from sqlalchemy.orm import aliased
from demo_ecommerce.connection.connection import create_session_maker
from demo_ecommerce.connection.connection_base import Connections
from demo_ecommerce.models.models import InvoiceDetail
from demo_ecommerce.query.query_base import render_query


def query_data(connection_string: str):
    with create_session_maker(connection_string)() as session:

        detail = aliased(InvoiceDetail)

        query = session.query(
            detail.item_code.label("codice"), detail.quantity.label("quantita")
        ).limit(3)

        print(render_query(session, query))

        for record in query.all():
            # print(record.item_code, record.quantity, record.item.description)
            print(record.codice, record.quantita)

        query_rel = session.query(detail).limit(3)

        print(render_query(session, query_rel))

        for record in query_rel.all():
            # print(record.item_code, record.quantity, record.item.description)
            print(record.item_code, record.quantity, record.item.description)


if __name__ == "__main__":
    query_data(Connections.MYSQL_SANDBOX.value)
