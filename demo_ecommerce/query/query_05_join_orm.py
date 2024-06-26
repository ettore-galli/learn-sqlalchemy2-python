from demo_ecommerce.connection.connection import create_session_maker
from demo_ecommerce.connection.connection_base import Connections
from demo_ecommerce.models.models import Customer, Invoice
from demo_ecommerce.query.query_base import render_query, result_as_dict


def query_data(connection_string: str):
    with create_session_maker(connection_string)() as session:

        # pylint: disable=not-callable
        source = session.query(Customer, Invoice).join(
            Invoice, Customer.id == Invoice.customer_id
        )

        print(render_query(session, source))

        for record in source.all():
            print("--- ° " * 10)
            print(result_as_dict(record))
            print(record.Invoice.id)
            print(record.Customer.id)
            print(record.Customer.name)
            for detail in record.Invoice.details:
                print(result_as_dict(detail))


if __name__ == "__main__":
    query_data(Connections.MYSQL_SANDBOX.value)
