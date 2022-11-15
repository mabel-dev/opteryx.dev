# Expressions

An expression is a combination of values, operators and functions. Expressions are highly composable, and range from very simple to arbitrarily complex. They can be found in many different parts of SQL statements. In this section, we provide the different types of operators that can be used within expressions.

## Logical Operators

Logical Operators are used within Expressions to express how predicates combine.

The following logical operators are available: `NOT`, `AND`, `OR`, and `XOR`.

| a      | b     | a `AND` b | a `OR` b | a `XOR` b | `NOT` a |
| :----: | :---: | :-------: | :------: | :-------: | :-----: |
| true   | true  | true      | true     | false     | false   |
| true   | false | false     | true     | true      | false   |
| false  | false | false     | false    | false     | true    |
| _null_ | true  | _null_    | _null_   | _null_    | _null_  |
| _null_ | false | _null_    | _null_   | _null_    | _null_  |

The operators `AND`, `OR`, and `XOR` are commutative, that is, you can switch the left and right operand without affecting the result.

## Comparison Operators

Comparison Operators are used within Expressions to compare values, usually involving comparing a field within the datasets against a literal value - although comparisons can be used against two fields, or two literals.

Usually when one of the values involved in the comparison is `null`, the result is `null`.

Operator     | Description                   
:----------- | :-----------------------------
`=`          | equal to               
`<>`         | not equal to  
`<`          | less than                     
`>`          | greater than                
`<=`         | less than or equal to        
`>=`         | greater than or equal to                  
`IN`         | value in list              
`NOT IN`     | value not in list            
`LIKE`       | pattern match           
`NOT LIKE`   | inverse results of `LIKE`         
`ILIKE`      | case-insensitive pattern match 
`NOT ILIKE`  | inverse results of `ILIKE`     
`~`          | regular expression match (also `SIMILAR TO`)     
`!~`         | inverse results of `~` (also `NOT SIMILAR TO`)
`~*`         | case insensitive regular expression match
`!~*`        | inverse results of `~*`
`IS`         | special comparison for non-values `true`, `false` and `null`

## Other Comparisons

### BETWEEN

Predicate               | Description
----------------------- | ---------------------------------
`a BETWEEN x AND y`     | equivalent to `a >= x AND a <= y`
`a NOT BETWEEN x AND y` | equivalent to `a < x OR a > y`

!!! Warning  
    Using `BETWEEN` with other predicates, especially when used with an `AND` conjunction, can cause the query parser to fail. 

### CASE

The standard SQL CASE expression has two forms. The “simple” form searches each value expression from left to right until it finds one that equals expression:

~~~sql
CASE expression
    WHEN value THEN result
    [ WHEN ... ]
    [ ELSE result ]
END
~~~

The result for the matching value is returned. If no match is found, the result from the ELSE clause is returned if it exists, otherwise null is returned. Example:

~~~sql
SELECT a,
       CASE a
           WHEN 1 THEN 'one'
           WHEN 2 THEN 'two'
           ELSE 'many'
       END
~~~

The “searched” form evaluates each boolean condition from left to right until one is true and returns the matching result:

~~~sql
CASE
    WHEN condition THEN result
    [ WHEN ... ]
    [ ELSE result ]
END
~~~

If no conditions are true, the result from the ELSE clause is returned if it exists, otherwise null is returned. Example:

~~~sql
SELECT a, b,
       CASE
           WHEN a = 1 THEN 'aaa'
           WHEN b = 2 THEN 'bbb'
           ELSE 'ccc'
       END
~~~

## Subqueries

The `IN` operator can reference a sub query, this sub query cannot include a temporal clause (`FOR`), but otherwise the full syntax for `SELECT` queries are supported.

For example, to find the planets without any satellites.

~~~sql
SELECT name
  FROM $planets
 WHERE id NOT IN (
     SELECT DISTINCT planetId
       FROM $satellites
    );
~~~
