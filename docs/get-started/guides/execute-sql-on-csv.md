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
