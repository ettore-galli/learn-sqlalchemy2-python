import os

from tutorial.orm.models import BaseModel
from tutorial.connection import create_db_engine


if __name__ == "__main__":
    db_path = os.path.join(os.path.dirname(__file__), "data", "database.db")
    connection_string = f"sqlite:///{db_path}"
    engine = create_db_engine(connection_string)
    BaseModel.metadata.create_all(engine)
