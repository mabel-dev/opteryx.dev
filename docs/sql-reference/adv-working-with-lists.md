# Working with Arrays

An Array is an ordered collection of zero or more `VARCHAR` values.

## Actions

### Casting

~~~
CAST(column AS ARRAY<element_type>)
~~~

### Construct

~~~
SPLIT(string)
~~~

### Accessing

~~~
list[index]
~~~

### Testing

#### ANY (comparision)

~~~
value <operator> ANY (column)
~~~

The `ANY` function is used to apply a filter to each item in an array, and returns `True` if any item in the array matches the condition.

~~~sql
SELECT * 
  FROM $astronauts
 WHERE 'Apollo 11' = ANY(missions);
~~~

`ANY` supports the following operators: `=`, `!=`, `>`, `<`, `>=`, and `<=`. 

#### ANY (similarity)

~~~
value column <operator> ANY (patterns)
~~~

The `ANY` modifier is used to perform a similarity search against all of the items in an array for each item in an array, and returns `True` is any item in the array matches the pattern.

~~~sql
SELECT *
  FROM $astronauts
 WHERE missions LIKE ANY ('Mercury%', 'Gemini%', 'Apollo%')
~~~

`ANY` supports the following operators: `LIKE`, `NOT LIKE`, `ILIKE`, `NOT ILIKE`

#### ALL

~~~
value <operator> ALL(column)
~~~

The `ALL` function is used to apply a filter to each item in an array, and returns `True` if all items in the array matches the condition.

!!! Note
    `ALL` currently supports a subset of operators: `=`, `!=`. 

#### SEARCH

~~~sql
SELECT *
  FROM $astronauts
 WHERE Search(missions, 'Apollo 11')
~~~

#### IN

The `IN` operator allows a column to be tested against a list of values.

~~~sql
SELECT *
  FROM $planets
 WHERE name IN ('Earth', 'Mars')
~~~

#### IN UNNEST

The combination of `IN UNNEST` allows a value to be tested for containment in a column.

~~~sql
SELECT *
  FROM $astronauts
 WHERE 'Apollo 11' IN UNNEST(missions)
~~~

#### Accessors

~~~
Array @? Array
~~~

### Transforms

~~~
SORT
~~~

## Converting Lists to Relations

### Using `UNNEST`

`UNNEST` allows you to create a single column table either as a list of literals, or from a column of LIST type in a dataset.

~~~sql
SELECT * 
  FROM UNNEST((True, False)) AS Booleans;
~~~

## Limitations

Lists have the following limitations

- Statements cannot `ORDER BY` a list column
- Statements cannot contain `DISTINCT` and `JOIN` when the relations include list columns
- Lists cannot be used in comparisons

!!! Note
    Some restrictions may be resolved by the query optimizer, for example, Projection Pushdown may remove list columns as part of optimization. However, you should not rely on the optimizer to take any particular action.