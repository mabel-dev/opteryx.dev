# Python Client

Opteryx offers Python bindings compliant with a subset of the [PEP 249](https://peps.python.org/pep-0249/) DBAPI specification, allowing integration into Python applications, scripts, and Jupyter notebooks.

### Basic Usage

This section demonstrates how to establish a connection to Opteryx, execute a query, and fetch results.

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

### Using Parameterized Queries

Parameterized queries help mitigate SQL injection risks by safely incorporating user input into SQL statements.

~~~python
import opteryx

# Establish a connection
conn = opteryx.connect()
# Create a cursor object
cursor = conn.cursor()

# Execute a SQL query
cursor.execute("SELECT * FROM $planets WHERE id = :user_provided_id;",
    { "user_provided_id": 1 }
    )

# Fetch all rows
rows = cursor.fetchall()
~~~

### Handling Query Results

Opteryx returns query results as [Orso DataFrames](https://github.com/mabel-dev/orso) accessible through the cursor. You can interact with the results in multiple ways:

- **Iteration**: Loop over the cursor directly.
- **Fetching Methods**: Utilize `fetchone()`, `fetchmany(size)`, and `fetchall()` for specific result sets.
- **Conversion Routines**:
    - `arrow()` for an [Arrow Table](https://arrow.apache.org/docs/python/generated/pyarrow.Table.html#pyarrow.Table)
    - `pandas()` for a [pandas DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
    - `polars()` for a [Polars DataFrame](https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/index.html)

## Simplified Short-Form API

For convenience, Opteryx provides a streamlined API that abstracts connection and cursor creation, suitable for quick queries.

### Basic Short-Form Usage

Execute a SQL query and immediately fetch all results:

~~~python
import opteryx

# Execute a SQL query and get the results
cursor = opteryx.query("SELECT * FROM $planets;").fetchall()
~~~

### Parameterized Short-Form Usage

~~~python
import opteryx

# Execute a SQL query and get a cursor
cursor = opteryx.query(
    "SELECT * FROM $planets WHERE id = :user_provided_id;",
    { "user_provided_id": 1 }
    ).fetchall()
~~~