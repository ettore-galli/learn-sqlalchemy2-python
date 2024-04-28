import sys


from demo_ecommerce.connection.connection import create_session_maker
from demo_ecommerce.models.models import Customer


def attributes(obj):
    return [item for item in dir(obj) if not item.startswith("_")]


def query_data_orm(connection_string: str):
    with create_session_maker(connection_string)() as session:

        print("-" * 80)

        # Elenco fatture per cliente
        query_clienti = session.query(Customer).where(Customer.id == 1)

        cliente = query_clienti.all()[0]

        print(cliente.__dict__)

        print(cliente.invoices)


if __name__ == "__main__":
    query_data_orm(sys.argv[1])
