# pylint: disable=duplicate-code
from sqlalchemy import func, select
from sqlalchemy.orm import aliased
from demo_ecommerce.connection.connection import create_session_maker
from demo_ecommerce.connection.connection_base import Connections
from demo_ecommerce.models.models import Invoice
from demo_ecommerce.query.query_base import render_query, result_as_dict


def query_data(connection_string: str):
    with create_session_maker(connection_string)() as session:

        fatture = aliased(Invoice, name="FATTURE")

        totali = select(
            func.sum(Invoice.id).label("id"),
            func.sum(Invoice.customer_id).label("customer_id"),
        ).subquery()
        totali_fatture = aliased(totali, name="TOTALI")

        # pylint: disable=not-callable
        query = select(fatture).limit(3).union_all(select(totali_fatture))

        print(render_query(session, query))

        for record in session.execute(query):
            print(result_as_dict(record))


if __name__ == "__main__":
    query_data(Connections.MYSQL_LOCAL.value)
