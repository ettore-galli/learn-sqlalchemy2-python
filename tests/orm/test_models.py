from decimal import Decimal
from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import Session
from tests.utils.engine import setup_orm_db_engine

from tutorial.orm.models import Customer, Item, PriceList


def test_db_models():
    with Session(setup_orm_db_engine()) as session:
        data = [
            Customer(name="Ettore", address="Via dei Tigli"),
            Item(code="P001", description="Pinza manico rosso"),
            Item(code="L001", description="Lampadina piccola"),
            Item(code="L002", description="Lampadina media"),
            PriceList(item_code="L001", price=Decimal("2.30")),
            PriceList(item_code="L002", price=Decimal("2.50")),
        ]
        for item in data:
            session.add(item)
        session.commit()

        query = select(Customer)
        result = session.execute(query).all()
        assert result[0].Customer.name == "Ettore"

        query = select(Item)
        result = session.execute(query).all()
        assert [item.Item.code for item in result] == ["P001", "L001", "L002"]
        assert [
            item.Item.price_list.price if item.Item.price_list else "<none>"
            for item in result
        ] == ["<none>", Decimal("2.30"), Decimal("2.50")]


def test_core_insert_with_orm_models():
    with Session(setup_orm_db_engine()) as session:

        session.execute(insert(Customer).values(name="Ettore", address="Via dei Tigli"))
        session.commit()

        query = select(Customer)
        result = session.execute(query).all()
        assert result[0].Customer.name == "Ettore"


def test_basic_select():
    with Session(setup_orm_db_engine()) as session:
        data = [
            Customer(name="Ettore", address="Via dei Tigli"),
            Item(code="P001", description="Pinza manico rosso"),
            Item(code="L001", description="Lampadina piccola"),
            Item(code="L002", description="Lampadina media"),
            PriceList(item_code="L001", price=Decimal("2.30")),
            PriceList(item_code="L002", price=Decimal("2.50")),
        ]
        for item in data:
            session.add(item)
        session.commit()

        query = select(Item).where(Item.code == "L001")
        result = session.execute(query).all()
        assert len(result) == 1
        assert result[0].Item.description == "Lampadina piccola"

        result_orm = session.query(Item).filter(Item.code == "L002").all()
        assert len(result_orm) == 1
        assert result_orm[0].description == "Lampadina media"


def test_update_delete_core_style():
    with Session(setup_orm_db_engine()) as session:
        data = [
            Customer(name="Ettore", address="Via dei Tigli"),
            Item(code="P001", description="Pinza manico rosso"),
            Item(code="L001", description="Lampadina piccola"),
            Item(code="L002", description="Lampadina media"),
            PriceList(item_code="L001", price=Decimal("2.30")),
            PriceList(item_code="L002", price=Decimal("2.50")),
        ]
        for item in data:
            session.add(item)
        session.commit()

        for statement in [
            (
                update(Item)
                .values(description="Lampadina standard")
                .where(Item.code == "L002")
            ),
            (delete(Item).where(Item.code == "P001")),
        ]:
            session.execute(statement)

        result_orm = session.query(Item).all()

        assert len(result_orm) == 2
        assert [record.description for record in result_orm] == [
            "Lampadina piccola",
            "Lampadina standard",
        ]


def test_update_delete_orm_style():
    with Session(setup_orm_db_engine()) as session:
        data = [
            Customer(name="Ettore", address="Via dei Tigli"),
            Item(code="P001", description="Pinza manico rosso"),
            Item(code="L001", description="Lampadina piccola"),
            Item(code="L002", description="Lampadina media"),
            PriceList(item_code="L001", price=Decimal("2.30")),
            PriceList(item_code="L002", price=Decimal("2.50")),
        ]
        for item in data:
            session.add(item)
        session.commit()

        p1 = session.query(Item).where(Item.code == "P001").one_or_none()
        session.delete(p1)

        l2 = session.query(Item).where(Item.code == "L002").one_or_none()
        if l2:
            l2.description = "Lampadina standard"

        session.commit()

        result_orm = session.query(Item).all()

        assert len(result_orm) == 2
        assert [record.description for record in result_orm] == [
            "Lampadina piccola",
            "Lampadina standard",
        ]


def test_join_orm():
    with Session(setup_orm_db_engine()) as session:
        data = [
            Customer(name="Ettore", address="Via dei Tigli"),
            Item(code="P001", description="Pinza manico rosso"),
            Item(code="L001", description="Lampadina piccola"),
            Item(code="L002", description="Lampadina media"),
            PriceList(item_code="L001", price=Decimal("2.30")),
            PriceList(item_code="L002", price=Decimal("2.50")),
        ]
        for item in data:
            session.add(item)
        session.commit()

        result = session.query(Item).all()

        assert [
            (
                record.code,
                record.description,
                record.price_list.price if record.price_list else "-",
            )
            for record in result
        ] == [
            ("P001", "Pinza manico rosso", "-"),
            ("L001", "Lampadina piccola", Decimal("2.300000000")),
            ("L002", "Lampadina media", Decimal("2.500000000")),
        ]


def test_join_core():
    with Session(setup_orm_db_engine()) as session:
        data = [
            Customer(name="Ettore", address="Via dei Tigli"),
            Item(code="P001", description="Pinza manico rosso"),
            Item(code="L001", description="Lampadina piccola"),
            Item(code="L002", description="Lampadina media"),
            PriceList(item_code="L001", price=Decimal("2.30")),
            PriceList(item_code="L002", price=Decimal("2.50")),
        ]
        for item in data:
            session.add(item)
        session.commit()

        query = select(Item, PriceList).join(
            PriceList, Item.code == PriceList.item_code, isouter=True
        )

        result = session.execute(query).all()

        assert [
            (
                record.Item.code,
                record.Item.description,
                record.PriceList.price if record.PriceList else "*NO PRICE*",
            )
            for record in result
        ] == [
            ("P001", "Pinza manico rosso", "*NO PRICE*"),
            ("L001", "Lampadina piccola", Decimal("2.300000000")),
            ("L002", "Lampadina media", Decimal("2.500000000")),
        ]
