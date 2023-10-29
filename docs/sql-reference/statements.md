# Statements

The following statement forms are supported.

## SELECT

Retrieve rows from zero or more relations.

~~~sql
  WITH <cte> AS <statement> [, ..] 
SELECT [ DISTINCT [ ON (<columns>) ] ] <expression> [, ..]
  FROM <relation> [AS <alias>]
   FOR <period> [ WITH (NO_CACHE|NO_PARTITION|NO_PUSH_PROJECTION|NO_PUSH_SELECTION) ]
       [ INNER ] JOIN <relation> | <function> | (<subquery>)
       CROSS JOIN <relation> | <function> | (<subquery>)
       LEFT [ OUTER ] JOIN <relation> | <function> | (<subquery>)
       RIGHT [ OUTER ] JOIN <relation> | <function> | (<subquery>)
       FULL [ OUTER ] JOIN <relation> | <function> | (<subquery>)
                      ON <expression>
                      USING (<columns>)
 WHERE <expression> [ AND | OR | XOR .. ]
 GROUP BY 
       HAVING <expression> [ AND | OR | XOR .. ]
 ORDER BY <expression> [, ..]
OFFSET <offset>
 LIMIT <limit>
~~~

### WITH clause

~~~
WITH <cte> AS <statement> [, ..] 
~~~

The `WITH` clause, known as a _Common Table Expression_, or CTE, is used to define a temporary view which can be referenced within `FROM` and `JOIN` clauses. The statement in the CTE supports the full syntax for `SELECT` statements.

Unlike some platforms, Opteryx handles CTEs by inserting them as subqueries into the main statement and not by executing them and referencing the result.


### SELECT clause

~~~
SELECT [ DISTINCT [ ON (columns )]] expression [, ...]
~~~

The `SELECT` clause specifies the list of columns that will be returned by the query. While it appears first in the clause, logically the expressions here are executed after most other clauses. The `SELECT` clause can contain arbitrary expressions that transform the output, as well as aggregate functions.

The `DISTINCT` modifier is specified, only unique rows are included in the result set. In this case, each output column must be of a type that allows comparison. `DISTINCT ON ()` will perform a distinct on the specified columns and select one value for other columns. 

### FROM / JOIN clauses

~~~
FROM relation [AS alias] [FOR period] [WITH (NO_CACHE, NO_PARTITION, NO_PUSH_PROJECTION, NO_PUSH_SELECTION)] [, ...] 
~~~
~~~
FROM relation [AS alias] [FOR period] [ INNER ] JOIN relation [FOR period] < USING (columns) | ON condition >
~~~ 
~~~
FROM relation [AS alias] [FOR period] LEFT [ OUTER ] JOIN relation [FOR period] < USING (columns) | ON condition >
~~~ 
~~~
FROM relation [AS alias] [FOR period] < RIGHT | FULL > [OUTER ] JOIN relation [FOR period]
~~~
~~~
FROM relation [AS alias] [FOR period] CROSS JOIN < relation [FOR period] | UNNEST(column) >
~~~

The `FROM` clause specifies the source of the data on which the remainder of the query should operate. Logically, the `FROM` clause is where the query starts execution. The `FROM` clause can contain a single relation, a combination of multiple relations that are joined together, or another `SELECT` query inside a subquery node.

`JOIN` clauses allow you to combine data from multiple relations. If no `JOIN` qualifier is provided, `INNER` will be used. `JOIN` qualifiers are mutually exclusive. `ON` and `USING` clauses are also mutually exclusive and can only be used with `INNER` and `LEFT` joins.

See [Joins](../joins/) for more information on `JOIN` syntax and functionality.

Hints can be provided as part of the statement to direct the query planner and executor to make decisions. Relation hints are declared as `WITH` statements following a relation in the `FROM` and `JOIN` clauses, for example `FROM $astronauts WITH (NO_CACHE)`. Reconised hints are:

Hint               | Effect                         
------------------ | -------------------------------------------------
NO_CACHE           | Ignores any cache configuration 
NO_PARTITION       | Do not use partition configuration when reading
NO_PUSH_PROJECTION | Do not attempt to prune columns when reading 
NO_PUSH_SELECTION  | Do not use the source system to prefilter rows

!!! Note  
    Hints are not guaranteed to be followed, the query planner and executor may ignore hints in specific circumstances.

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
HAVING group_filter
~~~

The `GROUP BY` clause specifies which grouping columns should be used to perform any aggregations in the `SELECT` clause. If the `GROUP BY` clause is specified, the query is always an aggregate query, even if no aggregations are present in the `SELECT` clause. The `HAVING` clause specifies filters to apply to aggregated data, `HAVING` clauses require a `GROUP BY` clause.

`GROUP BY` expressions may use column numbers, however, this is not recommended for statements intended for reuse. 

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
EXPLAIN
statement
~~~

The `EXPLAIN` clause outputs a summary of the execution plan for the query in the `SELECT` statement.

!!! Warning  
    The data returned by the `EXPLAIN` statement is intended for interactive usage only and the output format may change between releases. Applications should not depend on the output of the `EXPLAIN` statement.

## EXECUTE :octicons-beaker-24: 

Execute a preprated statement.

~~~sql
EXECUTE statement_name[(<parameter[, ...]>)]
~~~

The `EXECUTE` clause executes a prepared statement, the parameters supplied in the invocation clause are used to populate placeholders in the prepared statement.

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
LIKE pattern
 FOR period
~~~

### EXTENDED modifier

Inclusion of the `EXTENDED` modifier includes summary statistics about the columns which take longer and more memory to create than the standard summary information without the modifier. The summary information varies between column types and values.

### FULL modifier

Inclusion of the `FULL` modifier uses the entire dataset in order to return complete column information, rather than just the first morsel from the dataset.

### LIKE clause

~~~
LIKE pattern
~~~

A case-insensitive `LIKE` clause to filter the results to the desired subset by the column name. This does not require a left-hand operator, it will always filter by the column name.

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

The `FOR` clause is a non-standard clause which filters data by the date it was recorded for. When provided `FOR` clauses must directly follow the relation name the `FROM` clause. If not provided `FOR TODAY` is assumed.

See [Time Travel](../adv-time-travel/) for more information on `FOR` syntax and functionality.

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