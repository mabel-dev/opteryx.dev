# Integrating Apache Iceberg with Opteryx

This guide walks you through integrating [Apache Iceberg](https://py.iceberg.apache.org/) with [Opteryx](https://opteryx.dev/), enabling you to run SQL queries directly on Iceberg tables using Opteryx.

The example below uses a SQLite catalog and local file storage. For more advanced configurations—including Hive Metastore, AWS Glue, or remote storage—refer to the [PyIceberg configuration documentation](https://py.iceberg.apache.org/configuration/).

## Installation

Install both Opteryx and PyIceberg using pip:

~~~console
$ pip install opteryx pyiceberg
~~~

## Querying Iceberg Tables with Opteryx

Opteryx supports querying Iceberg tables by registering an Iceberg catalog as a data source.

~~~python
import opteryx
from pyiceberg.catalog.sql import SqlCatalog
from opteryx.connectors import IcebergConnector

# Load the Iceberg catalog (must already exist)
iceberg_catalog = SqlCatalog(
    "default",
    uri="sqlite:///pyiceberg_catalog/pyiceberg_catalog.db",
    warehouse="pyiceberg_catalog",
)

# Register the Iceberg catalog in Opteryx under the 'iceberg' namespace
opteryx.register_store("iceberg", IcebergConnector, catalog=iceberg_catalog)

# Run a query against an Iceberg table (table must exist in the catalog)
results = opteryx.query("SELECT * FROM iceberg.planets")

# Use the results as needed
for row in results:
    print(row)
~~~

> 💡 Note: The iceberg.planets table refers to the planets table inside the Iceberg catalog namespace iceberg.

**Troubleshooting**
- Ensure the Iceberg catalog and referenced tables exist before querying.
- For remote or cloud-based Iceberg storage, update the catalog and warehouse configuration accordingly.
