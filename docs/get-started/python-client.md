# Python Client

## Python DBAPI API

Opteryx can be embedded into Python applications, scripts, and notebooks. It supports a subset of the Python DBAPI ([PEP 249](https://peps.python.org/pep-0249/)) interface.

### Usage

~~~python
import opteryx

# Establish a connection
conn = opteryx.connect()
# Create a cursor object
cursor = conn.cursor()

# Execute a SQL query
cursor.execute("SELECT * FROM $planets;")

# Fetch all rows
rows = cursor.fetchall()
~~~

### Query Results

Query results can be accessed through the Cursor, which is an [Orso DataFrame](https://github.com/mabel-dev/orso). You can retrieve data in several ways:

- Iterating through the Cursor
- Using `fetchone()`, `fetchmany()`, and `fetchall()` methods
- Format conversion routines:
    - `arrow()` returns an [Arrow Table](https://arrow.apache.org/docs/python/generated/pyarrow.Table.html#pyarrow.Table)
    - `pandas()` returns a [pandas DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
    - `polars()` returns a [Polars DataFrame](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/index.html)

## Short Form API

Opteryx also provides a simplified, short-form, API that assumes default values for creating the Connection and Cursor objects.

### Usage

~~~python
import opteryx

# Execute a SQL query and get a cursor
cursor = opteryx.query("SELECT * FROM $planets;")

# Fetch all rows
rows = cursor.fetchall()
~~~
