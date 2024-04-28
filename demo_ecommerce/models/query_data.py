import sys

from sqlalchemy import exists, literal, select

from demo_ecommerce.connection.connection import create_session_maker
from demo_ecommerce.models.models import Customer, Invoice


def attributes(obj):
    return [item for item in dir(obj) if not item.startswith("_")]


def render_query(session, query):
    return str(
        query.compile(session.get_bind(), compile_kwargs={"literal_binds": True})
    )


def query_data(connection_string: str):
    with create_session_maker(connection_string)() as session:

        print("-" * 80)

        # Elenco clienti
        query_elenco = select(Customer).where(Customer.name.like("%oni%"))

        print(render_query(session, query_elenco))

        for record in session.execute(query_elenco.limit(5)):
            print(record[0].name, record[0].address)

        print("-" * 80)

        # Elenco clienti e fatture (join)
        query_clienti = select(Customer, Invoice).join(
            Invoice, Customer.id == Invoice.customer_id
        )

        print(render_query(session, query_clienti))

        for record in session.execute(query_clienti.limit(5)):
            print(record.Customer.id, record.Customer.name, record.Invoice.id)

        print("-" * 80)

        # Elenco clienti con fatture (exists)
        query_exists = select(Customer).where(
            exists().where(Customer.id == Invoice.customer_id)
        )

        print(render_query(session, query_exists))

        for record in session.execute(query_clienti.limit(5)):
            print(record.Customer.id, record.Customer.name)

        print("-" * 80)

        # Exists alternativa
        subq_exists = (
            select(literal(1)).where((Customer.id == Invoice.customer_id)).exists()
        )

        query_exists_2 = select(Customer).where(subq_exists)
        print(render_query(session, query_exists_2))

        for record in session.execute(query_clienti.limit(5)):
            print(record.Customer.id, record.Customer.name)


if __name__ == "__main__":
    query_data(sys.argv[1])
