import os

from tutorial.core.models import db_metadata
from tutorial.connection import create_db_engine


if __name__ == "__main__":
    db_path = os.path.join(os.path.dirname(__file__), "data", "database.db")
    connection_string = f"sqlite:///{db_path}"
    engine = create_db_engine(connection_string)
    db_metadata.create_all(engine)
