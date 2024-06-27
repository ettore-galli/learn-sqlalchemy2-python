# pylint: disable=too-few-public-methods
from enum import Enum


# pylint: disable=line-too-long
class Connections(Enum):
    SQLITE_IN_MEMORY = "sqlite://"
    SQLITE = "sqlite:///./db-sqlite/database.db"
    MYSQL_SANDBOX = (
        "mysql+pymysql://root:password@localhost:3306/sandbox?charset=utf8mb4"
    )
    MYSQL_TUTORIAL = "mysql+pymysql://root:password@localhost:3306/sqlalchemy-tutorial?charset=utf8mb4"  # noqa: E501
