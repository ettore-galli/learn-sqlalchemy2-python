import sys
import random

from sqlalchemy import insert, select

from faker import Faker
import faker_commerce

from demo_ecommerce.connection.connection import create_session_maker
from demo_ecommerce.models.models import (
    Customer,
    Invoice,
    InvoiceDetail,
    Item,
    PriceList,
)


def create_fake_data():
    number_of_customers = 30
    number_of_products = 100
    fake = Faker("it_IT")
    fake.add_provider(faker_commerce.Provider)

    fake_customers = [
        (fake.company(), fake.address()) for _ in range(number_of_customers)
    ]
    fake_products = [
        (fake.ean13(), fake.ecommerce_name(), fake.ecommerce_price() / 100)
        for _ in range(number_of_products)
    ]
    fake_invoices = [
        (
            random.choice(fake_customers),
            [
                (random.choice(fake_products), random.randint(1, 10))
                for _ in range(random.randint(1, 20))
            ],
        )
    ]

    return fake_customers, fake_products, fake_invoices


def init_fake_data(connection_string: str):

    fake_customers, fake_products, fake_invoices = create_fake_data()

    with create_session_maker(connection_string)() as session:
        for name, address in fake_customers:
            session.execute(insert(Customer).values(name=name, address=address))

        for ean13, name, _ in fake_products:
            session.execute(insert(Item).values(code=ean13, description=name))

        for fake_customers, invoice_detail in fake_invoices:
            name, _ = fake_customers
            customer = session.execute(
                select(Customer.id).where(Customer.name == name)
            ).one_or_none()
            if customer is not None:
                customer_id = customer[0]
                record = session.execute(
                    insert(Invoice).values(customer_id=customer_id)
                )
                invoice_id = record.inserted_primary_key[0]
                for product, quantity in invoice_detail:
                    code, _, price = product
                    session.execute(
                        insert(InvoiceDetail).values(
                            invoice_id=invoice_id,
                            item_code=code,
                            quantity=quantity,
                            unit_price=price,
                        )
                    )

        session.commit()


if __name__ == "__main__":
    init_fake_data(sys.argv[1])
