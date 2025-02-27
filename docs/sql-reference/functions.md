# Functions

This document describes the supported SQL functions and operators.

Generally functions will return `null` on `null` input, although note that this is not true in all circumstances, especially for null-aware functions like `COALESCE` and `IFNULL`.

Definitions noted with a :octicons-dot-16: accept different input arguments.

New functions for this version are annotated with the :octicons-star-16: icon.

## Conversion Functions

!!! function "`BOOLEAN` **any**: _any_ → _boolean_"  
    Cast **any** to a `BOOLEAN`, raises an error if cast is not possible. Note `BOOLEAN` does not require parenthesis, however any aliases do.      
    Alias for `CAST`(**any** AS BOOLEAN)   

!!! function "`BLOB` (**varchar**: _varchar_) → _blob_"  
    Cast **varchar** to **blob**, raises an error if cast is not possible.   
    _Note_: prefixing can also be used to define a literal blob string, `b'value'` is equivalent to `blob('value')`.   

!!! function "`CAST` (**any**: _any_ AS **type**) → _type_"  
    Cast **any** to **type**, raises an error if cast is not possible.   
    Also implemented as individual cast functions (`BOOLEAN`, `INTEGER`, `FLOAT`, `VARCHAR`).

!!! function "`INT` (**num**: _numeric_) → _numeric_"  
    Alias for `INTEGER`

!!! function "`HUMANIZE` (**num**: _numeric_) → _varchar_"     
    :octicons-star-16: **New in 0.20** :octicons-beaker-24:    
    Convert large numbers to forms easier for humans to read.

!!! function "`INTEGER` (**num**: _numeric_) → _numeric_"  
    Convert **num** to an integer.   
    `INTEGER` is a psuedo-type, `CAST` is not supported and values may be coerced to `NUMERIC`.

!!! function "`FLOAT` (**num**: _numeric_) → _numeric_"  
    Convert **num** to a floating point number.   
    `FLOAT` is a psuedo-type, `CAST` is not supported and values may be coerced to `NUMERIC`.

!!! function "`NUMERIC` **any**: _any_ → _numeric_"  
    Cast **any** to a floating point number, raises an error if cast is not possible. Note `NUMERIC` does not require parenthesis, however any aliases do.   
    Alias for `CAST`(**any** AS NUMERIC)   

!!! function "`SAFE_CAST` (**any**: _any_ AS **type**) → _type_"    
    Alias for `TRY_CAST`(**any** AS **type**)  

!!! function "`STR` (**any**: _any_) → _varchar_"     
    Alias of `VARCHAR`(**any**) and `CAST`(**any** AS VARCHAR)   

!!! function "`STRING` (**any**: _any_) → _varchar_"     
    Alias of `VARCHAR`(**any**) and `CAST`(**any** AS VARCHAR)

!!! function "`STRUCT` (**any**: _any_) → _struct_"   
    Cast **any** to a struct / dictionary.   
    Alias of `CAST`(**any** AS STRUCT)

!!! function "`TIMESTAMP` **iso8601**: _varchar_ → _timestamp_"  
    Cast an [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format string to a timestamp, raises an error if cast is not possible. Note `TIMESTAMP` does not require parenthesis, however any aliases do.    
    Alias for `CAST`(**iso8601** AS TIMESTAMP)   

!!! function "`TRY_CAST` (**any**: _any_ AS **type**) → _type_"  
    Cast **any** to **type**, if cast is not possible, returns `null`.   

!!! function "`VARCHAR` (_any_) → _varchar_"  
    Cast **any** to a string, raises an error if cast is not possible.  
    Alias for `CAST`(**any** AS VARCHAR)

## Date & Time Functions

For more details, see [Working with Timestamps](../adv-working-with-timestamps/).

!!! function "`current_date` → _timestamp_"  
    Return the current date, in UTC. Note `current_date` does not require parenthesis.  

!!! function "`current_time` → _timestamp_"  
    Return the current date and time, in UTC. Note `current_time` does not require parenthesis.  

!!! function "`DATE` (**ts**: _timestamp_) → _timestamp_"  
    Remove any time information, leaving just the date part of **ts**.   

!!! function "`DATE_FORMAT` (**ts**: _timestamp_, **format**: _varchar_) → _varchar_"  
    Formats **ts** as a string using **format**.   

!!! function "`DATEPART`(**unit**: _varchar_, **ts**: _timestamp_) → _numeric_"  
    Alias of `EXTRACT`(**unit** FROM **ts**)

!!! function "`DATE_TRUNC` (**unit**: _varchar_, **ts**: _timestamp_) → _varchar_"  
    Returns **ts** truncated to **unit**.  

!!! function "`DATEDIFF` (**unit**: _varchar_, **start**: _timestamp_, **end**: _timestamp_) → _numeric_"  
    Calculate the difference between the start and end timestamps in a given **unit**.  

!!! function "`DAY` (_timestamp_) → _numeric_"  
    Extract day number from a timestamp. See `EXTRACT`.

!!! function "`EXTRACT` (**unit** FROM _timestamp_) → _numeric_"       
    Extract **unit** of a timestamp.   
    - `NANOSECOND`  
    - `MICROSECOND`  
    - `MILLISECOND`  
    - `SECOND`  
    - `MINUTE`  
    - `HOUR`  
    - `DATE`  
    - `DAY`  
    - `DAYOFWEEK` / `DOW`  
    - `WEEK`  
    - `ISOWEEK`  
    - `MONTH`  
    - `QUARTER`  
    - `DAYOFYEAR` / `DOY`  
    - `YEAR`  
    - `ISOYEAR`  
    - `DECADE`  
    - `CENTURY`  
    - `EPOCH`   
    - `JULIAN`    

!!! function "`FROM_UNIXTIME` (**timestamp**: _numeric_) → _timestamp_"    
    Return a timestamp representation of an [Unix Timestamp](https://www.unixtimestamp.com/).    
    _Related:_ `UNIXTIME` 

!!! function "`NOW` () → _timestamp_"  
    Alias for `current_time`

!!! function "`TIME` () → _timestamp_"  
    Returns the current iime (UTC).     

!!! function "`TIME_BUCKET` (_timestamp_, **multiple**: _numeric_, **unit**: _varchar_) → _timestamp_"  
    Floor timestamps into fixed time interval buckets. **unit** is optional and will be `day` if not provided.

!!! function "`TODAY` () → _timestamp_"  
    Alias for `current_date`

!!! function "`HOUR` (**ts**: _timestamp_) → _numeric_"  
    Returns the hour of the day from **ts**. The value ranges from `0` to `23`.   
    Alias for `EXTRACT`(hour FROM **ts**)

!!! function "`MINUTE` (**ts**: _timestamp_) → _numeric_"  
    Returns the minute of the hour from **ts**. The value ranges from `0` to `59`.  
    Alias for `EXTRACT`(minute FROM **ts**)

!!! function "`MONTH` (**ts**: _timestamp_) → _numeric_"  
    Returns the month of the year from **ts**. The value ranges from `1` to `12`.  
    Alias for `EXTRACT`(month FROM **ts**)

!!! function "`QUARTER` (**ts**: _timestamp_) → _numeric_"  
    Returns the quarter of the year from **ts**. The value ranges from `1` to `4`.  
    Alias for `EXTRACT`(quarter FROM **ts**)

!!! function "`SECOND` (**ts**: _timestamp_) → _numeric_"  
    Returns the second of the minute from **ts**. The value ranges from `0` to `59`.  
    Alias for `EXTRACT`(second FROM **ts**)

!!! function "`TIMEDIFF` (**unit**: _varchar_, **start**: _timestamp_) → _numeric_"   
    Calculate the difference between the start and end times.  

!!! function "`UNIXTIME` () → _numeric_:octicons-dot-16:"       
    Return the current time as a [Unix Timestamp](https://www.unixtimestamp.com/).    
    _Related:_ `FROM_UNIXTIME`, `current_time` 

!!! function "`UNIXTIME` (**timestamp**: _timestamp_) → _numeric_:octicons-dot-16:"    
    Return **timestamp** in [Unix Timestamp](https://www.unixtimestamp.com/) representation.    
    _Related:_ `FROM_UNIXTIME` 

!!! function "`UTC_TIMESTAMP` () → _timestamp_"   
    Alias for `current_time`

!!! function "`WEEK` (**ts**: _timestamp_) → _numeric_"  
    Returns the week of the year from **ts**. The value ranges from `1` to `53`.  
    Alias for `EXTRACT`(week FROM **ts**)

!!! function "`YEAR` (**ts**: _timestamp_) → _numeric_"  
    Returns the year from **ts**.  
    Alias for `EXTRACT`(year FROM **ts**)

## Infix Functions

These are functions that are called similar to comparison operators:

!!! function "_numeric_ `+` _numeric_ → _numeric_"  
    Numeric addition

!!! function "_timestamp_ `+` _interval_ → _timestamp_"  
    Timestamp and Interval addition

!!! function "_numeric_ `-` _numeric_ → _numeric_"  
    Numeric subtraction

!!! function "_timestamp_ `-` _interval_ → _timestamp_"  
    Timestamp and Interval subtraction

!!! function "_timestamp_ `-` _timestamp_ → _interval_"  
    Timestamp subtraction

!!! function "_numeric_ `*` _numeric_ → _numeric_"  
    Numeric multiplication

!!! function "_numeric_ `/` _numeric_ → _numeric_"  
    Numeric division

!!! function "_numeric_ `DIV` _numeric_ → _integer_"   
    Integer division

!!! function "_numeric_ `%` _numeric_ → _numeric_"  
    Numeric modulo (remainder)

!!! function "_varchar_ `||` _varchar_ → _varchar_"  
    String concatenation  

!!! function "_inet_ `|` _inet_ → _bool_"   
    IP address containment

!!! function "_integer_ `|` _integer_ → _integer_"   
    Bitwise OR

!!! function "_integer_ `&` _integer_ → _integer_"  
    Bitwise AND

!!! function "_integer_ `^` _integer_ → _integer_"   
    Bitwise XOR

## Array Functions

For more details, see [Working with Arrays](../adv-working-with-lists/).

!!! function "**array**: _array_`[`**index**: _numeric_`]` → _value_:octicons-dot-16:"  
    Return the **index**th element from **array**. 

!!! function "**array**: _array_ `@>` **values**: _array_ → _boolean_"   
    Return `true` if **array** contains any of the elements in **values**.   
    _Related:_ `ARRAY_CONTAINS_ANY`   

!!! function "`ARRAY_CONTAINS` (**array**: _array_, **value**) → _boolean_"  
    Return `true` if **array** contains **value**.  
    See also `SEARCH`(**array**, **value**)  
    See also `ANY`

!!! function "`ARRAY_CONTAINS_ANY` (**array**: _array_, **values**: _array_) → _boolean_"    
    Return `true` if **array** contains any of the elements in **values**.

!!! function "`ARRAY_CONTAINS_ALL` (**array**: _array_, **values**: _array_) → _boolean_"   
    Return `true` if **array** contains all of elements in **values**.

!!! function "`GET` (**array**: _array_, **index**: _numeric_) → _value_:octicons-dot-16:"   
    Alias of **array**`[`**index**`]`  

!!! function "`GREATEST` (**array**: _array_) → _value_"   
    Return the greatest value in **array**.  
    _Related:_ `LEAST`

!!! function "`LEAST` (**array**: _array_) → _value_"   
    Return the smallest value in **array**.  
    _Related:_ `GREATEST`

!!! function "`LEN` (**array**: _array_) → _numeric_:octicons-dot-16:"   
    Alias of `LENGTH`(**array**)

!!! function "`LENGTH` (**array**: _array_) → _numeric_:octicons-dot-16:"   
    Returns the number of elements in **array**.

!!! function "`LIST_CONTAINS` (**array**: _array_, **value**) → _boolean_"  
    **DEPRECATED**   
    Alias of `ARRAY_CONTAINS`

!!! function "`LIST_CONTAINS_ANY` (**array**: _array_, **values**: _array_) → _boolean_"    
    **DEPRECATED**   
    Alias of `ARRAY_CONTAINS_ANY`   
    _Related:_ `@>`

!!! function "`LIST_CONTAINS_ALL` (**array**: _array_, **values**: _array_) → _boolean_"   
    **DEPRECATED**   
    Alias of `ARRAY_CONTAINS_ALL`

!!! function "`SEARCH` (**array**: _array_, **value**) → _boolean_:octicons-dot-16:"  
    Return `true` if **array** contains **value**. 

!!! function "`SORT` (**array**: _array_) → _array_"  
    Return **array** in ascending order. 

## Numeric Functions

!!! function "`ABS` (**x**: _numeric_) → _numeric_"  
    Alias of `ABSOLUTE`  

!!! function "`ABSOLUTE` (**x**: _numeric_) → _numeric_"  
    Returns the absolute value of **x**.   

!!! function "`CEIL` (**x**: _numeric_, **scale**: _integer_) → _double_"  
    Returns the nearest equal or larger whole number to **x**, or to the nearest equal or larger double with **scale** places after the decimal point.   
    _Related:_ `FLOOR`   

!!! function "`CEILING` (**x**: _numeric_, **scale**: _integer_) → _double_"   
    **DEPRECATED** 

!!! function "`E` () → _numeric_"  
    Returns the constant _e_, also known as [_Euler's number_](https://en.wikipedia.org/wiki/E_(mathematical_constant)).  
    _Related:_ `LN`.

!!! function "`FLOOR` (**x**: _numeric_) → _numeric_"  
    Returns the nearest equal or lesser whole number to **x**, or to the nearest equal or lesser double with **scale** places after the decimal point.   
    _Related:_ `CEIL`    

!!! function "`PHI` () → _numeric_"  
    Returns the constant φ (_phi_), also known as [_the golden ratio_](https://en.wikipedia.org/wiki/Golden_ratio).  

!!! function "`PI` () → _numeric_"  
    Returns the constant [π](https://en.wikipedia.org/wiki/Pi) (_pi_).  

!!! function "`POWER` (**base**: _numeric_, **exponent**: _numeric**) → _numeric_"   
    Returns **base** to the power of **exponent**.  

!!! function "`LN` (**x**: _numeric_) → _numeric_"   
    Returns the natural logarithm of **x**.  
    _Related:_ `E`, `LOG`, `LOG10`, `LOG2`

!!! function "`LOG` (**x**: _numeric_, **base**: _numeric_) → _numeric_"   
    Returns the logarithm of **x** for base **base**.   
    _Related:_ `LN`, `LOG10`, `LOG2`

!!! function "`LOG10` (**x**: _numeric_) → _numeric_"   
    Returns the logarithm for base 10 of **x**.  
    _Related:_ `LN`, `LOG`, `LOG2`

!!! function "`LOG2` (**x**: _numeric_) → _numeric_"   
    Returns the logarithm for base 2 of **x**.  
    _Related:_ `LN`, `LOG`, `LOG10`

!!! function "`ROUND` (**x**: _numeric_) → _numeric_:octicons-dot-16:"  
    Returns **x** rounded to the nearest integer. 

!!! function "`ROUND` (**x**: _numeric_, **places**: _numeric_) → _numeric_:octicons-dot-16:"  
    Returns **x** rounded to **places** decimal places.

!!! function "`SIGN` (**x**: _numeric_) → _numeric_"   
    Returns the signum function of **x**; 0 if **x** is 0, -1 if **x** is less than 0 and 1 if **x** is greater than 0.

!!! function "`SIGNUM` (**x**: _numeric_) → _numeric_"   
    Alias for `SIGN`

!!! function "`SQRT` (**x**: _numeric_) → _numeric_"   
    Returns the square root of **x**.

!!! function "`TRUNC` (**x**: _numeric_) → _numeric_"  
    Alias of `TRUNCATE`  

!!! function "`TRUNCATE` (**x**: _numeric_) → _numeric_"  
    Returns **x** rounded to integer by dropping digits after decimal point.    

## String Functions

Functions for examining and manipulating string values. 

!!! function "**str**: _varchar_`[`**index**: _numeric_`]` → _varchar_:octicons-dot-16:"  
    Subscript operator, return the **index**th character from **str**. 

!!! function "`ASCII` (**string**: _char_) → _integer_"   
    Returns the ASCII code for a given character.  
    _Related:_ `CHAR`

!!! function "`CHAR` (**code**: _integer_) → _char_"   
    Returns the character for a given ASCII code.  
    _Related:_ `ASCII`

!!! function "`CONCAT` (**list**: _array_<_varchar_>) → _varchar_"   
    Returns the result of concatenating, or joining, of two or more string values in an end-to-end manner.  
    _Related:_ `CONCAT_WS`

!!! function "`CONCAT_WS` (**separator**: _varchar_, **list**: _array_<_varchar_>) → _varchar_"   
    Returns the result of concatenating, or joining, of two or more string values with a **separator** used to delimit individual values.  
    _Related:_ `CONCAT`

!!! function "`ENDS_WITH` (**str**: _varchar_, **value**: _varchar_) → _boolean_"  
    Return `true` if **str** ends with **value**.  
    _Related:_ `STARTS_WITH`

!!! function "`GET` (**str**: _varchar_, **index**: _numeric_) → _varchar_:octicons-dot-16:"  
    Alias of **str**`[`**index**`]`   

!!! function "`LEFT` (**str**: _varchar_, **n**: _numeric_) → _varchar_"  
    Extract the left-most **n** characters of **str**.  
    _Related:_ `RIGHT`

!!! function "`LEN` (**str**: _varchar_) → _numeric_:octicons-dot-16:"   
    Alias of `LENGTH`

!!! function "`LENGTH` (**str**: _varchar_) → _numeric_:octicons-dot-16:"  
    Returns the length of **str** in characters.    

!!! function "`LEVENSHTEIN` (**str1**: _varchar_, **str2**: _varchar_) → _numeric_"   
    Returns the [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) between **str1** and **str2**   

!!! function "`LOWER` (**str**: _varchar_) → _varchar_"  
    Converts **str** to lowercase.   
    _Related:_ `UPPER`, `TITLE`

!!! function "`LPAD` (**string**: _varchar_, **width**: _integer_, **fill**: _char_) → _varchar_"   
    Returns a string at least **width** characters wide, with **fill** used to pad the string, to the left, to fill to the required width.   
    _Related:_ `RPAD`

!!! function "`LTRIM` (**str**: _varchar_) → _varchar_"    
    Remove leading whitespace from **str**.   
    _Related:_ `RTRIM`, `TRIM`

!!! function "`MATCH` (**column**: _varchar_) `AGAINST` (**query**: _varchar_) → _boolean_"    
    Perform a fulltext search of **column** for the values in **query**.  
    _Note:_ Values in `$stop_words` are ignored.

!!! function "`POSITION` (**substring**: _varchar_ IN **string**: _varchar_) → _numeric_"    
    Returns the starting position of the first instance of **substring** in **string**. Positions start with 1. If not found, 0 is returned.   

!!! function "`REGEXP_REPLACE` (**str**: _varchar_, **pattern**: _varchar_, **replace**: _varchar_) → _varchar_"   
    Performs a replace based on regular expressions.  

!!! function "`REVERSE` (**str**: _varchar_) → _varchar_"  
    Returns **str** with the characters in reverse order.

!!! function "`RIGHT` (**str**: _varchar_, **n**: _numeric_) → _varchar_"  
    Extract the right-most **n** characters of **str**.   
    _Related:_ `LEFT`

!!! function "`RPAD` (**string**: _varchar_, **width**: _integer_, **fill**: _char_) → _varchar_"   
    Returns a string at least **width** characters wide, with **fill** used to pad the string, to the right, to fill to the required width.
    _Related:_ `LPAD`

!!! function "`RTRIM` (**str**: _varchar_) → _varchar_"     
    Remove trailing whitespace from **str**.   
    _Related:_ `LTRIM`, `TRIM`

!!! function "`SOUNDEX` (**str**: _varchar_) → _varchar_"  
    Returns a character string containing the phonetic representation of char. See [Soundex 🡕](https://en.wikipedia.org/wiki/Soundex).   

!!! function "`SEARCH` (**str**: _varchar_, **substring**: _varchar_) → _boolean_:octicons-dot-16:"  
    Return `true` if **str** contains **substring**.  

!!! function "`SPLIT` (**str**: _varchar_) → _array_:octicons-dot-16:"   
    Splits **str** on commas (`,`) and returns an array.

!!! function "`SPLIT` (**str**: _varchar_, **delimiter**: _varchar_) → _array_:octicons-dot-16:"   
    Splits **str** on **delimiter** and returns an array.

!!! function "`SPLIT` (**str**: _varchar_, **delimiter**: _varchar_, **limit**: _integer_) → _array_:octicons-dot-16:"   
    Splits **str** on **delimiter** and returns an array of size at most **limit**. The last element in the array contains the remaining part of the string. **limit** must be greater than zero.

!!! function "`SUBSTRING` (**str**: _varchar_, **start**: _numeric_) → _varchar_:octicons-dot-16:" 
    Return substring from a string from **start** position to the end of **str**.  

!!! function "`SUBSTRING` (**str**: _varchar_, **start**: _numeric_, **length**: _numeric_) → _varchar_:octicons-dot-16:"  
    Return substring from a string from **start** position for **length** characters.  
 
!!! function "`STARTS_WITH` (**str**: _varchar_, **value**: _varchar_) → _boolean_"  
    Return `true` if **str** starts with **value**.  
    _Related:_ `ENDS_WITH`

!!! function "`TITLE` (**str**: _varchar_) → _varchar_"  
    Returns **str** with the first letter of each work in upper case.   
    _Related:_ `LOWER`, `UPPER`

!!! function "`TRIM` ( [ LEADING | TRAILING | BOTH ] [ **chars**: _varchar_ FROM ] **str**: _varchar_ ) → _varchar_"   
    Removes leading and trailing **chars** from **str**, if **chars** is not specified, whitespace is removed. Note that any instance of a character in **chars** is removed in any order they appear.  
    The **LEADING** modifier removes **chars** from the start of **str**.   
    The **TRAILING** modifier removes **chars** from the end of **str**.    
    The **BOTH** modifier removes **chars** from both the start and end of **str**, this is the default behaviour if no positional modifier is supplied.   
    _Related:_ `LTRIM`, `RTRIM`

!!! function "`UPPER` (**str**: _varchar_) → _varchar_"  
    Converts **str** to uppercase.   
    _Related:_ `LOWER`, `TITLE`

## Struct Functions

For more details, see [Working with Structs](../adv-working-with-structs/).

!!! function "_struct_ `->` _key_ → _value_ "    
    Return the value for **key** from **object**.   
    Struct values can be `VARCHAR` or `BLOB` formatted JSON strings.

!!! function "_struct_ `->>` _key_ → _varchar_ "   
    Return the value for **key** from **object**, non `null` values are cast to `VARCHAR`.   
    Struct values can be `VARCHAR` or `BLOB` formatted JSON strings.
    _Related:_ `->` operator

!!! function "_struct_ `@?` _key_ → _value_ "   
    Return true if _struct_ contains the key _key_.   
    Struct values can be `VARCHAR` or `BLOB` formatted JSON strings.  

!!! function "_struct_ `@?` _jsonpath_ → _value_"  
    :octicons-star-16: **New in 0.19**       
    Return true if _struct_ contains a value at _jsonpath_.   
    Struct values can be `VARCHAR` or `BLOB` formatted JSON strings. 

!!! function "**object**: _struct_`[`**key**: _varchar_`]` → _value_:octicons-dot-16:"  
    Subscript operator
    Alias of **object**`->`**key**  

!!! function "`GET` (**object**: _struct_, **key**: _varchar_) → _value_:octicons-dot-16:"  
    Alias of **object**`->`**key**    

!!! function "`JSONB_OBJECT_KEYS` (**object**: _struct_) → _array_:octicons-dot-16:"   
    Returnan array of the keys in a struct value.   
    Struct values can be `STRUCT` values, or `VARCHAR` or `BLOB` formatted JSON strings.   

!!! function "`SEARCH` (**object**: _struct_, **value**: _varchar_) → _boolean_:octicons-dot-16:"  
    Return `true` if any of the values in **object** is **value**. Note `SEARCH` does not match struct keys.

## System Functions

!!! function "`VERSION` () → _varchar_"  
    Return the version of the query engine.

## Other Functions

!!! function "`BASE64_DECODE`  (**str**: _varchar_) → _varchar_"  
    Decode BASE64 encoded value, **str**. 
    _Related:_ `BASE64_ENCODE`

!!! function "`BASE64_ENCODE` (**str**: _varchar_) → _varchar_"  
    Encode **str** with BASE64 encoding.  
    _Related:_ `BASE64_DECODE`

!!! function "`BASE85_DECODE` (**str**: _varchar_) → _varchar_"  
    Decode BASE85 encoded value, **str**. 
    _Related:_ `BASE85_ENCODE`

!!! function "`BASE85_ENCODE` (**str**: _varchar_) → _varchar_"  
    Encode **str** with BASE85 encoding.  
    _Related:_ `BASE85_DECODE`

!!! function "`COALESCE` (**arg1**, **arg2**, ...) → _value_"  
    Return the first item from args which is not `null`.    
    _Related:_ `IFNULL`

!!! function "`COSINE_SIMILARITY`  (**str**: _varchar_, **value**: _varchar_) → _double_"     
    Perform an ad hoc cosine similarity comparison between **str** and **value**.   
    _Note:_ Values in `$stop_words` are ignored.

!!! function "`GENERATE_SERIES` (**start**: _numeric_, **stop**: _numeric_) → _array_<_numeric_>:octicons-dot-16:"   
    Return a numeric list between **start** and **stop**, with a step of 1.

!!! function "`GENERATE_SERIES` (**start**: _numeric_, **stop**: _numeric_, **step**: _numeric_) → _array_<_numeric_>:octicons-dot-16:"  
    Return a numeric list between **start** and **stop**, with an increment of **step**.

!!! function "`GENERATE_SERIES` (**start**: _timestamp_, **stop**: _timestamp_, _interval_) → _array_<_timestamp_>:octicons-dot-16:"    
    Return a timestamp list between **start** and **stop**, with a interval of **step**.     

!!! function "`HASH` (**value**: _any_) → _varchar_"  
    Calculate the [CityHash](https://opensource.googleblog.com/2011/04/introducing-cityhash.html) (64 bit) of **value**.

!!! function "`HEX_DECODE` (**str**: _varchar_) → _varchar_"  
    Decode hexidecimal (BASE16) encoded value, **str**.    
    _Related:_ `HEX_ENCODE`

!!! function "`HEX_ENCODE` (**str**: _varchar_) → _varchar_"  
    Encode **str** with hexadecimal (BASE16) encoding.  
    _Related:_ `HEX_DECODE`

!!! function "`IIF` (**condition**, **true_value**, **false_value**) → _input type_"  
    Return the **true_value** if the condition evaluates to `True`, otherwise return the **false_value**.

!!! function "`IFNOTNULL` (**check_expression**: _any_, **replacement_value**: _any_) → _input type_"  
    :octicons-star-16: **New in 0.19**   
    Returns **check_expression** if not `null`, otherwise returns **replacement_value**.   
    _Related:_ `IFNULL`   

!!! function "`IFNULL` (**check_expression**: _any_, **replacement_value**: _any_) → _input type_"  
    Returns **check_expression** if `null`, otherwise returns **replacement_value**.   
    _Related:_ `COALESCE`, `IFNOTNULL` 

!!! function "`NORMAL` () → _numeric_"  
    Random number from a normal (Gaussian) distribution; distribution is centred at 0.0 and has a standard deviation of 1.0. Per record.

!!! function "`NULLIF` (**value1**: _any_, **value2**: _any_) → _input type_"  
    Returns `null` if **value1** equals **value2**, otherwise returns **value1**. 

!!! function "`MD5` (**str**: _varchar_) → _varchar_"  
    Calculate the MD5 hash of **str**.

!!! function "`RAND` () → _numeric_"  
    Returns a random number between 0 and 1. Per record.

!!! function "`RANDOM` () → _numeric_"  
    Alias of `RAND`

!!! function "`RANDOM_STRING` (**length**: _numeric_) → _varchar_"  
    Returns a random string of lowercase alphabetic characters with a length of **length**. Per record.

!!! function "`SHA1` (**str**: _varchar_) → _varchar_"  
    Calculate the SHA1 hash of **str**.  
    _Related:_ `SHA224`, `SHA256`, `SHA384`, `SHA512`

!!! function "`SHA224` (**str**: _varchar_) → _varchar_"  
    Calculate the SHA224 hash of **str**.  
    _Related:_ `SHA1`, `SHA256`, `SHA384`, `SHA512`

!!! function "`SHA256` (**str**: _varchar_) → _varchar_"  
    Calculate the SHA256 hash of **str**.  
    _Related:_ `SHA1`, `SHA224`, `SHA384`, `SHA512`

!!! function "`SHA384` (**str**: _varchar_) → _varchar_"  
    Calculate the SHA384 hash of **stre**.  
    _Related:_ `SHA1`, `SHA224`, `SHA256`, `SHA512`

!!! function "`SHA512` (**str**: _varchar_) → _varchar_"  
    Calculate the SHA512 hash of **str**.  
    _Related:_ `SHA1`, `SHA224`, `SHA256`, `SHA384`

!!! function "`UNNEST` (**array**: _array_) → _relation_"  
    Create a virtual relation with a row for each element in **array**.

