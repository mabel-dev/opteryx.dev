# Execute SQL on CSV files using Opteryx

You can use Opteryx to execute SQL queries on CSV files. This is as simple as replacing the table name in a query with the location of the CSV file.

This feature can also be used to query all of the file typles Opteryx supports including parquet, avro, jsonl and orc.

Querying CSV files is supported in both the CLI and Python APIs.

**Command Line**

~~~ console
$ opteryx "SELECT * FROM 'taxi_trips.csv';"
~~~

!!! Note
    The terminal may require some special characters to be escaped

**Python**

~~~python
import opteryx

taxi_trips = opteryx.query("SELECT * FROM 'taxi_trips.csv';")
print(taxi_trips)
~~~

The full power of SQL is available, including joining CSV files with other files.
