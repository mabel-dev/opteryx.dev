# Connecting to MySQL using Opteryx

This short guide will demonstrate how to connect to MySQL using Opteryx using [SQLAlchemy](https://www.sqlalchemy.org/).

## Installation

Install Opteryx and libraries for connecting to MySQL.

~~~console
$ pip install opteryx
$ pip install sqlalchemy
$ pip install pymysql
~~~

## Registering MySQL with Opteryx

Create a [SQLAlchemy Engine](https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine) and register it as a store with Opteryx.

~~~python
from sqlalchemy import create_engine
# Replace with your connection string, for more information on SQLAlchemy
# Engine, see:
# https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine
connection_string = "mysql+pymysql://<user>:<password>@<server>/"
sqlalchemy_engine = create_engine(connection_string)

# Register as a store, so we know queries for this relations with the
# provided prefix should be directed to this database
opteryx.register_store(
    prefix="mysql_example",  # can be any string
    connector=SqlConnector,
    remove_prefix=True,  # the prefix isn't part of the MySQL table name
    engine=sqlalchemy_engine,
)
~~~

## Querying MySQL from Opteryx

~~~python
# Execute query against the store, the prefix we registered above is used
# to tell Opteryx that this relation should be read from MySQL using
# the Engine created and registered above
result = opteryx.query("SELECT * FROM mysql_example.planets LIMIT 5;")
result.head()
~~~

## Other Services

Opteryx supports connecting to other SQL engines using this method, such as Postgres, CockroachDB and DuckDB.