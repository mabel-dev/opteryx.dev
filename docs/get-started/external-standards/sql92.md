---
title: ANSI SQL-92 Compliance - SQL Standard Support
description: Opteryx SQL-92 standard compliance. Supported SQL features, statements, and ANSI SQL conformity level.
---

# ANSI SQL-92 Conformity

!!! Note   
    The Opteryx maintainers author this page as a living attestation of the engine’s SQL-92 capabilities. We update it as features land so users have a current statement of support straight from the builders.

For a system to [attest to supporting SQL][^1] it should demonstrate strong conformance to the [ANSI SQL-92](https://db.cs.cmu.edu/files/sql/sql1992.txt) standard, also published as [ISO/IEC 9075:1992](https://www.iso.org/standard/16663.html).

We attest that Opteryx targets the slice of SQL-92 needed for analytical `SELECT` workloads. The engine is intentionally read-only; transactional language, DDL, and privilege statements fall outside its charter.

## Purpose and Scope

This declaration is meant to:

- **State support** – Outline, in our own words, which SQL-92 features Opteryx already delivers.
- **Share intent** – Call out the features we purposefully omit (read-only focus) vs. those still in development.
- **Guide adopters** – Let users plan with confidence, knowing the data interface we stand behind today.

## Attestation Snapshot

- **Query surface area** – We implement the SQL-92 constructs required for expressive `SELECT` statements: set operations, joins, aggregations, scalar expressions, and UNNEST flows. Mutating statements and privilege control remain intentionally out of scope.
- **Test coverage** – Every feature listed here is exercised in the automated suites (`test_battery_sql92.py`, `test_shapes_basic.py`, `test_shapes_aliases_distinct.py`, `test_shapes_joins_subqueries.py`, etc.), which we run continuously across connectors and data sources.
- **Execution model** – We compile each statement into a read-only plan that federates local files, remote object stores, DuckDB snapshots, and registered virtual datasets. The same SQL applies regardless of backing storage.

## Attested Feature Coverage

Feature family | SQL-92 references | Support | Implementation notes / evidence
:-- | :-- | :-- | :--
Core projection & filtering | E051, E061, E131 | yes | `SELECT`, `DISTINCT`, aliasing, `WHERE`, `BETWEEN`, `IN` lists, `LIKE`/`ILIKE`, boolean logic, and `IS [NOT] NULL` semantics are exercised in `test_shapes_basic.py` and `test_battery_sql92.py`.
Grouping & aggregates | E051, E091, F131 | yes | `GROUP BY`, `HAVING`, and aggregates (`AVG/COUNT/ MIN/MAX/SUM`, `ARRAY_AGG`, `COUNT(DISTINCT)`) plus `time_bucket`/`DATE_TRUNC` helpers validated in `test_shapes_functions_aggregates.py` and alias/joins battery tests.
Joins & FROM clause | E031, F041 | yes | Planner supports `INNER`, `LEFT/RIGHT/FULL OUTER`, `CROSS`, `NATURAL`, `USING`, semi/anti joins, and `UNNEST`, proven via `test_shapes_aliases_distinct.py`, `test_shapes_edge_cases.py`, and `test_shapes_joins_subqueries.py`.
Set operations | E071 | partial | `UNION DISTINCT` and `UNION ALL` (with LIMIT/OFFSET pushdown) are covered extensively. `INTERSECT`/`EXCEPT` raise `UnsupportedSyntaxError` (`test_shapes_joins_subqueries.py`).
Subqueries & CTEs | E051, E061 | partial | Subqueries are supported in the `FROM` clause and scalar select lists; correlated subqueries, `EXISTS`, and `IN (SELECT ...)` predicates remain unsupported (see disabled cases in `test_shapes_joins_subqueries.py`).
Scalar expressions & data types | E011, E021, F201, F261 | partial | Integer/decimal/double arithmetic, implicit numeric casts, string literals, concatenation, `SUBSTRING`, `TRIM`, `POSITION`, case folding, `CASE`, `COALESCE`, `NULLIF`, and regex helpers are implemented. `CHARACTER_LENGTH`, `OCTET_LENGTH`, and full fixed-length character semantics are not yet provided (`test_battery_sql92.py`).
Temporal literals & functions | F051 | partial | `DATE`/`TIMESTAMP` literals, `CURRENT_DATE/TIME/TIMESTAMP`, comparisons, `CAST` to/from text, `EXTRACT`, `DATE_TRUNC`, `time_bucket`, and `FOR 'timestamp'` filters are supported. Native `TIME` literals with fractional seconds and `LOCALTIMESTAMP` parity need additional work.
Null handling & search conditions | E061, E131, F261 | yes | Logical combinations with NULL, `CASE`, `COALESCE`, `NULLIF`, and null-aware predicates are verified in `test_shapes_aliases_distinct.py` and `test_null_semantics.py`.
Views & virtual datasets | F031/F081 | partial | Static (configuration-backed) views are queryable, but SQL `CREATE VIEW`, `ALTER`, and `INFORMATION_SCHEMA` discovery are not exposed.
Privileges, DML, DDL, transactions | E081, E101, E151, F031 | n/a | Opteryx operates as a read-only analytics engine—no `INSERT/UPDATE/DELETE`, `COMMIT/ROLLBACK`, `GRANT/REVOKE`, or schema statements.

Support statuses used above:

- **yes** – Feature is implemented and covered by automated tests.
- **partial** – Core behavior works, but specific SQL-92 sub-features (e.g., ESCAPE clauses, correlated subqueries) are still missing.
- **no** – Explicitly unsupported; the parser/planner raises an error.
- **n/a** – Out of scope for Opteryx’s read-only design.

## Maintainers’ Statement

We stand behind Opteryx’s SQL-92 coverage for analytical use cases:

- **Analytical focus** – Complex projection, filtering, grouping, joins, unions, and UNNEST paths are native features we rely on internally and validate through regression.
- **Rich expression support** – Arithmetic, string functions, CASE logic, JSON search operators, and datetime helpers are first-class citizens in the execution engine.
- **Storage flexibility** – The same SQL applies to tables, registered views, DuckDB snapshots, cloud object stores, and ad-hoc virtual datasets, with the planner handling pushdown where possible.

We also call out, by design or by pending work, the features still outside the supported set:

- **Correlated subqueries / EXISTS / IN (SELECT …)** – Not yet implemented; we recommend rewriting them as joins or set operations today.
- **INTERSECT / EXCEPT** – Raise `UnsupportedSyntaxError` until the set-operator stack is extended.
- **Character-length routines** – `CHARACTER_LENGTH`/`OCTET_LENGTH` remain queued behind ongoing string-function improvements.
- **Information schema / privilege statements** – Metadata inspection and access control are exposed via configuration APIs rather than SQL.
- **DML/DDL/Transactions** – Opteryx is purpose-built for read-only analytics, so mutating constructs are intentionally absent.

This statement represents the current capabilities of the engine. As we land new SQL-92 features we will update this page so the attestation remains accurate.  


[^1]: https://15445.courses.cs.cmu.edu/fall2020/slides/02-advancedsql.pdf