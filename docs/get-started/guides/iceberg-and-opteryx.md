# Iceberg and Opteryx Integration

This short guide demonstrates how to integrate [Apache Iceberg](https://py.iceberg.apache.org/) and [Opteryx](https://opteryx.dev/), showing you how to query an Iceberg Table with Opteryx.

This example is using a catalog in SQLite and local storage as the file store, for other configurations and more detail how to create and connect to Iceberg refer to the [PyIceberg Documentation](https://py.iceberg.apache.org/configuration/).

## Installation

Install Opteryx and PyIceberg.

~~~console
$ pip install opteryx
$ pip install pyiceberg[sql-sqlite]
~~~

## Iceberg to Opteryx

Opteryx can natively query Pandas DataFrames by registering the DataFrame as a data source.

~~~python
import opteryx
from pyiceberg.catalog.sql import SqlCatalog

# Load the catalog - this must already exist
iceberg_catalog = SqlCatalog(
    "default",
    **{
        "uri": f"sqlite:///pyiceberg_catalog/pyiceberg_catalog.db",
        "warehouse": "pyiceberg_catalog",
    },
)

# Register the 'iceberg' namespace to use the IcebergConnector and catalot
opteryx.register_store("iceberg", IcebergConnector, catalog=iceberg_catalog)

# Query a table in the catalog - this must already exist
results = opteryx.query("SELECT * FROM iceberg.planets")
~~~
