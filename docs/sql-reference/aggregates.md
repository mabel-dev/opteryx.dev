# Aggregates

Aggregates are functions that combine multiple rows into a single value. Aggregates can only be used in the `SELECT` and `HAVING` clauses of a SQL query.

When the `ORDER BY` clause is provided, the values being aggregated are sorted after applying the function. 

Aggregate functions generally ignore `null` values when performing calculations.

Definitions noted with a :octicons-dot-16: are only supported in a statement with a `GROUP BY` clause.

New aggregates for this version are annotated with the :octicons-star-16: icon.

## General Functions

!!! function "`ANY_VALUE` (**column**) → _any_"  
    Select any single value from the grouping.  

!!! function "`ARRAY_AGG` ([DISTINCT] **column**) → _array_ :octicons-dot-16:"   
    The list of values for **column** in the group. The **DISTINCT* modifier optionally filters to unique values only. 
    ** :octicons-star-16: New in 0.7** 

!!! function "`APPROXIMATE_MEDIAN` (**column**: _numeric_) → _numeric_"  
    Approximate median of a column with T-Digest algorithm.

!!! function "`AVG` (**column**: _numeric_) → _numeric_"  
    The mean average of a numeric column.   
    Also `MEAN` and `AVERAGE`.

!!! function "`COUNT` (*) → _numeric_"  
    Count the number of rows.

!!! function "`COUNT` (**column**) → _numeric_"  
    Count the number of non `null` values in **column**.

!!! function "`COUNT_DISTINCT` (**column**) → _numeric_"  
    Count the number of unique values.

!!! function "`LIST` (**column**) → _array_ :octicons-dot-16:"  
    The complete list of values for **column** in the group.
    Related `ARRAY_AGG`

!!! function "`MAX` (**column**) → _any_"  
    The maximum value in **column**.  
    Also `MAXIMUM`.

!!! function "`MIN` (**column**) → _any_"  
    The minimum value in **column**.  
    Also `MINIMUM`.

!!! function "`MIN_MAX` (**column**) → _struct_"  
    The minimum and maximum values in **column**.  

!!! function "`ONE` (**column**) → _any_"  
    Alias for 'ANY_VALUE'()  

!!! function "`PRODUCT` (**column**: _numeric_) → _numeric_"  
    The product of values in **column**.  

!!! function "`STDDEV` (**column**: _numeric_) → _numeric_"  
    The standard deviation of values in **column**.  

!!! function "`SUM` (**column**: _numeric_) → _numeric_"  
    The sum of values in **column**.  

!!! function "`VARIANCE` (**column**: _numeric_) → _numeric_"  
    The variance of values in **column**.  

