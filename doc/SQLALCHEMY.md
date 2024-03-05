# SQLALCHEMY 2

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

.

</style>

## Introduzione

Riassunto condensato di SQLAlchemy per chi va di fretta e ha bisogno di sapere come si fanno le cose.

## Riferimenti

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

### Domanda aperta

Abbiamo **bisogno** veramente dell'ORM?

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

## Definizione tabelle

Alla base delle funzionalità di SQLAlchemy ci sono i concetti di tabella e colonna, utilizzati sia dalla parte Core che dalla parte ORM.

### L'oggetto MetaData

E' la collezione di oggetti che rappresentano il database (tabelle, colonne...)

```python
from sqlalchemy import MetaData

metadata = MetaData()

```

### Definizione delle tabelle in stile Core

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


class Customer(BaseModel):
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    address: Mapped[str] = mapped_column(String(200), nullable=True)

```

### vincoli e relazioni in stile ORM

<https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html>

## Costruzione ed esecuzione statement SQL

### Insert

### Select (base)

### Update

### Delete

### Select avanzate (ricette)

#### Join

#### Exists
