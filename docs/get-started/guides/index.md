---
title: Opteryx Integration Guides - Connect to Databases and Data Sources
description: Comprehensive guides for integrating Opteryx with databases, cloud storage, and data tools. Connect to PostgreSQL, MySQL, BigQuery, S3, Iceberg, Pandas and more.
---

# Integration Guides

Opteryx provides flexible integration options to query data across multiple sources. These guides will help you connect Opteryx to various databases, cloud storage systems, and data tools.

## Getting Started

New to Opteryx? Start here:

- **[Quickstart Guide](../quickstart.md)** - Get Opteryx up and running in minutes
- **[Python API](../python-client.md)** - Learn the Python API basics
- **[Using with Jupyter Notebooks](using-opteryx-with-jupyter.md)** - Interactive data analysis

## Data Sources

Query data from various storage systems without moving or copying it.

### Cloud Storage

- **[AWS S3](s3-and-opteryx.md)** - Query Parquet, CSV, and JSONL files directly from Amazon S3
- **[Google Cloud Storage](gcs-and-opteryx.md)** - Access data files in GCS buckets
- **[Apache Iceberg](iceberg-and-opteryx.md)** - Query Iceberg tables with catalog support

### File Formats

- **[Execute SQL on CSV Files](execute-sql-on-csv.md)** - Query CSV files directly without loading into a database
- **[Convert CSV to Parquet](convert-csv-to-parquet.md)** - Transform file formats using SQL

## SQL Databases

Connect to relational databases and run federated queries across them.

- **[PostgreSQL](postgres-and-opteryx.md)** - Connect to Postgres databases using SQLAlchemy
- **[MySQL](mysql-and-opteryx.md)** - Query MySQL databases and join with other sources
- **[BigQuery](bigquery-and-opteryx.md)** - Access Google BigQuery tables
- **[DuckDB](duckdb-and-opteryx.md)** - Query DuckDB databases for analytics
- **[SQLite](sqlite-and-opteryx.md)** - Work with SQLite databases

## Data Analysis Tools

Integrate with popular Python data analysis libraries.

### DataFrames

- **[Pandas](pandas-and-opteryx.md)** - Query Pandas DataFrames and output results as Pandas
- **[Polars](polars-and-opteryx.md)** - High-performance DataFrame integration with Polars

### Notebooks

- **[Jupyter Notebooks](using-opteryx-with-jupyter.md)** - Interactive data exploration and visualization

## Common Use Cases

### Federated Queries

Combine data from multiple sources in a single query:

~~~python
import opteryx
from opteryx.connectors import SqlConnector, AwsS3Connector
from sqlalchemy import create_engine

# Register S3 connector
opteryx.register_store("my-bucket", AwsS3Connector)

# Register PostgreSQL
postgres_engine = create_engine("postgresql+psycopg2://user:pass@host/")
opteryx.register_store("pg", SqlConnector, remove_prefix=True, engine=postgres_engine)

# Query across S3 and Postgres
result = opteryx.query("""
    SELECT 
        s3_data.customer_id,
        s3_data.purchase_amount,
        pg_data.customer_name
    FROM my-bucket.sales AS s3_data
    JOIN pg.customers AS pg_data
    ON s3_data.customer_id = pg_data.id
""")
~~~

### Data Pipeline Integration

Use Opteryx in data pipelines:

~~~python
import opteryx
from opteryx.connectors import GcpCloudStorageConnector

# Register GCS connector
opteryx.register_store("data", GcpCloudStorageConnector)

# Read from GCS
df = opteryx.query("""
    SELECT 
        date,
        product_id,
        SUM(amount) as total_sales
    FROM data.sales
    WHERE date >= '2024-01-01'
    GROUP BY date, product_id
""").pandas()

# Continue processing with your preferred tool
df.to_csv('processed_sales.csv', index=False)
~~~

## Need Help?

- **[Discord Community](https://discord.gg/qpv2tr989x)** - Get help from the community
- **[GitHub Issues](https://github.com/mabel-dev/opteryx/issues)** - Report bugs or request features
- **[Documentation](https://opteryx.dev)** - Explore the full documentation

## Contributing

Found an issue or want to contribute a guide? Check out our [Contributing Guide](../../contributing/contributing.md).
