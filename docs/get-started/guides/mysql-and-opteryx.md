---
title: Connect MySQL to Opteryx - Query MySQL Database with SQL
description: Learn how to connect MySQL with Opteryx using SQLAlchemy. Query MySQL tables and join with other data sources using Opteryx federated SQL engine.
---

# Connecting to MySQL using Opteryx

This short guide demonstrates how to connect to MySQL using Opteryx and [SQLAlchemy](https://www.sqlalchemy.org/).

## Installation

Install Opteryx and libraries for connecting to MySQL.

~~~console
$ pip install opteryx sqlalchemy pymysql
~~~

## Registering MySQL with Opteryx

Create a [SQLAlchemy Engine](https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine) and register it as a store with Opteryx.

~~~python
import opteryx
from opteryx.connectors import SqlConnector
from sqlalchemy import create_engine

# Replace with your connection string.
# For more information on SQLAlchemy Engine, see:
# https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine
connection_string = "mysql+pymysql://<user>:<password>@<server>/"
sqlalchemy_engine = create_engine(connection_string)

# Register as a store. Queries for relations with the provided prefix will
# be directed to this database.
opteryx.register_store(
    prefix="mysql_example",  # use this prefix before table names in queries
    connector=SqlConnector, 
    remove_prefix=True,  # the prefix isn't part of the MySQL table name
    engine=sqlalchemy_engine,
)
~~~

## Parameters Explained

- `prefix` A string to identify which queries should be directed to this database.
- `connector` The type of connector to use.
- `remove_prefix` Boolean flag to indicate if the prefix should be removed when querying the actual MySQL table.
- `engine` SQLAlchemy Engine to connect to MySQL.

## Querying MySQL from Opteryx

~~~python
# Execute query against the store.
result = opteryx.query("SELECT * FROM mysql_example.planets LIMIT 5;")
result.head()
~~~

## Other Services

Opteryx supports connecting to other SQL engines using this method, such as Postgres, CockroachDB, and DuckDB.

## Related Guides

- [Connect to PostgreSQL](postgres-and-opteryx.md) - Query PostgreSQL databases
- [Connect to BigQuery](bigquery-and-opteryx.md) - Query Google BigQuery
- [Connect to DuckDB](duckdb-and-opteryx.md) - Query DuckDB databases
- [Connect to SQLite](sqlite-and-opteryx.md) - Query SQLite databases
- [Polars Integration](polars-and-opteryx.md) - Work with query results in Polars
