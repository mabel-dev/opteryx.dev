# Statements

The following statement forms are supported.

## SELECT

Retrieve rows from zero or more relations.

~~~sql
[ <statement> UNION [ ALL ] ... ]

SELECT [ DISTINCT ] [ ON ( <columns> ) ] ] <expression> [ , ... ]
       | [ * EXCEPT ( <columns> ) ]
    FROM { <relation> | <function> | (<subquery>) } AS <alias>
    [ FOR <period> ]
    [
        [ INNER ] JOIN { <relation> | <function> | (<subquery>) } [ AS <alias> ]
            [ ON <condition> | USING ( <columns> ) ]
        | CROSS JOIN { <relation> | <function> | (<subquery>) } [ AS <alias> ]
        | LEFT [ OUTER | ANTI | SEMI ] JOIN { <relation> | <function> | (<subquery>) } [ AS <alias> ]
            [ ON <condition> | USING ( <columns> ) ]
        | RIGHT [ OUTER ] JOIN { <relation> | <function> | (<subquery>) } [ AS <alias> ]
            [ ON <condition> | USING ( <columns> ) ]
        | FULL [ OUTER ] JOIN { <relation> | <function> | (<subquery>) } [ AS <alias>  ]
            [ ON <condition> | USING ( <columns> ) ]  
   ] [ ... ]                  
 WHERE <condition> [ { AND | OR | XOR } ... ]
 GROUP BY [ ALL | <expression> [ , ... ] ]
HAVING <condition> [ { AND | OR | XOR } ... ]
 ORDER BY <expression> [ , ... ]
 LIMIT <limit>
OFFSET <offset>
~~~

### UNION class

~~~
statement UNION [ ALL ] statement
~~~

The `UNION` class appends the results of two queries together one after the other. The names and types of the resulting columns are taken from the first statement, names in the second statement are ignored and types are coerced where possible.

The default behaviour of the `UNION` class is to deduplicate rows, to return all rows, including duplicates the `ALL` modifier must be used.

### SELECT clause

~~~
SELECT [ DISTINCT [ ON (columns )]] expression [, ...]
~~~
~~~
SELECT * EXCEPT (column[, ... ])
~~~

The `SELECT` clause specifies the list of columns that will be returned by the query. While it appears first in the clause, logically the expressions here are executed after most other clauses. The `SELECT` clause can contain arbitrary expressions that transform the output, as well as aggregate functions.

The `DISTINCT` modifier is specified, only unique rows are included in the result set. In this case, each output column must be of a type that allows comparison. `DISTINCT ON ()` will perform a distinct on the specified columns and select one value for other columns. 

`EXCEPT` can be used to list columns to exclude from results.

### FROM / JOIN clauses

~~~
FROM relation [AS alias] [FOR period] [WITH (NO_CACHE, NO_PARTITION, NO_PUSH_PROJECTION, NO_PUSH_SELECTION)] [, ...] 
~~~
~~~
FROM relation [AS alias] [FOR period] [ INNER ] JOIN relation [FOR period] < USING (columns) | ON condition >
~~~ 
~~~
FROM relation [AS alias] [FOR period] LEFT [ OUTER | ANTI | SEMI ] JOIN relation [FOR period] < USING (columns) | ON condition >
~~~ 
~~~
FROM relation [AS alias] [FOR period] RIGHT [ OUTER | ANTI | SEMI ] JOIN relation [FOR period] < USING (columns) | ON condition >
~~~ 
~~~
FROM relation [AS alias] [FOR period] FULL [OUTER ] JOIN relation [FOR period]
~~~
~~~
FROM relation [AS alias] [FOR period] CROSS JOIN < relation [FOR period] | UNNEST(column) >
~~~

The `FROM` clause specifies the source of the data on which the remainder of the query should operate. Logically, the `FROM` clause is where the query starts execution. The `FROM` clause can contain a single relation, a combination of multiple relations that are joined together, or another `SELECT` query inside a subquery node.

`JOIN` clauses allow you to combine data from multiple relations. If no `JOIN` qualifier is provided, `INNER` will be used. `JOIN` qualifiers are mutually exclusive. `ON` and `USING` clauses are also mutually exclusive and can only be used with `INNER` and `LEFT` joins.

See [Joins](../joins/) for more information on `JOIN` syntax and functionality.

### FOR clause

~~~
FOR date
~~~
~~~
FOR DATES BETWEEN start AND end
~~~
~~~
FOR DATES IN range
~~~
~~~
FOR DATES SINCE start
~~~
~~~
FOR LAST count DAYS
~~~

The `FOR` clause is a non-standard clause which filters data by the date it was recorded for. When provided `FOR` clauses must directly follow the relation in a `FROM` or `JOIN` clause. If not provided `FOR TODAY` is assumed.

See [Time Travel](../adv-time-travel/) for more information on `FOR` syntax and functionality.

### WHERE clause

~~~
WHERE condition
~~~

The `WHERE` clause specifies any filters to apply to the data. This allows you to select only a subset of the data in which you are interested. Logically the `WHERE` clause is applied immediately after the `FROM` clause.

### GROUP BY / HAVING clauses

~~~
GROUP BY expression [, ...]
~~~
~~~
GROUP BY ALL
~~~
~~~
HAVING group_filter
~~~

The `GROUP BY` clause specifies which grouping columns should be used to perform any aggregations in the `SELECT` clause. If the `GROUP BY` clause is specified, the query is always an aggregate query, even if no aggregations are present in the `SELECT` clause. The `HAVING` clause specifies filters to apply to aggregated data, `HAVING` clauses require a `GROUP BY` clause.

`GROUP BY ALL` will automatically include all columns in the corresponding `SELECT` clause which do not contain aggregrations.  

### ORDER BY / LIMIT / OFFSET clauses

~~~
ORDER BY expression [ ASC | DESC ] [, ...]
~~~
~~~
OFFSET count
~~~
~~~
LIMIT count
~~~

`ORDER BY`, `LIMIT` and `OFFSET` are output modifiers. Logically they are applied at the very end of the query. The `OFFSET` clause discards initial rows from the returned set, the `LIMIT` clause restricts the amount of rows fetched, and the `ORDER BY` clause sorts the rows on the sorting criteria in either ascending or descending order.

`ORDER BY` expressions may use column numbers, however, this is not recommended for statements intended for reuse.

## EXPLAIN

Show the logical execution plan of a statement.

~~~sql
EXPLAIN [ ANALYZE ] [ FORMAT MERMAID | FORMAT TEXT ]
statement
~~~

The `EXPLAIN` clause outputs a summary of the execution plan for the query in the `SELECT` statement. The `ANALYZE` modifier is used to execute the query and return additional information about the execution of the query.

The optional `FORMAT` modifier controls the output format, `TEXT` is the default tabular representation of the plan, `MERMAID` creates a flow which can be interpretted as a [mermaid](https://mermaid.js.org/) diagram.

!!! Warning  
    The data returned by the `EXPLAIN` statement is intended for interactive usage only and the output format may change between releases. Applications should not depend on the output of the `EXPLAIN` statement.

## EXECUTE :octicons-beaker-24: 

Execute a preprated statement.

~~~sql
EXECUTE statement_name[(<parameter=value[, ...]>)]
~~~

The `EXECUTE` clause executes a prepared statement, the parameters supplied in the invocation clause are used to populate placeholders in the prepared statement. The supplied parameters must be named, for example `EXECUTE PLANETS_BY_ID (id=1)`.

## SET

Specifies the value of a variable, the variable is available to the scope of the executing query batch.

~~~sql
SET variable = value
~~~

User defined variable names must be prefixed with an 'at' symbol (`@`) and the value must be a literal value. The variable can be used within `SELECT` clauses within the same query batch. A `SET` statement without a `SELECT` statement is invalid.

System parameters can also be temporarily for a query batch and are prefixed with a dollar sign (`$`).

**Related**: `SHOW VARIABLES` and `SHOW PARAMETER`

## SHOW COLUMNS

List the columns in a relation along with their data type. Without any modifiers, `SHOW COLUMNS` only reads a single morsel of data before returning.

~~~sql
SHOW [EXTENDED] [FULL] COLUMNS
FROM relation
 FOR period
~~~

### EXTENDED modifier

Inclusion of the `EXTENDED` modifier includes summary statistics about the columns which take longer and more memory to create than the standard summary information without the modifier. The summary information varies between column types and values.

### FULL modifier

Inclusion of the `FULL` modifier uses the entire dataset in order to return complete column information, rather than just the first morsel from the dataset.

### FOR clause

~~~
FOR date
~~~
~~~
FOR DATES BETWEEN start AND end
~~~
~~~
FOR DATES IN range
~~~
~~~
FOR DATES SINCE start
~~~

The `FOR` clause is a non-standard clause which filters data by the date it was recorded for. When provided `FOR` clauses must directly follow the relation name the `FROM` clause. If not provided `FOR TODAY` is assumed.

See [Time Travel](../adv-time-travel/) for more information on `FOR` syntax and functionality.

## SHOW CREATE VIEW

Show an approximation of the SQL to create a specified relation.

~~~sql
SHOW CREATE VIEW view
~~~

Returns the SQL (including comments) which is executed when the view is accessed.

<!---

## SHOW CREATE TABLE

Show an approximation of the SQL to create a specified relation.

~~~sql
SHOW CREATE TABLE table
 FOR period
~~~

The SQL generated by this statement is unlikely to be able to be used with any SQL engine to create the table without some intervention and edits. It is intended to reduce effort to obtain this SQL, not eliminate it.

### FOR clause

~~~
FOR date
~~~
~~~
FOR DATES BETWEEN start AND end
~~~
~~~
FOR DATES IN range
~~~

The `FOR` clause is a non-standard clause which filters data by the date it was recorded for. When provided `FOR` clauses must directly follow the relation name. If not provided `FOR TODAY` is assumed.

## SHOW FUNCTIONS

List the functions and aggregators supported by the engine.

~~~sql
SHOW FUNCTIONS
LIKE pattern
~~~

### LIKE clause

~~~
LIKE pattern
~~~

A case-insensitive `LIKE` clause to filter the results to the desired subset by the function name. This does not require a left-hand operator, it will always filter by the function name.

## SHOW PARAMETER

Display the value of a given configuration setting.

~~~sql
SHOW PARAMETER parameter
~~~

## SHOW DATABASES

Display the set of configured data stores.

~~~sql
SHOW DATABASES
~~~

## SHOW VARIABLES

List the variables set in the query batch.

~~~sql
SHOW VARIABLES
LIKE pattern
~~~

### LIKE clause

~~~
LIKE pattern
~~~

A case-insensitive `LIKE` clause to filter the results to the desired subset by the variable name. This does not require a left-hand operator, it will always filter by the variable name.

**Related**: `SET`

## USE :octicons-beaker-24:  

This statement currently has no effect.

~~~sql
USE database
~~~


--->