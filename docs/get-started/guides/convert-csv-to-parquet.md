---
title: Convert CSV to Parquet with Opteryx - Fast File Format Conversion
description: Convert CSV files to Parquet format using Opteryx command line tool. Support for multiple file formats including JSONL, Avro, and ORC conversion.
---

# Converting CSV to Parquet using Opteryx

You can use Opteryx to convert CSV files to Parquet files from the command line.

This feature can also be used to convert between all of the file types Opteryx supports. Input file types include Parquet, Avro, JSONL, and ORC. Output file types include Parquet, JSONL, and CSV.

**Command Line**

To convert a CSV file to a Parquet file, use the following command:

~~~ console
$ python -m opteryx --o 'taxi_trips.parquet' "SELECT * FROM 'taxi_trips.csv';"
~~~

!!! Note
    The terminal may require some special characters to be escaped.

## Advanced Examples

### Convert with Filtering

Apply transformations and filters during conversion:

~~~ console
$ python -m opteryx --o 'filtered_trips.parquet' "SELECT * FROM 'taxi_trips.csv' WHERE fare_amount > 10;"
~~~

### Aggregate and Convert

Create aggregated output files:

~~~ console
$ python -m opteryx --o 'monthly_sales.parquet' "
    SELECT 
        DATE_TRUNC('month', date) as month,
        product_category,
        SUM(amount) as total_sales
    FROM 'sales_data.csv'
    GROUP BY month, product_category
"
~~~

### Convert Multiple File Formats

Convert JSONL to Parquet:

~~~ console
$ python -m opteryx --o 'events.parquet' "SELECT * FROM 'logs.jsonl';"
~~~

Convert Parquet to CSV:

~~~ console
$ python -m opteryx --o 'export.csv' "SELECT * FROM 'data.parquet';"
~~~

## Supported Conversions

**Input Formats:**
- Parquet (`.parquet`)
- CSV (`.csv`)
- Tab-delimited (`.tsv`)
- JSONL (`.jsonl`)
- JSONL Zstandard compressed (`.zstd`)
- Avro (`.avro`)
- ORC (`.orc`)
- Feather/Arrow (`.arrow`)
- Arrow IPC (`.ipc`)
- Excel (`.xlsx`)
- Apache Vortex (`.vortex`)

**Output Formats:**
- Parquet (`.parquet`) - Recommended for analytics
- JSONL (`.jsonl`) - Line-delimited JSON
- CSV (`.csv`) - Comma-separated values

!!! note
    - ORC is not supported on Windows environments
    - CSV and TSV support is limited and not recommended beyond trivial use cases
    - Avro and Vortex are not recommended for performance-sensitive contexts

## Performance Tips

- **Use Parquet for large datasets** - Parquet is columnar and compressed, making it ideal for analytics
- **Apply filters during conversion** - Reduce output file size by filtering unnecessary data
- **Partition large outputs** - For very large datasets, consider partitioning by date or category

## Related Guides

- [Execute SQL on CSV Files](execute-sql-on-csv.md) - Query CSV files without conversion
- [Query AWS S3](s3-and-opteryx.md) - Convert files in cloud storage
- [Using Opteryx with Jupyter](using-opteryx-with-jupyter.md) - Interactive file processing
- [Pandas Integration](pandas-and-opteryx.md) - Convert to DataFrames for analysis

