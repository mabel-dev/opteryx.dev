# Python Client

Opteryx provides Python bindings compliant with a subset of the [PEP 249](https://peps.python.org/pep-0249/) DBAPI specification. This allows for seamless integration into Python applications, scripts, and Jupyter notebooks, facilitating easy manipulation and querying of data.

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

Parameterized queries are essential for securing SQL statements against injection attacks. By using placeholders, you can safely incorporate user inputs into your SQL queries, preventing malicious code from being executed.

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

### Query Statistics and Messages

Opteryx provides detailed statistical data and messages about the execution of queries through the cursor object. This information can be invaluable for debugging and optimizing performance.

**Messages**

The `.messages` attribute of the cursor object provides a list of warnings and advisories generated during query processing. These messages can help you understand any issues or optimizations made by the engine:

~~~python
# Assuming cursor is already defined and used for a query
for message in cursor.messages:
    print("Message from query execution:", message)
~~~

**Statistics**

The `.stats` attribute offers detailed execution metrics. These statistics are useful for performance tuning and understanding the internal workings of the query engine.

Here’s a brief description of some key statistics:

- blobs_read: The number of data blobs the engine read from storage.
- bytes_processed: Total data processed during the query execution.
- rows_read: Rows read after applying filters and projections.
- time_planning: Time spent planning the query execution.

Here’s how you can access these statistics:

~~~python
# Assuming cursor is already defined and used for a query
stats = cursor.stats
print(f"Data processed: {stats['bytes_processed']} bytes")
print(f"Query planning time: {stats['time_planning']} seconds")
~~~

!!! note
    Not all statistics are available for every query. Some metrics depend on the specific operations performed and the data involved.

**Usage Tips**

- Debugging: Use .messages to identify potential minor issues in query execution.   
- Optimization: Review .stats to pinpoint performance bottlenecks like excessive data reads or long planning times.   
- Monitoring: Regularly check these metrics to understand the health and performance of your database interactions.   

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