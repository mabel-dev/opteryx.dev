# Convert CSV to Parquet using Opteryx

You can use Opteryx to convert CSV files to parquet files on the command line.

This feature can also be used for all of the file typles Opteryx supports including parquet, avro, jsonl and orc as input files, and parquet, jsonl and CSV as outputs.

**Command Line**

~~~ console
$ opteryx --taxi_trips.parquet "SELECT * FROM 'taxi_trips.csv';"
~~~

!!! Note
    The terminal may require some special characters to be escaped
