# SQLALCHEMY 2

## Introduzione

Riassunto condensato di SQLAlchemy per chi va di fretta e ha bisogno di sapere come si fanno le cose.

## Riferimenti

Home page del tutorial
<https://docs.sqlalchemy.org/en/20/tutorial/index.html>

Differenza tra Connection e Session
<https://stackoverflow.com/questions/34322471/sqlalchemy-engine-connection-and-session-difference>

## Modi di funzionamento

### Core

Dal tutorial:

> "SQLAlchemy Core is the foundational architecture for SQLAlchemy as a “database toolkit”. The library provides tools for managing connectivity to a database, interacting with database queries and results, and programmatic construction of SQL statements."

### ORM

> "SQLAlchemy ORM builds upon the Core to provide optional object relational mapping capabilities. The ORM provides an additional configuration layer allowing user-defined Python classes to be mapped to database tables and other constructs, as well as an object persistence mechanism known as the Session. It then extends the Core-level SQL Expression Language to allow SQL queries to be composed and invoked in terms of user-defined objects."

### Domanda aperta

Abbiamo **bisogno** veramente dell'ORM?

## Connessione e sessione

## Definizione tabelle

## Costruzione ed esecuzione statement SQL

### Insert

### Select (base)

### Update

### Delete

### Select avanzate (ricette)

#### Join

#### Exists
