# Functions

This document describes the supported SQL functions and operators.

Generally functions will return `null` on `null` input, although note that this is not true in all circumstances, especially for null-aware functions like `COALESCE` and `IFNULL`.

Definitions noted with a :octicons-dot-16: accept different input arguments.

New functions for this version are annotated with the :octicons-star-16: icon.

## Conversion Functions

!!! function "`BOOLEAN` **any**: _any_ → _boolean_"  
    Cast **any** to a `BOOLEAN`, raises an error if cast is not possible. Note `BOOLEAN` does not require parenthesis, however any aliases do.      
    Alias for `CAST`(**any** AS BOOLEAN)   

!!! function "`CAST` (**any**: _any_ AS **type**) → _type_"  
    Cast **any** to **type**, raises an error if cast is not possible.   
    Also implemented as individual cast functions.

!!! function "`INT` (**num**: _numeric_) → _numeric_"  
    Alias for `INTEGER`

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
    Also implemented as individual extraction functions.

!!! function "`FROM_UNIXTIME` (**timestamp**: _numeric_) → _timestamp_"    
    ** :octicons-star-16: New in 0.8**      
    Return a timestamp representation of an [Unix Timestamp](https://www.unixtimestamp.com/).    
    Related: `UNIXTIME` 

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

!!! function "`UNIXTIME` () → _numeric_:octicons-dot-16:"       
    ** :octicons-star-16: New in 0.8**      
    Return the current time as a [Unix Timestamp](https://www.unixtimestamp.com/).    
    Related: `FROM_UNIXTIME`, `current_time` 

!!! function "`UNIXTIME` (**timestamp**: _timestamp_) → _numeric_:octicons-dot-16:"    
    ** :octicons-star-16: New in 0.8**      
    Return **timestamp** in [Unix Timestamp](https://www.unixtimestamp.com/) representation.    
    Related: `FROM_UNIXTIME` 

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

!!! function "_numeric_ `%` _numeric_ → _numeric_"  
    Numeric modulo (remainder)

!!! function "_varchar_ `||` _varchar_ → _varchar_"  
    String concatenation  

!!! function "_inet_ `|` _inet_ → _bool_"   
    IP address containment

## List Functions

For more details, see [Working with Lists](../adv-working-with-lists/).

!!! function "**array**: _list_`[`**index**: _numeric_`]` → _value_:octicons-dot-16:"  
    Return the **index**th element from **array**. 

!!! function "`GET` (**array**: _list_, **index**: _numeric_) → _value_:octicons-dot-16:"   
    Alias of **array**`[`**index**`]`  

!!! function "`GREATEST` (**array**: _list_) → _value_"   
    Return the greatest value in **array**.  
    Related: `LEAST`

!!! function "`LEAST` (**array**: _list_) → _value_"   
    Return the smallest value in **array**.  
    Related: `GREATEST`

!!! function "`LEN` (**array**: _list_) → _numeric_:octicons-dot-16:"   
    Alias of `LENGTH`(**array**)

!!! function "`LENGTH` (**array**: _list_) → _numeric_:octicons-dot-16:"   
    Returns the number of elements in **array**.

!!! function "`LIST_CONTAINS` (**array**: _list_, **value**) → _boolean_"  
    Return `true` if **array** contains **value**.  
    See also `SEARCH`(**array**, **value**)  

!!! function "`LIST_CONTAINS_ANY` (**array**: _list_, **values**: _list_) → _boolean_"    
    Return `true` if **array** contains any elements in **values**.

!!! function "`LIST_CONTAINS_ALL` (**array**: _list_, **values**: _list_) → _boolean_"   
    Return `true` if **array** contains all of elements in **values**.

!!! function "`SEARCH` (**array**: _list_, **value**) → _boolean_:octicons-dot-16:"  
    Return `true` if **array** contains **value**. 

!!! function "`SORT` (**array**: _list_) → _list_"  
    Return **array** in ascending order. 

## Numeric Functions

!!! function "`ABS` (**x**: _numeric_) → _numeric_"  
    Alias of `ABSOLUTE`  

!!! function "`ABSOLUTE` (**x**: _numeric_) → _numeric_"  
    Returns the absolute value of **x**.   

!!! function "`CEIL` (**x**: _numeric_) → _numeric_"  
    Alias of `CEILING`  

!!! function "`CEILING` (**x**: _numeric_) → _numeric_"  
    Returns **x** rounded up to the nearest integer.   
    Related: `FLOOR` 

!!! function "`E` () → _numeric_"  
    Returns the constant _e_, also known as [_Euler's number_](https://en.wikipedia.org/wiki/E_(mathematical_constant)).  
    Related: `LN`.

!!! function "`FLOOR` (**x**: _numeric_) → _numeric_"  
    Returns **x** rounded down to the nearest integer.   

!!! function "`PHI` () → _numeric_"  
    Returns the constant φ (_phi_), also known as [_the golden ratio_](https://en.wikipedia.org/wiki/Golden_ratio).  

!!! function "`PI` () → _numeric_"  
    Returns the constant [π](https://en.wikipedia.org/wiki/Pi) (_pi_).  

!!! function "`POWER` (**base**: _numeric_, **exponent**: _numeric**) → _numeric_"   
    Returns **base** to the power of **exponent**.  

!!! function "`LN` (**x**: _numeric_) → _numeric_"   
    Returns the natural logarithm of **x**.  
    Related: `E`, `LOG`, `LOG10`, `LOG2`

!!! function "`LOG` (**x**: _numeric_, **base**: _numeric_) → _numeric_"   
    Returns the logarithm of **x** for base **base**.   
    Related: `LN`, `LOG10`, `LOG2`

!!! function "`LOG10` (**x**: _numeric_) → _numeric_"   
    Returns the logarithm for base 10 of **x**.  
    Related: `LN`, `LOG`, `LOG2`

!!! function "`LOG2` (**x**: _numeric_) → _numeric_"   
    Returns the logarithm for base 2 of **x**.  
    Related: `LN`, `LOG`, `LOG10`

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

!!! function "`CONCAT` (**list**: _array_<_varchar_>) → _varchar_"   
    Returns the result of concatenating, or joining, of two or more string values in an end-to-end manner.  
    Related: `CONCAT_WS`

!!! function "`CONCAT_WS` (**separator**: _varchar_, **list**: _array_<_varchar_>) → _varchar_"   
    Returns the result of concatenating, or joining, of two or more string values with a **separator** used to delimit individual values.  
    Related: `CONCAT`

!!! function "`ENDS_WITH` (**str**: _varchar_, **value**: _varchar_) → _boolean_"  
    Return `true` if **str** ends with **value**.  
    Related: `STARTS_WITH`

!!! function "`GET` (**str**: _varchar_, **index**: _numeric_) → _varchar_:octicons-dot-16:"  
    Alias of **str**`[`**index**`]`   

!!! function "`LEFT` (**str**: _varchar_, **n**: _numeric_) → _varchar_"  
    Extract the left-most **n** characters of **str**.  
    Related: `RIGHT`

!!! function "`LEN` (**str**: _varchar_) → _numeric_:octicons-dot-16:"   
    Alias of `LENGTH`

!!! function "`LENGTH` (**str**: _varchar_) → _numeric_:octicons-dot-16:"  
    Returns the length of **str** in characters.    

!!! function "`LEVENSHTEIN` (**str1**: _varchar_, **str2**: _varchar_) → _numeric_"   
    ** :octicons-star-16: New in 0.8**    
    Returns the [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) between **str1** and **str2**   

!!! function "`LOWER` (**str**: _varchar_) → _varchar_"  
    Converts **str** to lowercase.   
    Related: `UPPER`, `TITLE`

!!! function "`LTRIM` (**str**: _varchar_) → _varchar_"    
    Remove leading whitespace from **str**.   
    Related: `RTRIM`, `TRIM`

!!! function "`POSITION` (**substring**: _varchar_ IN **string**: _varchar_) → _numeric_"    
    Returns the starting position of the first instance of **substring** in **string**. Positions start with 1. If not found, 0 is returned.   

!!! function "`REVERSE` (**str**: _varchar_) → _varchar_"  
    Returns **str** with the characters in reverse order.

!!! function "`RIGHT` (**str**: _varchar_, **n**: _numeric_) → _varchar_"  
    Extract the right-most **n** characters of **str**.   
    Related: `LEFT`

!!! function "`RTRIM` (**str**: _varchar_) → _varchar_"     
    Remove trailing whitespace from **str**.   
    Related: `LTRIM`, `TRIM`

!!! function "`SOUNDEX` (**str**: _varchar_) → _varchar_"  
    Returns a character string containing the phonetic representation of char. See [Soundex 🡕](https://en.wikipedia.org/wiki/Soundex).   

!!! function "`SEARCH` (**str**: _varchar_, **substring**: _varchar_) → _boolean_:octicons-dot-16:"  
    Return `true` if **str** contains **substring**.  

!!! function "`SUBSTRING` (**str**: _varchar_, **start**: _numeric_) → _varchar_:octicons-dot-16:" 
    Return substring from a string from **start** position to the end of **str**.  

!!! function "`SUBSTRING` (**str**: _varchar_, **start**: _numeric_, **length**: _numeric_) → _varchar_:octicons-dot-16:"  
    Return substring from a string from **start** position for **length** characters.  
 
!!! function "`STARTS_WITH` (**str**: _varchar_, **value**: _varchar_) → _boolean_"  
    Return `true` if **str** starts with **value**.  
    Related: `ENDS_WITH`

!!! function "`TITLE` (**str**: _varchar_) → _varchar_"  
    Returns **str** with the first letter of each work in upper case.   
    Related: `LOWER`, `UPPER`

!!! function "`TRIM` ( [ LEADING | TRAILING | BOTH ] [ **chars**: _varchar_ FROM ] **str**: _varchar_ ) → _varchar_"   
    Removes leading and trailing **chars** from **str**, if **chars** is not specified, whitespace is removed. Note that any instance of a character in **chars** is removed in any order they appear.  
    The **LEADING** modifier removes **chars** from the start of **str**.   
    The **TRAILING** modifier removes **chars** from the end of **str**.    
    The **BOTH** modifier removes **chars** from both the start and end of **str**, this is the default behaviour if no positional modifier is supplied.   
    Related: `LTRIM`, `RTRIM`

!!! function "`UPPER` (**str**: _varchar_) → _varchar_"  
    Converts **str** to uppercase.   
    Related: `LOWER`, `TITLE`

## Struct Functions

For more details, see [Working with Structs](../adv-working-with-structs/).

!!! function "**object**: _struct_`[`**key**: _varchar_`]` → _value_:octicons-dot-16:"  
    Subscript operator, return the value for **key** from **object**. 

!!! function "`GET` (**object**: _struct_, **key**: _varchar_) → _value_:octicons-dot-16:"  
    Alias of **object**`[`**key**`]`  

!!! function "`SEARCH` (**object**: _struct_, **value**: _varchar_) → _boolean_:octicons-dot-16:"  
    Return `true` if any of the values in **object** is **value**. Note `SEARCH` does not match struct keys.

## System Functions

!!! function "`VERSION` () → _varchar_"  
    Return the version of the query engine.

## Other Functions

!!! function "`BASE64_DECODE`  (**str**: _varchar_) → _varchar_"  
    Decode BASE64 encoded value, **str**. 
    Related: `BASE64_ENCODE`

!!! function "`BASE64_ENCODE` (**str**: _varchar_) → _varchar_"  
    Encode **str** with BASE64 encoding.  
    Related: `BASE64_DECODE`

!!! function "`BASE85_DECODE` (**str**: _varchar_) → _varchar_"  
    Decode BASE85 encoded value, **str**. 
    Related: `BASE85_ENCODE`

!!! function "`BASE85_ENCODE` (**str**: _varchar_) → _varchar_"  
    Encode **str** with BASE85 encoding.  
    Related: `BASE85_DECODE`

!!! function "`COALESCE` (**arg1**, **arg2**, ...) → _value_"  
    Return the first item from args which is not `null`.    
    Related: `IFNULL`

!!! function "`GENERATE_SERIES` (**start**: _numeric_, **stop**: _numeric_) → _list_<_numeric_>:octicons-dot-16:"   
    Return a numeric list between **start** and **stop**, with a step of 1.

!!! function "`GENERATE_SERIES` (**start**: _numeric_, **stop**: _numeric_, **step**: _numeric_) → _list_<_numeric_>:octicons-dot-16:"  
    Return a numeric list between **start** and **stop**, with an increment of **step**.

!!! function "`GENERATE_SERIES` (**start**: _timestamp_, **stop**: _timestamp_, _interval_) → _list_<_timestamp_>:octicons-dot-16:"    
    Return a timestamp list between **start** and **stop**, with a interval of **step**.     

!!! function "`HASH` (**value**: _any_) → _varchar_"  
    Calculate the [CityHash](https://opensource.googleblog.com/2011/04/introducing-cityhash.html) (64 bit) of **value**.

!!! function "`HEX_DECODE` (**str**: _varchar_) → _varchar_"  
    Decode hexidecimal (BASE16) encoded value, **str**.    
    Related: `HEX_ENCODE`

!!! function "`HEX_ENCODE` (**str**: _varchar_) → _varchar_"  
    Encode **str** with hexadecimal (BASE16) encoding.  
    Related: `HEX_DECODE`

!!! function "`IIF` (**condition**, **true_value**, **false_value**) → _input type_"  
    Return the **true_value** if the condition evaluates to `True`, otherwise return the **false_value**.

!!! function "`IFNULL` (**check_expression**: _any_, **replacement_value**: _any_) → _input type_"  
    Returns **check_expression** if not `null`, otherwise returns **replacement_value**.
    Related: `COALESCE` 

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
    Related: `SHA224`, `SHA256`, `SHA384`, `SHA512`

!!! function "`SHA224` (**str**: _varchar_) → _varchar_"  
    Calculate the SHA224 hash of **str**.  
    Related: `SHA1`, `SHA256`, `SHA384`, `SHA512`

!!! function "`SHA256` (**str**: _varchar_) → _varchar_"  
    Calculate the SHA256 hash of **str**.  
    Related: `SHA1`, `SHA224`, `SHA384`, `SHA512`

!!! function "`SHA384` (**str**: _varchar_) → _varchar_"  
    Calculate the SHA384 hash of **stre**.  
    Related: `SHA1`, `SHA224`, `SHA256`, `SHA512`

!!! function "`SHA512` (**str**: _varchar_) → _varchar_"  
    Calculate the SHA512 hash of **str**.  
    Related: `SHA1`, `SHA224`, `SHA256`, `SHA384`

!!! function "`UNNEST` (**array**: _list_) → _relation_"  
    Create a virtual relation with a row for each element in **array**.

