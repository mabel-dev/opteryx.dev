# Client Connectivity Overview

Opteryx supports two methods of invocation; as an importable Python library and as a command line tool.

## Python Embedded

Opteryx is an embeddable package into Python applications, scripts and Notebooks which implements a partial Python DBAPI ([PEP 249](https://peps.python.org/pep-0249/)) interface.

~~~python
import opteryx

result = opteryx.query('SELECT * FROM $planets')
rows = cur.fetchall()
~~~

The results of the query are availble via the cursor using `fetchone()` that returns a tuple, `fetchmany()` and `fetchall()` that return generators of tuples, `arrow()` that returns an [Arrow Table](https://arrow.apache.org/docs/python/generated/pyarrow.Table.html#pyarrow.Table), or `to_df()` that returns a [pandas DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)

## Command Line Interface

Opteryx Command Line Interface (CLI) provides a terminal-based interactive shell for running queries. The CLI is a Python script usually run by invoking Python, like this:

~~~bash
python -m opteryx --o 'planets.csv' "SELECT * FROM \$planets"
~~~

!!! Note
    CLI usage may have character escaping requirements, such as a backslash before dollar signs and backticks.

Querying individual files quires the relative path in place of the relation/table name in the query, this usually requires the filename to be put in quotes as filenames often contain illegal characters.

Abridged usage guidance is available below:

~~~
Usage: python -m opteryx [OPTIONS] [SQL] 

--ast         Display the AST for the query.
--o <target>  Where to output the results. [default: console]
--no-color    Do not colorize console output. 
--help        Show the full help details.          
~~~

To see the full help and usage details for the CLI use the `--help` option:

~~~bash
python -m opteryx --help
~~~

Supported output locations are the **console**, a **parquet** file, a **csv** file, or a **jsonl** file.