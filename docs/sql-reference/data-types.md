# Data Types

The engine supports a reduced set of types compared to full DBMS platforms.

## Types

Name        | Description
----------- | --------------
`ARRAY`     | A list of items of the same type
`BOOLEAN`   | Logical boolean (True/False).
`BLOB` :octicons-star-16:     | Variable-length binary data
`DOUBLE`    | floating point number
`INTEGER`   | Whole number
`DECIMAL` :octicons-star-16:  | Fixed-point number with specified precision
`VARCHAR`   | Variable-length character string
`STRUCT` :octicons-star-16:   | A dictionary of multiple named values, where each key is a string, but the value can be a different type for each key.
`DATE`      | The date component of a TIMESTAMP
`TIME` :octicons-star-16: | The time component of a TIMESTAMP
`TIMESTAMP` | Combination of date and time.
`INTERVAL` :octicons-star-16: | The difference between two TIMESTAMP values

!!! Note  
    Types marked with :octicons-star-16: (DECIMAL, TIME, STRUCT, and INTERVAL) have limited support.

## Casting

### Functions

Values can be cast using the `CAST` function, its form is `CAST(any AS type)`. Where values are incompatible, an error will be thrown, to avoid errors `TRY_CAST` (or `SAFE_CAST`) can be used instead which will return `null` instead of error.

### Type Hints

**Intervals**

Intervals require definition by type hints, using the type name before providing a literal description of the value.

~~~
INTERVAL 'value' unit
~~~

Where unit can be 'Year', 'Month', 'Day', 'Hour', 'Minute' or 'Second'.

Example:
~~~sql
SELECT INTERVAL '1' YEAR
~~~

**Other**

`BOOLEAN`, `DOUBLE`, `INTEGER` and `TIMESTAMP` also support 'type hint' notation (e.g. `SELECT TIMESTAMP '2022-01-01';`) to perform casting.

`BLOB` supports `b` prefix notation (e.g. `b'string'`)

### Type Annotations

Some types support type annotations in the form `<value>::<type>`, for example `1::double` is equivalent to `1.0`.

### Byte Strings

`b` prefixes can be used to mark string literals as byte strings. For example `b'abc'` is equivalent to `blob('abc')`.

## Coercion

### Timestamps & Dates

Literal values in quotes may be interpreted as a `TIMESTAMP` or `DATE` when they match a valid date in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html)  format (e.g. `YYYY-MM-DD` and `YYYY-MM-DD HH:MM`). The value will be coerced to a `DATE` if there is no time component, otherwise it will be coerced to a `TIMESTAMP`. 

All `TIMESTAMP` and values read from datasets are coerced to nanosecond precision timestamps.

The default precision for `TIMESTAMP` is milliseconds, values not in this precision may be converted to this precision as handled internally.

### Numbers

Hex literals can be provided using `0x` prefix, for example `0xc0ffee` is handled as the integer `12648430`.

Numeric literals may contain underscores (`_`) which are helpful to improve the readability of long numbers, e.g. `1_000_000`.

### Structs

`VARCHAR` and `BLOB` columns containing JSON formatted strings support `STRUCT` accessors and functions. 
