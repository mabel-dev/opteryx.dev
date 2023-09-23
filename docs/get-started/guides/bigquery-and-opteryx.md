# Connecting to BigQuery using Opteryx

This short guide will demonstrate how to connect to [BigQuery](https://cloud.google.com/bigquery) using Opteryx using [SQLAlchemy](https://www.sqlalchemy.org/).

## Installation

Install Opteryx and libraries for connecting to BigQuery.

~~~console
$ pip install opteryx
$ pip install sqlalchemy
$ pip install sqlalchemy-bigquery
$ pip install google-cloud-bigquery-storage
~~~

## Registering Postgres with Opteryx

Create a [SQLAlchemy Engine](https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine) and register it as a store with Opteryx.

~~~python

# Create an SqlAlchemy Engine connecting to your GCP project. See the
# following libj for more information:
# https://pypi.org/project/sqlalchemy-bigquery/
from sqlalchemy.engine import create_engine
from opteryx.connectors import SqlConnector

GCP_PROJECT:str = "your GCP project"
engine = create_engine(f"bigquery://{GCP_PROJECT}")

# Register as a store, so we know queries for relations with the
# provided prefix (bq) should be directed to BigQuery
opteryx.register_store(
    "bq",  # The prefix to indicate to use this store
    SqlConnector,
    remove_prefix=True,  # the prefix isn't part of the BigQuery table name
    engine=engine  # The SqlAlchemy Engine we created above
)
~~~

## Querying BigQuery from Opteryx

~~~python
# Execute query against the store, the prefix we registered above is used
# to tell Opteryx that this relation should be read from BigQuery using
# the Engine created and registered above
result = opteryx.query("SELECT * FROM bq.planets LIMIT 5;")
result.head()
~~~

## Other Services

Opteryx supports connecting to other SQL engines using this method, such as MySQL, CockroachDB and DuckDB.