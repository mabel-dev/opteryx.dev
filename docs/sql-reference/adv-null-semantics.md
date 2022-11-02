# NULL Semantics

Most comparisons to `null` return `null`.

~~~sql
WHERE a IS NOT b
~~~
and
~~~sql
WHERE NOT a IS b
~~~

Appear to be identical however, produce different results when `null` values are encountered. 

Condition          | a      | b      | result
------------------ | ------ | ------ | ---------
`WHERE a != b`     | _true_ | _null_ | _true_
`WHERE NOT a = b`  | _true_ | _null_ | _false_