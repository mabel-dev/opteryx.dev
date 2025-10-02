---
title: Connect SQLite to Opteryx - Query SQLite Database with SQL
description: Step-by-step guide to connecting SQLite with Opteryx using SQLAlchemy. Run federated queries across SQLite and other data sources seamlessly.
---

# Connecting to SQLite using Opteryx

This short guide demonstrates how to connect to SQLite using Opteryx and [SQLAlchemy](https://www.sqlalchemy.org/).

## Installation

Install Opteryx and libraries for connecting to SQLite.

~~~console
$ pip install opteryx sqlalchemy
~~~

## Registering SQLite with Opteryx

Create a [SQLAlchemy Engine](https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine) and register it as a store with Opteryx.

~~~python
import opteryx
from opteryx.connectors import SqlConnector
from sqlalchemy import create_engine

# Replace with your SQLite database path.
# For more information on SQLAlchemy Engine, see:
# https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine
connection_string = "sqlite:///database.db"
sqlalchemy_engine = create_engine(connection_string)

# Register as a store. Queries for relations with the provided prefix will
# be directed to this database.
opteryx.register_store(
    prefix="sqlite_example",  # use this prefix before table names in queries
    connector=SqlConnector, 
    remove_prefix=True,  # the prefix isn't part of the SQLite table name
    engine=sqlalchemy_engine,
)
~~~

## Parameters Explained

- `prefix` A string to identify which queries should be directed to this database.
- `connector` The type of connector to use.
- `remove_prefix` Boolean flag to indicate if the prefix should be removed when querying the actual SQLite table.
- `engine` SQLAlchemy Engine to connect to SQLite.

## Querying SQLite from Opteryx

~~~python
# Execute query against the store.
result = opteryx.query("SELECT * FROM sqlite_example.planets LIMIT 5;")
result.head()
~~~

## Other Services

Opteryx supports connecting to other SQL engines using this method, such as Postgres, MySQL, and DuckDB.

## Related Guides

- [Connect to PostgreSQL](postgres-and-opteryx.md) - Query PostgreSQL databases
- [Connect to MySQL](mysql-and-opteryx.md) - Query MySQL databases
- [Connect to DuckDB](duckdb-and-opteryx.md) - Query DuckDB databases
- [Execute SQL on CSV Files](execute-sql-on-csv.md) - Query file-based data
- [Pandas Integration](pandas-and-opteryx.md) - Work with query results in Pandas
