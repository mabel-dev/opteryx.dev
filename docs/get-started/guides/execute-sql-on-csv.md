---
title: Execute SQL Queries on CSV Files - Query CSV with Opteryx
description: Run SQL queries directly on CSV files using Opteryx. No database required - query CSV, Parquet, JSONL and other file formats with standard SQL.
---

# Executing SQL Queries on CSV Files with Opteryx

You can use Opteryx to execute SQL queries on CSV files. Simply replace the table name in a query with the location of the CSV file.

This feature can also be used to query all of the file types Opteryx supports, including Parquet, Avro, JSONL, and ORC.

Querying CSV files is supported in both the CLI and Python APIs.

**Command Line**

To execute an SQL query on a CSV file using the CLI, use the following command:

~~~ console
$ opteryx "SELECT * FROM 'taxi_trips.csv';"
~~~

!!! Note
    The terminal may require some special characters to be escaped.

**Python**

To execute an SQL query on a CSV file using the Python API, use the following code:

~~~python
import opteryx

taxi_trips = opteryx.query("SELECT * FROM 'taxi_trips.csv';")
print(taxi_trips)
~~~

The full power of SQL is available, including the ability to join CSV files with other files.

## Advanced Examples

### Filtering and Aggregation

~~~python
import opteryx

# Aggregate data from CSV
result = opteryx.query("""
    SELECT 
        pickup_borough,
        COUNT(*) as trip_count,
        AVG(fare_amount) as avg_fare
    FROM 'taxi_trips.csv'
    WHERE trip_distance > 5
    GROUP BY pickup_borough
    ORDER BY trip_count DESC
""")

print(result)
~~~

### Joining Multiple CSV Files

~~~python
import opteryx

# Join customer data with orders
result = opteryx.query("""
    SELECT 
        c.customer_name,
        o.order_id,
        o.order_total
    FROM 'customers.csv' AS c
    JOIN 'orders.csv' AS o
    ON c.customer_id = o.customer_id
    WHERE o.order_date >= '2024-01-01'
""")

print(result.head())
~~~

### Querying Multiple Files

You can query multiple CSV files by running separate queries or by combining them with UNION:

~~~python
import opteryx

# Combine multiple CSV files with UNION
result = opteryx.query("""
    SELECT * FROM 'sales_january.csv'
    UNION ALL
    SELECT * FROM 'sales_february.csv'
    UNION ALL
    SELECT * FROM 'sales_march.csv'
""")
~~~

## Supported File Formats

In addition to CSV, Opteryx supports:
- **Parquet** (`.parquet`) - Columnar format, best for large datasets
- **JSONL** (`.jsonl`) - JSON Lines format
- **Avro** (`.avro`) - Binary format with schema
- **ORC** (`.orc`) - Optimized Row Columnar format

## Related Guides

- [Convert CSV to Parquet](convert-csv-to-parquet.md) - Transform file formats for better performance
- [Query AWS S3](s3-and-opteryx.md) - Query CSV files in cloud storage
- [Query Google Cloud Storage](gcs-and-opteryx.md) - Access CSV files in GCS
- [Pandas Integration](pandas-and-opteryx.md) - Convert results to Pandas DataFrames

