# ANSI SQL-92 Conformity

For a system to [attest to supporting SQL][^1] it must have good conformance to the [ANSI SQL-92](https://db.cs.cmu.edu/files/sql/sql1992.txt) standard. This standard is also known as [ISO/IEC 9075:1992](https://www.iso.org/standard/16663.html).

Opteryx is not a DBMS, so only aims for confirmity to the subset of SQL-92 for to featureset it supports - this is primarily related to `SELECT` statements.

Function | Description                                               | Support
:------- | :-------------------------------------------------------- | :---------
**E011** | **Numeric data types**                                    | partial
E011-01	 | `INTEGER` and `SMALLINT` data types                       | yes
E011-02  | `REAL`, `DOUBLE PRECISION`, and `FLOAT` data types        | partial
E011-03  | `DECIMAL` and `NUMERIC` data                              | unknown
E011-04  | Arithmetic                                                | yes
E011-05  | Numeric comparison                                        | yes
E011-06  | Implicit casting among the numeric data types             | yes
**E021** | **Character string types**                                | unknown
E021-01  | `CHARACTER` data type                                     | unknown
E021-02  | `CHARACTER VARYING` data type                             | unknown
E021-03  | Character literals                                        | unknown
E021-04  | `CHARACTER_LENGTH` function                               | no
E021-05  | `OCTET_LENGTH`                                            | no
E021-06  | `SUBSTRING` function                                      | partial
E021-07  | Character concatenation                                   | yes
E021-08  | `UPPER` and `LOWER` functions                             | yes
E021-09  | `TRIM` function                                           | unknown
E021-10  | Implicit casting among the fixed-length and variable-length character string types | unknown
E021-11  | `POSITION` function                                       | no
E021-12  | Character comparison                                      | yes
**E031** | **Identifiers**                                           | unknown
E031-01  | Delimited identifiers                                     | unknown
E031-02  | Lower case identifiers                                    | unknown
E031-03  | Trailing underscore                                       | unknown
**E051** | **Basic query specification**                             | unknown
E051-01  | `SELECT DISTINCT`                                         | unknown
E051-02  | `GROUP BY` clause                                         | unknown
E051-04  | `GROUP BY` can contain columns not in select-list         | unknown
E051-05  | Select list items can be renamed                          | unknown
E051-06  | `HAVING` clause                                           | unknown
E051-07  | Qualified `*` in select list                              | unknown
E051-08  | Correlation names in the `FROM` clause                    | unknown
E051-09  | Rename columns in the `FROM` clause                       | unknown
**E061** | **Basic predicates and search conditions**                | unknown
E061-01  | Comparison predicate                                      | unknown
E061-02  | `BETWEEN` predicate                                       | unknown
E061-03  | `IN` predicate with list of values                        | unknown
E061-04  | `LIKE` predicate                                          | unknown
E061-05  | `LIKE` predicate: `ESCAPE` clause                         | unknown
E061-06  | `NULL` predicate                                          | unknown
E061-07  | Quantified comparison predicate                           | unknown
E061-08  | `EXISTS` predicate                                        | no
E061-09  | Subqueries in comparison predicate                        | unknown
E061-11  | Subqueries in `IN` predicate                              | unknown
E061-12  | Subqueries in quantified comparison predicate             | unknown
E061-13  | Correlated subqueries                                     | unknown
E061-14  | Search condition                                          | unknown
**E071** | **Basic query expressions**                               | unknown
E071-01  | `UNION DISTINCT` table operator                           | no
E071-02  | `UNION ALL` table operator                                | no
E071-03  | `EXCEPT DISTINCT` table operator                          | no
E071-05  | Columns combined via table operators need not have exactly the same data type | unknown
E071-06  | Table operators in subqueries                             | unknown
**E081** | **Basic Privileges**                                      | unknown
E081-01  | `SELECT` privilege at the table level                     | unknown
E081-02  | `DELETE` privilege                                        | n/a
E081-03  | `INSERT` privilege at the table level                     | n/a
E081-04  | `UPDATE` privilege at the table level                     | n/a  
E081-05  | `UPDATE` privilege at the column level                    | n/a
E081-06  | `REFERENCES` privilege at the table level                 | unknown
E081-07  | `REFERENCES` privilege at the column level                | unknown
E081-08  | `WITH GRANT OPTION`                                       | no
E081-09  | `USAGE` privilege                                         | unknown
E081-10  | `EXECUTE` privilege                                       | unknown
**E091** | **Set functions**                                         | unknown
E091-01  | `AVG`                                                     | unknown
E091-02  | `COUNT`                                                   | unknown
E091-03  | `MAX`                                                     | unknown
E091-04  | `MIN`                                                     | unknown
E091-05  | `SUM`                                                     | unknown
E091-06  | `ALL` quantifier                                          | unknown
E091-07  | `DISTINCT` quantifier                                     | unknown
**E101** | **Basic data manipulation**                               | n/a
E101-01  | `INSERT` statement                                        | n/a
E101-03  | Searched `UPDATE` statement                               | n/a
E101-04  | Searched `DELETE` statement                               | n/a
**E111** | **Single row SELECT statement**                           | unknown
**E121** | **Basic cursor support**                                  | unknown
E121-01  | `DECLARE CURSOR`                                          | no
E121-02  | `ORDER BY` columns need not be in select                  | unknown
E121-03  | Value expressions in `ORDER BY` clause                    | unknown
E121-04  | `OPEN` statement                                          | unknown
E121-06  | Positioned `UPDATE` statement                             | no
E121-07  | Positioned `DELETE` statement                             | no
E121-08  | `CLOSE` statement                                         | no
E121-10  | `FETCH` statement: implicit `NEXT`                        | no
E121-17  | `WITH HOLD` cursors                                       | no
**E131** | **Null value support**                                    | unknown
**E141** | **Basic integrity constraints**                           | unknown
E141-01  | `NOT NULL` constraints                                    | unknown
E141-02  | `UNIQUE` constraints of `NOT NULL`                        | unknown
E141-03  | `PRIMARY KEY` constraints                                 | unknown
E141-04  | Basic `FOREIGN KEY` constraint with the `NO ACTION` default for both referential delete action and referential update action | unknown
E141-06  | `CHECK` constraints                                       | unknown
E141-07  | Column defaults                                           | unknown
E141-08  | `NOT NULL` inferred on `PRIMARY KEY`                      | unknown
E141-10  | Names in a foreign key can be specified in any order      | unknown
**E151** | **Transaction support**                                   | n/a
E151-01  | `COMMIT` statement                                        | n/a
E151-02  | `ROLLBACK` statement                                      | n/a
**E152** | **Basic `SET TRANSACTION` statement**                     | n/a
E152-01  | `SET TRANSACTION` statement: `ISOLATION LEVEL SERIALIZABLE` clause   | n/a
E152-02  | `SET TRANSACTION` statement: `READ ONLY` and `READ WRITE` clauses    | n/a
**E+**   | **Other**                                                 | unknown
**E153** | **Updatable queries with subqueries**                     | unknown
**E161** | **SQL comments using leading double minus**               | yes
**E171** | **`SQLSTATE` support**                                    | unknown
**E182** | **Host language binding**                                 | unknown
**F021** | **Basic information schema**                              | unknown
F021-01  | `COLUMNS` view                                            | unknown
F021-02  | `TABLES` view                                             | unknown
F021-03  | `VIEWS` view                                              | unknown
F021-04  | `TABLE_CONSTRAINTS` view                                  | unknown
F021-05  | `REFERENTIAL_CONSTRAINTS` view                            | unknown
F021-06  | `CHECK_CONSTRAINTS` view                                  | unknown
**F031** | **Basic schema manipulation**                             | unknown
F031-01  | `CREATE TABLE` statement to create persistent base tables | n/a
F031-02  | `CREATE VIEW` statement                                   | n/a
F031-03  | `GRANT` statement                                         | unknown
F031-04  | `ALTER TABLE` statement: `ADD COLUMN` clause              | n/a
F031-13  | `DROP TABLE` statement: `RESTRICT` clause                 | n/a
F031-16  | `DROP VIEW` statement: `RESTRICT` clause                  | n/a
F031-19  | `REVOKE` statement: `RESTRICT` clause                     | unknown
**F041** | **Basic joined table**                                    | unknown
F041-01  | Inner join (but not necessarily the `INNER` keyword)      | unknown
F041-02  | `INNER` keyword                                           | unknown
F041-03  | `LEFT OUTER JOIN`                                         | unknown
F041-04  | `RIGHT OUTER JOIN`                                        | unknown
F041-05  | Outer joins can be nested                                 | unknown
F041-07  | The inner table in a left or right outer join can also be used in an inner join   | unknown
F041-08  | All comparison operators are supported (rather than just `=`)                     | unknown
**F051** | **Basic date and time**                                   | unknown
F051-01  | `DATE` data type (including support of `DATE` literal)    | unknown
F051-02  | `TIME` data type (including support of `TIME` literal) with fractional seconds    | unknown
F051-03  | `TIMESTAMP` data type (including support of `TIMESTAMP` literal) with fractional seconds precision of at least 0 and 6   | unknown
F051-04  | Comparison predicate on `DATE`, `TIME`, and `TIMESTAMP` data types   | partial
F051-05  | Explicit `CAST` between datetime types and character string types    | unknown
F051-06  | `CURRENT_DATE`                                            | yes
F051-07  | `LOCALTIME`                                               | unknown
F051-08  | `LOCALTIMESTAMP`                                          | unknown
**F081** | **`UNION` and `EXCEPT` in views**                         | unknown
**F131** | **Grouped operations**                                    | unknown
F131-01  | `WHERE`, `GROUP BY`, and `HAVING` clauses supported in queries with grouped views   | unknown
F131-02  | Multiple tables supported in queries with grouped views   | unknown
F131-03  | Set functions supported in queries with grouped views     | unknown
F131-04  | Subqueries with `GROUP BY` and `HAVING` clauses and grouped views   | unknown
F131-05  | Single row `SELECT` with `GROUP BY` and `HAVING` clauses and grouped views    | unknown
**F181** | **Multiple module support**                               | unknown
**F201** | **`CAST` function**                                       | unknown
**F221** | **Explicit defaults**                                     | unknown
**F261** | **`CASE` expression**                                     | no
F261-01  | Simple `CASE`                                             | no
F261-02  | Searched `CASE`                                           | no
F261-03  | `NULLIF`                                                  | yes
F261-04  | `COALESCE`                                                | yes
**F311** | **Schema definition statement**                           | n/a
F311-01  | `CREATE SCHEMA`                                           | n/a
F311-02  | `CREATE TABLE`                                            | n/a
F311-03  | `CREATE VIEW`                                             | n/a
F311-04  | `CREATE VIEW`: `WITH CHECK OPTION`                        | n/a
F311-05  | `GRANT` statement                                         | n/a
**F471** | **Scalar subquery values**                                | unknown
**F481** | **Expanded `NULL` predicate**                             | unknown
**F501** | **Features and conformance views**                        | unknown
F501-01  | `SQL_FEATURES` view                                       | unknown
F501-02  | `SQL_SIZING` view                                         | unknown
F501-03  | `SQL_LANGUAGES` view                                      | unknown
**F812** | **Basic flagging**                                        | unknown
**S011** | **Distinct data types**                                   | unknown
S011-01  | `USER_DEFINED_TYPES` view                                 | no
**T321** | **Basic SQL-invoked routines**                            | unknown
T321-01  | User-defined functions with no overloading                | unknown
T321-02  | User-defined stored procedures with no overloading        | unknown
T321-03  | Function invocation                                       | unknown
T321-04  | `CALL` statement                                          | unknown
T321-05  | `RETURN` statement                                        | unknown
T321-06  | `ROUTINES` view                                           | unknown
T321-07  | `PARAMETERS` view                                         | unknown
**T631** | **`IN` predicate with one list element**                  | unknown

Support statuses in this table:

&emsp;**yes** - The feature is supported and conformance is part of the test suite.  
&emsp;**no** - The feature is not supported.  
&emsp;**partial** - Some features are supported.  
&emsp;**n/a** - The feature relates to a feature not supported by Opteryx.  
&emsp;**unknown** - No test exists to confirm conformance.  


[^1]: https://15445.courses.cs.cmu.edu/fall2020/slides/02-advancedsql.pdf