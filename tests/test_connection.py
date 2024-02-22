from sqlalchemy import text
from sqlalchemy.orm import Session
from tutorial.connection import create_db_engine
from tutorial.connection_base import Connections


def test_create_db_engine():
    engine = create_db_engine(Connections.SQLITE.value)
    assert engine is not None


def test_engine_basic_behaviour():
    """
    https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html
    """

    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 'test';"))
        records = result.all()
        assert records == [("test",)]


def test_table_insert():
    """
    https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html
    """

    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)

    with engine.connect() as connection:
        connection.execute(text("CREATE TABLE phonebook(NAME text, NUMBER text);"))
        connection.execute(
            text("INSERT INTO phonebook values(:name, :number);"),
            [{"name": f"nome-{i}", "number": f"{2434 * i}"} for i in range(10)],
        )
        connection.commit()  # type: ignore[attr-defined]

    with engine.connect() as connection:
        result = connection.execute(text("SELECT * from phonebook"))
        records = result.all()
        assert records == [
            ("nome-0", "0"),
            ("nome-1", "2434"),
            ("nome-2", "4868"),
            ("nome-3", "7302"),
            ("nome-4", "9736"),
            ("nome-5", "12170"),
            ("nome-6", "14604"),
            ("nome-7", "17038"),
            ("nome-8", "19472"),
            ("nome-9", "21906"),
        ]


def test_table_insert_session():
    """
    https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html#executing-with-an-orm-session
    """

    engine = create_db_engine(Connections.SQLITE_IN_MEMORY.value)

    with Session(engine) as session:
        session.execute(text("CREATE TABLE phonebook(NAME text, NUMBER text);"))
        session.execute(
            text("INSERT INTO phonebook values(:name, :number);"),
            [{"name": f"nome-{i}", "number": f"{2434 * i}"} for i in range(10)],
        )
        session.commit()

    with Session(engine) as session:
        result = session.execute(text("SELECT * from phonebook"))
        records = result.all()
        assert records == [
            ("nome-0", "0"),
            ("nome-1", "2434"),
            ("nome-2", "4868"),
            ("nome-3", "7302"),
            ("nome-4", "9736"),
            ("nome-5", "12170"),
            ("nome-6", "14604"),
            ("nome-7", "17038"),
            ("nome-8", "19472"),
            ("nome-9", "21906"),
        ]
