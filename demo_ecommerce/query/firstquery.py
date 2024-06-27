from sqlalchemy import (
    create_engine,
    select,
    update,
    insert,
    delete,
    Integer,
    String,
    Numeric,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm.session import sessionmaker

# from sqlalchemy.orm import aliased
# from demo_ecommerce.connection.connection import create_session_maker
# from demo_ecommerce.connection.connection_base import Connections
# from demo_ecommerce.models.models import InvoiceDetail
# from demo_ecommerce.query.query_base import render_query


class BaseModel(DeclarativeBase):
    pass


class Item(BaseModel):
    __tablename__ = "item"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    code: Mapped[str] = mapped_column(String(30), nullable=False)
    description: Mapped[str] = mapped_column(String(5000))


def get_session():
    database = "mysql+pymysql://root:password@localhost:3306/sqlalchemy-tutorial?charset=utf8mb4"  # noqa: E501
    engine = create_engine(database)
    SessionMaker = sessionmaker(bind=engine)
    return SessionMaker()


def firstquery():
    # database = "mysql+pymysql://root:password@localhost:3306/sqlalchemy-tutorial?charset=utf8mb4"  # noqa: E501
    # engine = create_engine(database)
    # SessionMaker = sessionmaker(bind=engine)

    with get_session() as session:
        print("***** CORE 1 *****")
        print(session, Item)
        query = select(Item)

        result = session.execute(query).all()

        for row in result:
            # item = row.Item
            # print(item.id, item.code, item.description)
            print(row)

        print("***** CORE 2 *****")
        query = select(Item.id, Item.code, Item.description)

        result = session.execute(query).all()

        for row in result:
            print("-")
            print(row)
            print(row.id, row.code, row.description)

        print("***** ORM *****")
        items = session.query(Item).all()

        for row in items:
            print("---")
            print(row)
            print(row.id, row.code, row.description)

    with get_session() as session:
        print("***** CORE WHERE *****")

        query = select(Item).where(Item.code == "PN001")

        result = session.execute(query).all()

        for row in result:
            item = row.Item
            print(item.id, item.code, item.description)


def demo_insert():
    with get_session() as session:

        qi = insert(Item).values(
            code="XXX",
            description="Artiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo XArtiocolo X",
        )

        session.execute(qi)

        session.commit()

        query_s = select(Item.id, Item.code, Item.description)

        result = session.execute(query_s).all()

        for row in result:
            print(row.id, row.code, row.description)


def demo_update():
    with get_session() as session:

        qi = (
            update(Item)
            .values(description="Artiocolo di tipo X")
            .where(Item.code == "XXX")
        )

        session.execute(qi)

        session.commit()

        query_s = select(Item.id, Item.code, Item.description)

        result = session.execute(query_s).all()

        for row in result:
            print(row.id, row.code, row.description)


def demo_delete():
    with get_session() as session:

        qi = delete(Item).where(Item.code == "XXX")

        session.execute(qi)

        session.commit()

        query_s = select(Item.id, Item.code, Item.description)

        result = session.execute(query_s).all()

        for row in result:
            print(row.id, row.code, row.description)


# def query_data(connection_string: str):
#     with create_session_maker(connection_string)() as session:

#         detail = aliased(InvoiceDetail)

#         # pylint: disable=not-callable
#         query = select(
#             detail.item_code.label("articolo"),
#             detail.quantity.label("quantita"),
#         )

#         print(render_query(session, query))

#         for record in session.execute(query):
#             print(record.articolo, record.quantita)


def display_items():
    with get_session() as session:

        query_s = select(Item.id, Item.code, Item.description)

        result = session.execute(query_s).all()

        for row in result:
            print(row.id, row.code, row.description)


def demo_insert_orm():
    with get_session() as session:

        my_item = Item(code="YYY", description="Articolo y")

        session.add(my_item)

        session.commit()

        display_items()


def demo_update_orm():
    with get_session() as session:

        my_item = session.query(Item).filter(Item.code == "YYY").one_or_none()

        if my_item is not None:  # oppure: if my_item:
            my_item.description = "Descrizione modificata"

            session.merge(my_item)

            session.commit()

            display_items()


def demo_delete_orm():
    with get_session() as session:

        session.query(Item).filter(Item.code == "YYY").delete()

        session.commit()

        display_items()


if __name__ == "__main__":
    # query_data(Connections.MYSQL_TUTORIAL.value)
    # firstquery()
    # demo_insert()
    # demo_update()
    #  demo_delete()
    # demo_insert_orm()
    # demo_update_orm()
    demo_delete_orm()

    # TODO:
    # - Delete ORM cancellare solo alcuni elementi estratti con la session.query()
    # - Approfondire il funzioamento delle dimensioni dei campi.

    
