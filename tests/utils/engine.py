from tutorial.connection import create_db_engine
from tutorial.connection_base import Connections
from tutorial.orm.models import BaseModel


def create_test_db_engine():
    return create_db_engine(Connections.SQLITE_IN_MEMORY.value)


def setup_orm_db_engine():
    engine = create_test_db_engine()
    BaseModel.metadata.create_all(engine)
    return engine
