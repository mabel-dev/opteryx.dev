# Connecting to Postgres using Opteryx

This short guide will demonstrate how to connect to Postgres using Opteryx using [SQLAlchemy](https://www.sqlalchemy.org/).

## Installation

Install Opteryx and optional libraries for connecting to Postgres.

~~~console
$ pip install opteryx
$ pip install sqlalchemy
$ pip install psycopg2-binary
~~~

## Registering Postgres with Opteryx

Create a [SQLAlchemy Engine](https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine) and register it as a store with Opteryx.

~~~python
from sqlalchemy import create_engine
# Replace with your connection string, for more information on SQLAlchemy Engine, see
# https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine
connection_string = "postgresql+psycopg2://<user>:<password>@<server>/"
sqlalchemy_engine = create_engine(connection_string)

# Register as a store, so we know queries for this relations with the provided prefix 
# should be directed to this database
opteryx.register_store(
    prefix="postgres_example",  # can be any string
    connector=SqlConnector,
    remove_prefix=True,  # the prefix isn't part of the SQLite table name
    engine=sqlalchemy_engine,
)
~~~

## Querying Postgres from Opteryx

~~~python
# Execute query against the store, the prefix we registered above is used to tell
# Opteryx that this relation should be read from Postgres using the Engine created
# and registered above
result = opteryx.query("SELECT * FROM postgres_example.planets LIMIT 5;")
result.head()
~~~