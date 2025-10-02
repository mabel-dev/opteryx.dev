---
title: Connect BigQuery to Opteryx - Query Google BigQuery with SQL
description: Complete guide to connecting Google BigQuery with Opteryx using SQLAlchemy. Query BigQuery tables alongside other data sources with unified SQL interface.
---

# Connecting to BigQuery using Opteryx

This short guide demonstrates how to connect to [BigQuery](https://cloud.google.com/bigquery) using Opteryx using [SQLAlchemy](https://www.sqlalchemy.org/).

## Installation

Install Opteryx and libraries for connecting to BigQuery.

~~~console
$ pip install opteryx sqlalchemy sqlalchemy-bigquery google-cloud-bigquery-storage
~~~

## Registering BigQuery with Opteryx

Create a [SQLAlchemy Engine](https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine) and register it as a store with Opteryx.

~~~python
import opteryx
from opteryx.connectors import SqlConnector
from sqlalchemy.engine import create_engine

# Create an SqlAlchemy Engine connecting to your GCP project.
# See the following page for more information:
# https://pypi.org/project/sqlalchemy-bigquery/
GCP_PROJECT:str = "your GCP project"
engine = create_engine(f"bigquery://{GCP_PROJECT}")

# Register as a store, so we know queries for relations with the
# provided prefix (bq) should be directed to BigQuery
opteryx.register_store(
    prefix="bq",  # The prefix to indicate to use this store
    connector=SqlConnector,
    remove_prefix=True,  # the prefix isn't part of the BigQuery table name
    engine=engine  # The SqlAlchemy Engine we created above
)
~~~

## Parameters Explained

- `prefix` A string to identify which queries should be directed to this database.
- `connector` The type of connector to use.
- `remove_prefix` Boolean flag to indicate if the prefix should be removed when querying the actual BigQuery table.
- `engine` SQLAlchemy Engine to connect to BigQuery.

## Querying BigQuery from Opteryx

~~~python
# Execute query against the store.
result = opteryx.query("SELECT * FROM bq.planets LIMIT 5;")
result.head()
~~~

## Other Services

Opteryx supports connecting to other SQL engines using this method, such as MySQL, CockroachDB and DuckDB.

## Related Guides

- [Connect to PostgreSQL](postgres-and-opteryx.md) - Query PostgreSQL databases
- [Connect to MySQL](mysql-and-opteryx.md) - Query MySQL databases
- [Connect to DuckDB](duckdb-and-opteryx.md) - Query DuckDB databases
- [Query Google Cloud Storage](gcs-and-opteryx.md) - Combine BigQuery with GCS data
- [Pandas Integration](pandas-and-opteryx.md) - Work with query results in Pandas
