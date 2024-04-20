from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import sessionmaker


def create_db_engine(database: str) -> Engine:
    engine = create_engine(database)
    return engine


def create_session_maker(database: str) -> sessionmaker:
    return sessionmaker(bind=create_db_engine(database=database))
