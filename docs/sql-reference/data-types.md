# Data Types

The engine supports a reduced set of types compared to full DBMS platforms.

## Types

Name        | Description
----------- | --------------
`ARRAY`     |
`BOOLEAN`   | Logical boolean (True/False).
`DOUBLE`    | 
`INTEGER`   |
`DECIMAL` :octicons-star-16:  |
`VARCHAR`   | Variable-length character string.
`STRUCT`    | A dictionary of multiple named values, where each key is a string, but the value can be a different type for each key.
`DATE`      |
`TIMESTAMP` | Combination of date and time.
`INTERVAL` :octicons-star-16: | The difference between two TIMESTAMP values
`INET`     :octicons-star-16: | Network Range

!!! Note  
    Types marked with :octicons-star-16: (DECIMAL, INTERVAL and INET) have limited support.

## Casting

Values can be cast using the `CAST` function, its form is `CAST(any AS type)`. Where values are incompatible, an error will be thrown, to avoid errors `TRY_CAST` (or `SAFE_CAST`) can be used instead which will return `null` instead of error.

### Type Hints

**Intervals**

Intervals require definition by type hints, using the type name before providing a literal description of the value.

~~~
INTERVAL 'value' unit
~~~

Where unit can be 'Year', 'Month', 'Day', 'Hour', 'Minute' or 'Second'.

**Other**

`BOOLEAN`, `NUMERIC` and `TIMESTAMP` also support 'type hint' notation (`SELECT TIMESTAMP '2022-01-01';`) to perform casting.

## Coercion

### Timestamps & Dates

Literal values in quotes may be in interpreted as a `TIMESTAMP` or `DATE` when they match a valid date in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html)  format (e.g. `YYYY-MM-DD` and `YYYY-MM-DD HH:MM`). The decision regarding coercising to a `DATE` if there is no time component to the value, otherwise it will be coerced to a `TIMESTAMP`. 

All `TIMESTAMP` and values read from datasets are coerced to nanosecond precision timestamps.

### Numbers

All numeric values included in SQL statements and read from datasets are coerced to 64bit floats.

Hex literals can be provided using `0x` prefix, for example `0xc0ffee` is handled as the integer `12648430`.

### IPv4 Network Ranges

IPv4 Network Range comparisions automatically interpret IP addresses and ranges.
