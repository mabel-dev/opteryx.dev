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