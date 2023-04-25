# Converting CSV to Parquet using Opteryx

You can use Opteryx to convert CSV files to Parquet files from the command line.

This feature can also be used to convert between all of the file types Opteryx supports. Input file types include Parquet, Avro, JSONL, and ORC. Output file types include Parquet, JSONL, and CSV.

**Command Line**

To convert a CSV file to a Parquet file, use the following command:

~~~ console
$ opteryx --taxi_trips.parquet "SELECT * FROM 'taxi_trips.csv';"
~~~

!!! Note
    The terminal may require some special characters to be escaped.
