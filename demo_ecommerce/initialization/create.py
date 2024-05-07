import sys

from demo_ecommerce.models.models import BaseModel
from demo_ecommerce.connection.connection import create_db_engine


def create_database(connection_string: str):
    engine = create_db_engine(connection_string)
    BaseModel.metadata.drop_all(engine)
    BaseModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_database(sys.argv[1])
