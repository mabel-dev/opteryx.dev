# Client Connectivity Overview

Opteryx supports two methods of invocation; as a Python library (embedded) and as a command line tool.

## Python Embedded

Opteryx is an embeddable package into Python applications, scripts and Notebooks and supports parts of the Python DBAPI ([PEP 249](https://peps.python.org/pep-0249/)) interface.

~~~python
import opteryx

conn = opteryx.connection()
curr = conn.cursor()
curr.execute('SELECT * FROM $planets')
rows = curr.fetchall()
~~~

The results of the query are availble via the Cursor. The Cursor is an [orso DataFrame](https://github.com/mabel-dev/orso) and support accessing results using the Cursor as an iterator, using `fetchone()`, `fetchmany()` and `fetchall()`, and using format conversion routines such as `arrow()` which returns an [Arrow Table](https://arrow.apache.org/docs/python/generated/pyarrow.Table.html#pyarrow.Table), and `pandas()` which returns a [pandas DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)

## Command Line Interface

Opteryx Command Line Interface (CLI) provides a terminal-based interface for running queries. The CLI is a Python script usually run by invoking Python, like this:

~~~console
$ python -m opteryx --o 'planets.csv' "SELECT * FROM \$planets"
~~~

!!! Note
    CLI usage may have character escaping requirements, such as a backslash before dollar signs and backticks.

Querying individual files requires the relative path in place of the relation/table name in the query, this usually requires the filename to be put in quotes as filenames often contain illegal characters.

Abridged usage guidance is available below:

~~~console
Usage: python -m opteryx [OPTIONS] [SQL] 

--o <target>  Where to output the results. [default: console]
--no-color    Do not colorize console output. 
--help        Show the full help details.          
~~~

To see the full help and usage details for the CLI use the `--help` option:

~~~console
$ python -m opteryx --help
~~~

Supported output locations include the **console**, a **parquet** file, a **csv** file, or a **jsonl** file.