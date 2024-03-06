# Working with Structs

A struct is a collection of zero or more key, value pairs. Keys must be `VARCHAR`, values can be different types.

## Actions

### Construct

~~~
STRUCT(json string)
~~~

### Reading

~~~
struct[key]
~~~

Values within structs can be accessed by key using subscript notation, putting the key in square brackets following the struct.

Example:

~~~sql
SELECT birth_place['town']
  FROM $astronauts;
~~~

Struct values can be treated the same as other identifiers and, for example, used within `SELECT`, `WHERE` and `GROUP BY` clauses:

~~~sql
SELECT birth_place['town'], COUNT(*)
  FROM $astronauts
 WHERE birth_place['state'] IS NOT NULL
 GROUP BY birth_place['town'];
~~~

:octicons-beaker-24: **Beta Functionality**
~~~
struct -> key
~~~

~~~
struct ->> key
~~~

Values within structs can be accessed by key using Accessor notation, support is limited.

### Searching

~~~
`SEARCH(struct, value)`
~~~

All values in a struct can be searched for a given value using the `SEARCH` function.

Example:

~~~sql
SELECT name,
       SEARCH(birth_place, 'Italy')
  FROM $astronauts;
~~~

## Limitations

Structs have the following limitations

- Statements cannot `ORDER BY` a struct column
- Statements cannot contain `DISTINCT` and `JOIN` when the relations include struct columns
- Structs cannot be used in comparisons, however, their component values can be
- Subscript references (the bit in square brackets) must be in single quotes only

!!! Note  
    Some restrictions may be resolved by the query optimizer, for example, Projection Pushdown may remove struct columns as part of optimization. However, you should not rely on the optimizer to take any particular action.