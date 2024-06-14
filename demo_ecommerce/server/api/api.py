from fastapi import Depends, FastAPI
from sqlalchemy.orm import scoped_session


from demo_ecommerce.connection.connection import create_session_maker
from demo_ecommerce.server.repo.invoice import get_invoices_count

app = FastAPI()


def get_db_session() -> scoped_session:
    db = "mysql+pymysql://root:password@localhost:3306/sqlalchemy-tutorial?charset=utf8mb4"
    return create_session_maker(database=db)()


base_dependencies = [Depends(get_db_session)]


@app.post("/something/")
def conteggio(db: scoped_session = Depends(get_db_session)):
    return {"db": get_invoices_count(db=db)}
