from dataclasses import dataclass


@dataclass
class Config:
    database: str


def get_config() -> Config:
    return Config(
        database="mysql+pymysql://root:password@localhost:3306/sqlalchemy-tutorial?charset=utf8mb4"
    )
