from functools import reduce
from typing import Any, Dict, Union

from sqlalchemy import Row, inspect
from sqlalchemy.orm import DeclarativeBase


def render_query(session, query):
    separator = "-" * 80
    rendered = str(
        query.compile(session.get_bind(), compile_kwargs={"literal_binds": True})
        if hasattr(query, "compile")
        else query.statement.compile(
            session.get_bind(), compile_kwargs={"literal_binds": True}
        )
    )
    return f"{separator}" "\n" f"{rendered}" "\n" f"{separator}"


def model_as_dict(record: DeclarativeBase) -> Dict[str, Any]:
    fields = [column.name for column in inspect(record).mapper.columns]
    return {field: getattr(record, field, None) for field in fields}


def value_as_dict(name: str, value: Any) -> Dict[str, Any]:
    return {name: value}


def result_as_dict(record: Union[Row, DeclarativeBase]) -> Dict:
    if isinstance(record, DeclarativeBase):
        return model_as_dict(record=record)

    fields = record._mapping.keys()  # pylint: disable=protected-access

    elements = [
        (
            model_as_dict(getattr(record, field, None))  # type: ignore[arg-type]
            if isinstance(getattr(record, field, None), DeclarativeBase)
            else {field: getattr(record, field, None)}
        )
        for field in fields
    ]
    return reduce(lambda acc, cur: {**acc, **cur}, elements, {})
