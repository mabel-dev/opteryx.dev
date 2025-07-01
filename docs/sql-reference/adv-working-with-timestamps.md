# Working with Timestamps

Working with DATE and TIMESTAMP often involves working with INTERVALs. 

INTERVALs may not always act as expected, especially when working with months and years, primarily due to complexities in quickly and accurately determining if an number of days is a given number of months.

!!! Note  
    Functions that return the current time or date (including now) will return the time as at the start of the execution of the query.

## Actions

### Add/Subtract

_timestamp_ `+` _interval_ → _timestamp_  

_timestamp_ `-` _interval_ → _timestamp_  

_timestamp_ `-` _timestamp_ → _interval_ *

_interval_ `+` _interval_ -> _interval_

_interval_ `-` _interval_ -> _interval_

_timestamp_ `+` _timestamp_ -> **not possible**

`DATEDIFF` (**unit**: _varchar_, **start**: _timestamp_, **end**: _timestamp_) → _numeric_  

**Note** INTERVALs created as the result of date and timestamp substraction have no month or year component and are handled internally as seconds. This may result in unexpected outcomes, for example when mixed with month calculations.

If determing differences in months or years, this form is supported:

~~~
WHERE birth + INTERVAL '100' YEAR > death
~~~

this form is not

~~~
WHERE death - birth > INTERVAL '100' YEAR
~~~

### Construct

~~~
INTERVAL values units
~~~

Examples:

`INTERVAL '1' YEAR`
`INTERVAL '1' DAY`
`INTERVAL '1 1' DAY TO HOUR`

Supported units:
`YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, `SECOND`

~~~
TIMESTAMP value
~~~

Examples:

`TIMESTAMP '2024-02-14'`

### Extract

~~~
EXTRACT(part FROM timestamp)
~~~
~~~
DATE(timestamp)
~~~

### Format

~~~
DATE_FORMAT(timestamp, format)
~~~

### Parse

~~~
CAST(field AS TIMESTAMP)
~~~
~~~
TIMESTAMP(field)
~~~

### Truncate

~~~
DATE_TRUNC(part, timestamp)
~~~
~~~
TIME_BUCKET(timestamp, multiple, unit)
~~~

### Generate

~~~
current_date
~~~
~~~
current_time
~~~
~~~
current_timestamp
~~~
~~~
YESTERDAY()
~~~
~~~
TIME()
~~~
~~~
generate_series()
~~~

Note that `current_date`, `current_timestamp` and `current_time` support being called without parenthesis.


Recognized date parts and periods and support across various functions:

Part     | DATE_TRUNC | EXTRACT | DATEDIFF | TIME_BUCKET | Notes
-------- | :--------: | :-----: | :------: | :---------: | ----
second   | ✓          | ✓       | ✓        | ✓           |
minute   | ✓          | ✓       | ✓        | ✓           |
hour     | ✓          | ✓       | ✓        | ✓           |
day      | ✓          | ✓       | ✓        | ✓           |
dow      | ✘          | ✓       | ✘        | ✘           | day of week
week     | ✓          | ✓       | ✓        | ✓           | iso week i.e. to monday
month    | ✓          | ✓       | ▲        | ✓           | DATEFIFF unreliable calculating months
quarter  | ✓          | ✓       | ✓        | ✓           |
doy      | ✘          | ✓       | ✘        | ✘           | day of year
year     | ✓          | ✓       | ✓        | ✓           |

## Implicit Casting

In many situation where a timestamp is expected, if an [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) formatted string is provided, the engine will default to interpretting as a timestamp. However, for reliability, you should not rely on the engine doing this for you.

## Timezones

The engine is opinionated to run in UTC - all instances where the system time is requested, UTC is used.

## Precision

INTERVALs are maintained internally with a millisecond precision.

TIMESTAMPs are maintained internally with a nanosecond precision.

DATEs are maintained internally with a day precision.