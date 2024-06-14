from sqlalchemy import select, func, text
from sqlalchemy.orm import scoped_session


def get_invoices_count(db: scoped_session):
    return db.execute(select(func.count()).select_from(text("invoice"))).scalar()
