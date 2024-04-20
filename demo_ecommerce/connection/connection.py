from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine


def create_db_engine(database: str) -> Engine:
    engine = create_engine(database)
    return engine
