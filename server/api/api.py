from fastapi import Depends, FastAPI
from sqlalchemy.orm import scoped_session


from server.connection.connection import create_session_maker
from server.config.config import get_config
from server.repo.invoice import get_invoices_count

app = FastAPI()


def get_db_session() -> scoped_session:
    return create_session_maker(database=get_config().database)()


base_dependencies = [Depends(get_db_session)]


@app.post("/something/")
def conteggio(db: scoped_session = Depends(get_db_session)):
    return {"db": get_invoices_count(db=db)}
