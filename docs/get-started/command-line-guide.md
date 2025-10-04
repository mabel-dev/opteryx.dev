---
title: Opteryx Command Line Interface - CLI Usage Guide
description: Complete guide to the Opteryx CLI. Run SQL queries from the terminal in REPL or batch mode with examples and options.
---

# Command Line Interface

The Opteryx Command Line Interface (CLI) provides a terminal-based interface for executing queries. You can use it either as an interactive shell (REPL) or to execute individual queries (Batch).

Both modes require a working Python environment and Opteryx to be installed. To install Python, refer to the [Python website](https://www.python.org/). To install Opteryx follow the [quickstart](quickstart.md) guide.

## REPL (Interactive) Mode

To start Opteryx in REPL mode, execute Opteryx without providing a SQL statement:

~~~console
$ python -m opteryx
~~~

You will then be presented with a prompt similar to the following:


~~~
Opteryx version 0.10.0
  Enter '.help' for usage hints
  Enter '.exit' to exit this program

opteryx> 
~~~


Once the CLI has been opened, the `opteryx>` prompt indicates that you can enter a SQL statement. Hitting enter will execute the statement, and the results will be displayed in a table in the terminal.

The CLI supports all of Opteryx's SQL syntax.

### Special Commands (Dot Commands)

In addition to SQL syntax, special dot commands may be entered that are specific to the CLI client. To use one of these commands, begin the line with a period/full stop (`.`) immediately followed by the name of the command you wish to execute. For example, `.help` will display the full set of supported Dot Commands.

## Batch Mode

The Opteryx Command Line Interface (CLI) provides a terminal-based interface for running queries. The CLI is a Python script that is usually run by invoking Python.

### Simple Query Example

Execute a simple query and see results in the console:

~~~console
$ python -m opteryx "SELECT 'Hello, Opteryx!' AS greeting"
~~~

### Querying Files

To query individual files, use the file path in place of the table name in your SQL query. The file path must be prefixed with a dollar sign (`$`).

For example, to query a local CSV file:

~~~console
$ python -m opteryx "SELECT * FROM \$data/sales.csv"
~~~

To query and save results to a different file:

~~~console
$ python -m opteryx --o 'results.csv' "SELECT * FROM \$data/sales.csv WHERE amount > 100"
~~~

!!! Note
    CLI usage may have character escaping requirements, such as a backslash before dollar signs and backticks.

Querying individual files requires the relative path in place of the relation/table name in the query. This usually requires putting the filename in quotes, as filenames often contain illegal characters.

### Command Line Options

~~~console
Usage: python -m opteryx [OPTIONS] [SQL] 

--o <target>  Where to output the results. [default: console]
--no-color    Do not colorize console output. 
--help        Show the full help details.          
~~~

To see the full help and usage details for the CLI, use the `--help` option:

~~~console
$ python -m opteryx --help
~~~

### Output Formats

Batch mode can be used to save the results of a SQL statement to a file. The format of the file is determined by the provided file extension. The following formats are supported:

Extension | Format
--------- | -----------
csv       | Comma Separated Values
jsonl     | JSON Lines
md        | Markdown Table
parquet   | Apache Parquet
