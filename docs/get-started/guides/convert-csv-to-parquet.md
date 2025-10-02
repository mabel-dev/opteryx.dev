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
