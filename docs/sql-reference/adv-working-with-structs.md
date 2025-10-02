# Working with Structs

A struct is a collection of zero or more key, value pairs. Keys must be `VARCHAR`, values can be different types.

`STRUCT` as a datatype is being deprecated in favour of treating `BLOB` and `VARCHAR` columns containing JSON strings as implicit `STRUCT` columns. All features available for explicitly typed `STRUCT` columns are available on JSON-formatted columns.

## Actions

### Casting

Structs can be cast from JSON strings:

~~~sql
CAST(json_string AS STRUCT)
~~~

Note: `VARCHAR` and `BLOB` columns containing JSON-formatted strings automatically support struct operations without explicit casting.

### Create

Structs are typically created from JSON data or can be constructed from columns:

~~~sql
-- JSON string that will be treated as struct
SELECT '{"name": "Alice", "age": 30}'::STRUCT;
~~~

### Reading

#### Subscript Notation

~~~sql
struct[key]
~~~

Values within structs can be accessed by key using subscript notation, putting the key in single quotes in square brackets following the struct.

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

#### Arrow Operator

~~~sql
struct -> key
~~~

Returns the value for the specified key from the struct.

Example:

~~~sql
SELECT birth_place -> 'town'
  FROM $astronauts;
~~~

#### Arrow Text Operator

~~~sql
struct ->> key
~~~

Returns the value for the specified key from the struct, casting non-null values to `VARCHAR`.

Example:

~~~sql
SELECT birth_place ->> 'town'
  FROM $astronauts;
~~~

#### Key Existence

~~~sql
struct @? key
~~~

Returns `true` if the struct contains the specified key.

Example:

~~~sql
SELECT *
  FROM $astronauts
 WHERE birth_place @? 'country';
~~~

#### Get Keys

~~~sql
JSONB_OBJECT_KEYS(struct)
~~~

Returns an array of all keys in the struct.

Example:

~~~sql
SELECT JSONB_OBJECT_KEYS(birth_place)
  FROM $astronauts;
~~~

#### Alias Function

~~~sql
GET(struct, key)
~~~

Alias for the `->` operator.

### Comparing

Structs can be compared for equality:

~~~sql
SELECT *
  FROM table1
 WHERE struct_column = '{"key": "value"}';
~~~

### Searching

~~~sql
SEARCH(struct, value)
~~~

All values in a struct can be searched for a given value using the `SEARCH` function.

Example:

~~~sql
SELECT name,
       SEARCH(birth_place, 'Italy')
  FROM $astronauts;
~~~

Note: `SEARCH` does not match struct keys, only values.

## Limitations

Structs have the following limitations

- Subscript references (the bit in square brackets) must be in single quotes only

!!! Note  
    Some restrictions may be resolved by the query optimizer, for example, Projection Pushdown may remove struct columns as part of optimization. However, you should not rely on the optimizer to take any particular action.