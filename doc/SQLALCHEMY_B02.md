# SQLALCHEMY - CHEAT SHEET

<!-- markdownlint-disable MD033 -->
<style>
h1 {
    font-size: 30px;
}
h2 {
    font-size: 24px;
}
h3 {
    font-size: 22px;
}
h4 {
    font-size: 20px;
}
h4 {
    font-size: 18px;
}

div {
    padding: 5px;
}

.box {
    border: 1px solid;
    position: relative;
    margin: 5%;
}



</style>

## Introduzione

SQLAlchemy è un framework che fornisce:

- Astrazione per l'interazione col DB ("core")
- Funzionalità ("ORM")

## FARE Tutti gli esempi 1.4

## AGGIUNGERE

* install Librerie specifiche DB
- alias
- label
- order_by
- limit + offset
- join
- group by
- distinct

già fatte
- exists
- join

## Installazione

```shell
pip install sqlalchemy
```

## AGGIUNGERE installazione del client del DB

Nella semplicità del comando di installazione è "naascosta" la natura da un lato doppia (core/orm) dall'altra parte inscindibile che suggerirà alcune strategie d'uso.

## Riferimenti

SQLAlchemy 2 ha - finalmente - un tutorial.

Home page del tutorial
<https://docs.sqlalchemy.org/en/20/tutorial/index.html>

Differenza tra Connection e Session
<https://stackoverflow.com/questions/34322471/sqlalchemy-engine-connection-and-session-difference>

## Modi di funzionamento: Core e ORM

### Core

Dal tutorial:

> "SQLAlchemy Core is the foundational architecture for SQLAlchemy as a “database toolkit”. The library provides tools for managing connectivity to a database, interacting with database queries and results, and programmatic construction of SQL statements."

### ORM

Dal tutorial:

> "SQLAlchemy ORM builds upon the Core to provide optional object relational mapping capabilities. The ORM provides an additional configuration layer allowing user-defined Python classes to be mapped to database tables and other constructs, as well as an object persistence mechanism known as the Session. It then extends the Core-level SQL Expression Language to allow SQL queries to be composed and invoked in terms of user-defined objects."

<!-- markdownlint-disable MD033 -->
<div class="box" style="width: 100%">
<h4>ORM</h4>
    <div class="box" style="width: 75%">
    <h4>Core</h4>
    </div>
</div>

## _Engine_, _Connection_ e _Session_

<!-- markdownlint-disable MD033 -->
<div class="box" style="width: 100%;">
<h4>Session</h4>
Fornisce le funzionalità ORM
    <div class="box" style="width: 75%;">
    <h4>Connection</h4>
    Fornisce l'interfaccia per l'esecuzione transazionale dei comandi
        <div class="box" style="width: 50%;">
        <h4>Engine</h4>
        Fornisce la base per la connessione
        </div>
    </div>
</div>

## Percorso consigliato da SQLAlchemy

--> SPOSTARE IN FONDO
Leggendo la documentazione si evince che SQLAlchemy permette ed ha permesso nel tempo una molteplicità di modalità operative; Con la versione 2.0 tuttavia emerge che la via consigliata di lavorare è un mix di feature core ed ORM.

In particolare:

- Per l'accesso alle operazioni di database viene consogliato di utilizzare sempre la Session (ORM)

- Per la definizione delle tabelle viene consigliata la sintassi ORM in quanto più completa di funzionalità

- Per l'esecuzione delle operazioni sul DB sono disponibili entrambe le strade; tuttavia se non ci sono particolari necessità di utilizzare le finzionalità ORM viene suggerito di eseguire glli statement in modalità e stile core.

## Creazione della connessione e sessione

Per creare una connessione o una sessione si segue grossomodo lo schema logico spiegato sopra.

I passaggi logici risultano quindi essere:

### 1. Creazione di un oggetto Engine

```python

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import sessionmaker


database:str = "mysql+pymysql://root:password@localhost:3306/sandbox?charset=utf8mb4" 
engine = create_engine(database)
 

```

### 2/a. Creazione di un oggetto Connection

Per completezza si mostra l'istanziazione di un a Connection anche se la raccomandazione di SQLAlchemy è quella di utilizzare un oggetto di tipo Session anche se i utilizzano le soloe funzionalità ORM

```python

with engine.connect() as connection:
    ...


```

### 2/b. Creazione di un oggetto Session

```python

from sqlalchemy.orm import Session
from sqlalchemy.orm.session import sessionmaker

# Creare un session_maker
# https://medium.com/@keyyleiva/easy-database-handling-with-sqlalchemys-sessionmaker-659f718a86d5#:~:text=The%20SessionMaker%20is%20a%20tool,changes%2C%20and%20executing%20database%20queries.

Session = sessionmaker(bind=create_db_engine(database=database))

# Creare un oggetto session

session = Session()

```

### 3. Utilizzo dell'oggetto connection o session

Il modo suggerito è quello di usare la session come context manager

```python

with Session() as session:
    ...

```

## Definizione tabelle

Alla base delle funzionalità di SQLAlchemy ci sono i concetti di tabella e colonna, utilizzati sia dalla parte Core che dalla parte ORM.

### L'oggetto MetaData

E' la collezione di oggetti che rappresentano il database (tabelle, colonne...)

```python
from sqlalchemy import MetaData

metadata = MetaData()

```

### Definizione delle tabelle in stile Core

Viene illustrato per completezza un esempio di creazione tabelle in stile Core, anche se è consigliato comunque di utilizzare l'ORM

<https://docs.sqlalchemy.org/en/20/tutorial/metadata.html#setting-up-metadata-with-table-objects>

Si veda anche ```tutorial/core/models.py``````

Esempio di tabella

```python
from sqlalchemy import Column, Integer, String, MetaData

from sqlalchemy import Table

db_metadata = MetaData()

customer = Table(
    "customer",
    db_metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("address", String(100), nullable=True),
)

```

### Vincoli e relazioni stile Core

<https://docs.sqlalchemy.org/en/20/core/constraints.html>

Chiave esterna

```python

Column("item_id", ForeignKey(item.c.id), nullable=False),
```

Unicità

```python

Column("colx", Integer, unique=True),
...
UniqueConstraint("col_a", "col_b", name="my_unique_constraint"),

```

Vincoli vari

Si noti come sia possibile definire il vincolo al di fuori della tabella, esattamente come in SQL, con il grosso vantaggio di poter riferirsi direttamente agli oggetti colonna e non esprimere espressioni testuali (non parsate che rischiano di rompersi a runtime)

Tuttavia anrebbero usati col contagocce.

```python

CheckConstraint("col2 > col3 + 5", name="check1"),

...

CheckConstraint(
    price_list.c.price > 0,
    name="check_price",
    table=price_list,
)

```

Chiave primaria

La versione esplicita (```PrimaryKeyConstraint("id")```) in fase di creazione effettua il controllo della correttezza del nome colonna per cui risulta _safe_ (basta un test unitario o un conftest che fa il create_all per tenere sotto controllo la cosa); ha il vantaggio di poter dare il nome al constraint.

```python
Column("id", Integer, primary_key=True),

...

item = Table(
    "item",
    db_metadata,
    Column("id", Integer),
    Column("description", String(50), nullable=False),
    PrimaryKeyConstraint("id", name"my_primary_key"),
)

```

### Definizione delle tabelle in stile ORM

<https://docs.sqlalchemy.org/en/20/tutorial/metadata.html#using-orm-declarative-forms-to-define-table-metadata>

Le definizioni in stile ORM sono quelle raccomandate perché

- Sono in stile più "pythonico"
- Migliore compatibilità con i type checkers (mypy)
- Disponibilità sia delle funzionalità ORM che Core, essendo una Façade su Table

```python
class BaseModel(DeclarativeBase):
    pass


db_orm_metadata = BaseModel.metadata

# Sqlalchemy 2.x

class Customer(BaseModel):
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    address: Mapped[str] = mapped_column(String(200), nullable=True)

```

```python

# Sqlalchemy 1.4

class Customer(BaseModel):
    __tablename__ = "customer"

    id: int = sa.Column(sa.Integer, primary_key=True)
    name: str = sa.Column(sa.String(50), nullable=False)
    address: str = sa.Column(sa.String(200), nullable=True)

```

### vincoli e relazioni in stile ORM

<https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html>

Le relazioni vengono definite tutte attraverso l'insieme di Foreign Key e la funzione relationship().

```python

class Customer(BaseModel):
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    address: Mapped[str] = mapped_column(String(200), nullable=True)
    invoices: Mapped[List[Invoice]] = relationship(back_populates="customer")
 
class Invoice(BaseModel):
    __tablename__ = "invoice"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey(Customer.id))
    customer: Mapped[Customer] = relationship(back_populates="invoices")

```

## Costruzione ed esecuzione statement SQL

Spiegazione del pattern "unit of work"

<https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html#data-manipulation-with-the-orm>

> Unit of work:
A software architecture where a persistence system such as an object relational mapper maintains a list of changes made to a series of objects, and periodically flushes all those pending changes out to the database.
SQLAlchemy’s Session implements the unit of work pattern, where objects that are added to the Session using methods like Session.add() will then participate in unit-of-work style persistence.

### Creazione della sessione

L'utilizzo dell'oggetto Session è la via raccomandata ancjhe nel caso in cui si vogliano scrivere gli statement in modalità "core"

Gli step logici sono:

1. Stringa di connessione -> Engine
2. Session maker
3. scoped_session (context manager)

```python

database: str = "mysql+pymysql://root:password@localhost:3306/sandbox?charset=utf8mb4"

# 1.
engine = create_engine(database)

#    2.                                     3.
with create_session_maker(connection_string)() as session:
    session.execute(...)

```

### Insert

#### Insert Core Style

```python
from sqlalchemy import insert
session.execute(insert(Customer).values(name="Ettore", address="Via dei Tigli"))

```

#### Insert ORM Style

```python
record = Customer(name="Ettore", address="Via dei Tigli")
session.add(record)
session.commit()

```

### Select (base)

<https://docs.sqlalchemy.org/en/20/tutorial/data_select.html#selecting-orm-entities-and-columns>

Differenza tra core ed ORM nel risultato:

> When executing a statement like the above using the ORM Session.execute() method, there is an important difference when we select from a full entity such as User, as opposed to user_table, which is that the entity itself is returned as a single element within each row.

#### Select Core Style

```python
from sqlalchemy import select

query = select(Item).where(Item.code == "L001")
result = session.execute(query).all()

# result_orm == [(Item,)]
```

#### Select ORM Style

```python
result = session.query(Item).filter(Item.code == "L002").all()

# result == [Item]
```

### Update

#### Update Core Style

```python
from sqlalchemy import update

session.execute(
    update(Item).values(description="Lampadina standard").where(Item.code == "L002")
)        
```

#### Update ORM Style

```python
l2 = session.query(Item).where(Item.code=="L002").one_or_none()
l2.description = "Lampadina standard"

```

### Delete

#### Delete Core Style

```python
from sqlalchemy import delete

session.execute(
    delete(Item).where(Item.code == "P001")
)

```

#### Delete ORM Style

```python
p1 = session.query(Item).where(Item.code=="P001").one_or_none()
session.delete(p1)

```

### Select avanzate (ricette) Core style

#### Join

<https://docs.sqlalchemy.org/en/20/tutorial/data_select.html#explicit-from-clauses-and-joins>

```python

"""
SELECT customer.id, customer.name, customer.address, invoice.id AS id_1, invoice.customer_id 
FROM customer INNER JOIN invoice ON customer.id = invoice.customer_id
"""


query = select(Customer, Invoice).join(
    Invoice, Customer.id == Invoice.customer_id
)

result = session.execute(query).all()

```

#### Exists

<https://docs.sqlalchemy.org/en/20/tutorial/data_select.html#explicit-from-clauses-and-joins>

```python


# Versione 1
"""
SELECT customer.id, customer.name, customer.address 
FROM customer 
WHERE EXISTS (SELECT * 
FROM invoice 
WHERE customer.id = invoice.customer_id)
"""

query_exists = select(Customer).where(
    exists().where(Customer.id == Invoice.customer_id)
)

# Versione 2

"""
SELECT customer.id, customer.name, customer.address 
FROM customer 
WHERE EXISTS (SELECT 1 AS anon_1 
FROM invoice 
WHERE customer.id = invoice.customer_id)
"""

subq_exists = (
    select(literal(1)).where((Customer.id == Invoice.customer_id)).exists()
)

query_exists_2 = select(Customer).where(subq_exists)
 

```
