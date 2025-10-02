---
title: Connect DuckDB to Opteryx - Query DuckDB Database with SQL
description: Learn how to connect DuckDB with Opteryx using SQLAlchemy. Query DuckDB tables and join with other data sources using Opteryx federated SQL engine.
---

# Connecting to DuckDB using Opteryx

This short guide demonstrates how to connect to [DuckDB](https://duckdb.org/) using Opteryx and [SQLAlchemy](https://www.sqlalchemy.org/).

## Installation

Install Opteryx and libraries for connecting to DuckDB.

~~~console
$ pip install opteryx sqlalchemy duckdb duckdb-engine
~~~

## Registering DuckDB with Opteryx

Create a [SQLAlchemy Engine](https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine) and register it as a store with Opteryx.

~~~python
import opteryx
from opteryx.connectors import SqlConnector
from sqlalchemy import create_engine

# Replace with your DuckDB database path.
# Use ':memory:' for an in-memory database.
# For more information on SQLAlchemy Engine, see:
# https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine
connection_string = "duckdb:///database.duckdb"
sqlalchemy_engine = create_engine(connection_string)

# Register as a store. Queries for relations with the provided prefix will
# be directed to this database.
opteryx.register_store(
    prefix="duckdb_example",  # use this prefix before table names in queries
    connector=SqlConnector, 
    remove_prefix=True,  # the prefix isn't part of the DuckDB table name
    engine=sqlalchemy_engine,
)
~~~

## Parameters Explained

- `prefix` A string to identify which queries should be directed to this database.
- `connector` The type of connector to use.
- `remove_prefix` Boolean flag to indicate if the prefix should be removed when querying the actual DuckDB table.
- `engine` SQLAlchemy Engine to connect to DuckDB.

## Querying DuckDB from Opteryx

~~~python
# Execute query against the store.
result = opteryx.query("SELECT * FROM duckdb_example.planets LIMIT 5;")
result.head()
~~~

## Other Services

Opteryx supports connecting to other SQL engines using this method, such as Postgres, MySQL, and SQLite.

## Related Guides

- [Connect to PostgreSQL](postgres-and-opteryx.md) - Query PostgreSQL databases
- [Connect to MySQL](mysql-and-opteryx.md) - Query MySQL databases
- [Connect to SQLite](sqlite-and-opteryx.md) - Query SQLite databases
- [Query AWS S3](s3-and-opteryx.md) - Query files in Amazon S3
- [Polars Integration](polars-and-opteryx.md) - Use Polars for high-performance analytics

