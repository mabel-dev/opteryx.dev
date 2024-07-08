# Changelog

All notable changes to this project will be documented in this file, where appropriate the GitHub issue reference will be noted along with the change. Breaking changes will be clearly indicated with the :octicons-alert-24: icon.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.15.9] - 2024-06-29

### Added

- [[#1778](https://github.com/mabel-dev/opteryx/issues/1778)] Specialized `INNER JOIN` operator for `INTEGERS` and `VARCHARS` [@joocer](https://github.com/joocer)
- [[#1768](https://github.com/mabel-dev/opteryx/issues/1768)] Date calculation predicate rewriter (optimizer) [@joocer](https://github.com/joocer)

### Fixed

- [[#1788](https://github.com/mabel-dev/opteryx/issues/1788)] Errors reading files reported as SQL syntax errors. [@joocer](https://github.com/joocer)

## [0.15.8] - 2024-06-29

### Added

- [[#1763](https://github.com/mabel-dev/opteryx/issues/1763)] Support `@?` JSON Accessor [@joocer](https://github.com/joocer)
- [[#1670](https://github.com/mabel-dev/opteryx/issues/1670)] Inital [Tarchia](https://github.com/mabel-dev/tarchia) catalog support [@joocer](https://github.com/joocer)

### Fixed

- [[#1700](https://github.com/mabel-dev/opteryx/issues/1700)] Mac versions not building and publishing to PyPI [@joocer](https://github.com/joocer)

## [0.15.5] - 2024-06-18

### Changed

- [[#1759](https://github.com/mabel-dev/opteryx/issues/1759)] `->` and `->>` operators able to parse JSON strings and bytes [@joocer](https://github.com/joocer)

## [0.15.4] - 2024-06-17

### Added

- [[#1746](https://github.com/mabel-dev/opteryx/issues/1746)] Support legacy Mabel LZMA compressed JSONL files [@joocer](https://github.com/joocer)
- [[#1748](https://github.com/mabel-dev/opteryx/issues/1748)] S3/MinIO Connector supports async reads [@joocer](https://github.com/joocer)

### Changed

- [[#1714](https://github.com/mabel-dev/opteryx/issues/1714)] [ClickBench] `GROUP BY` literals [@joocer](https://github.com/joocer)
- [[#1696](https://github.com/mabel-dev/opteryx/issues/1696)] Prevent predicates being pushed past limits [@joocer](https://github.com/joocer)
- [[#1753](https://github.com/mabel-dev/opteryx/issues/1753)] Error on `SELECT TOP` syntax [@joocer](https://github.com/joocer)

### Fixed

- [[#1756](https://github.com/mabel-dev/opteryx/issues/1756)] Sort incorrectly returning zero records when first morsel is empty [@joocer](https://github.com/joocer)

## [0.15.3] - 2024-06-06

### Changed

- [[#1715](https://github.com/mabel-dev/opteryx/issues/1715)] More optimizations `AND`, `OR` and `XOR` aware  [@joocer](https://github.com/joocer)
- [[#1717](https://github.com/mabel-dev/opteryx/issues/1717)] Memcahed notified when resource read from local buffers [@joocer](https://github.com/joocer)

## [0.15.1] - 2024-05-31

### Added 

- [[#1685](https://github.com/mabel-dev/opteryx/issues/1685)] [ClickBench] Include `BLOB` as column types for predicate pushdowns [@joocer](https://github.com/joocer)
- [[#1697](https://github.com/mabel-dev/opteryx/issues/1697)] [ClickBench] Optimizer removes redundant operators [@joocer](https://github.com/joocer)
- [[#1698](https://github.com/mabel-dev/opteryx/issues/1698)] [ClickBench] Replace `LIKE` conditions with `STARTS_WITH` and `ENDS_WITH` functions [@joocer](https://github.com/joocer)
- [[#1581](https://github.com/mabel-dev/opteryx/issues/1581)] `ANY` operator supports literal lists [@joocer](https://github.com/joocer)
- [[#1690](https://github.com/mabel-dev/opteryx/issues/1690)] Support `REGEXP_REPLACE` function [@joocer](https://github.com/joocer)

## [0.15.0] - 2024-05-26

### Added

- [[#723](https://github.com/mabel-dev/opteryx/issues/723)] Initial `MATCH AGAINST` support. [@joocer](https://github.com/joocer)
- [[#346](https://github.com/mabel-dev/opteryx/issues/346)] Permissions Model. [@joocer](https://github.com/joocer)  
- [[#1582](https://github.com/mabel-dev/opteryx/issues/1582)] Lemmatize full text searches [@joocer](https://github.com/joocer)
- [[#1584](https://github.com/mabel-dev/opteryx/issues/1584)] Additional Statistics [@joocer](https://github.com/joocer)
- [[#1590](https://github.com/mabel-dev/opteryx/issues/1590)] Push filters into sub queries [@joocer](https://github.com/joocer)
- [[#1588](https://github.com/mabel-dev/opteryx/issues/1588)] Push filters into `UNNEST` [@joocer](https://github.com/joocer)
- [[#1613](https://github.com/mabel-dev/opteryx/issues/1613)] Parallelize reads of GCS storage [@joocer](https://github.com/joocer)
- [[#1652](https://github.com/mabel-dev/opteryx/issues/1652)] `BLOB` and `VARCHAR` values can be compared [@joocer](https://github.com/joocer)
- [[#1666](https://github.com/mabel-dev/opteryx/issues/1666)] Heap Sort fused operator (`LIMIT` and `ORDER BY` implemented) [@joocer](https://github.com/joocer)
- [[#1665](https://github.com/mabel-dev/opteryx/issues/1665)] Smart buffer size allocations [@joocer](https://github.com/joocer)
- [[#1676](https://github.com/mabel-dev/opteryx/issues/1676)] b-prefixed blob literals [@joocer](https://github.com/joocer)
- [[#1586](https://github.com/mabel-dev/opteryx/issues/1586)] Initial VIEWs functionality [@joocer](https://github.com/joocer)

### Changed

- [[#1550](https://github.com/mabel-dev/opteryx/issues/1550)] Additional Statistics [@joocer](https://github.com/joocer)
- [[#731](https://github.com/mabel-dev/opteryx/issues/731)] Buffer Pool Statistics [@joocer](https://github.com/joocer)
- [[#1604](https://github.com/mabel-dev/opteryx/issues/1604)] Internal 'Node' object performance [@joocer](https://github.com/joocer)
- [[#1643](https://github.com/mabel-dev/opteryx/issues/1643)] Mabel Planning Improvements [@joocer](https://github.com/joocer)

### Fixed

- [[#1587](https://github.com/mabel-dev/opteryx/issues/1587)] Filtering on `CROSS JOIN UNNEST` columns pushed too far. [@joocer](https://github.com/joocer)
- [[#1592](https://github.com/mabel-dev/opteryx/issues/1592)] Prevent `RANDOM` being evaluated once in optimizer. [@joocer](https://github.com/joocer)
- [[#1598](https://github.com/mabel-dev/opteryx/issues/1598)] Buffer Pool inefficiencies. [@joocer](https://github.com/joocer)
- [[#1620](https://github.com/mabel-dev/opteryx/issues/1620)] Failure to set in Memcache shouldn't be fatal. [@joocer](https://github.com/joocer)
- [[#1622](https://github.com/mabel-dev/opteryx/issues/1622)] Incorrect handling of nulls in JOIN conditions. [@joocer](https://github.com/joocer)
- [[#1664](https://github.com/mabel-dev/opteryx/issues/1664)] Memory Pool stats not correct [@joocer](https://github.com/joocer)
- [[#1674](https://github.com/mabel-dev/opteryx/issues/1674)] Errors with large chunks [@joocer](https://github.com/joocer)


## [0.14.1] - 2024-04-13

### Added

- [[#1571](https://github.com/mabel-dev/opteryx/issues/1571)] Initial `COSINE_SIMILARITY` support (ad hoc). [@joocer](https://github.com/joocer)

### Fixed

- [[#1573](https://github.com/mabel-dev/opteryx/issues/1573)] Parquet `COUNT(*)` returns unfiltered row count. [@joocer](https://github.com/joocer)

## [0.14.0] - 2024-04-07

### Added

- [[#1460](https://github.com/mabel-dev/opteryx/issues/1460)] Support PyArrow's IPC formated files. [@joocer](https://github.com/joocer)
- [[#1464](https://github.com/mabel-dev/opteryx/issues/1464)] `LIKE` with no wildcards rewritten as `=` [@joocer](https://github.com/joocer)
- [[#1468](https://github.com/mabel-dev/opteryx/issues/1468)] Python 3.12 support [@joocer](https://github.com/joocer)
- [[#1459](https://github.com/mabel-dev/opteryx/issues/1459)] Primitive support for `EXECUTE` queries [@joocer](https://github.com/joocer)
- [[#1479](https://github.com/mabel-dev/opteryx/issues/1479)] Unary (`IS TRUE`) operators pushed to SQL sources [@joocer](https://github.com/joocer)
- [[#540](https://github.com/mabel-dev/opteryx/issues/540)] Initial support for JSON Accessors `->` and `->>`. [@joocer](https://github.com/joocer)
- [[#1499](https://github.com/mabel-dev/opteryx/issues/1499)] Error when `EXECUTE USING` syntax is attempted. [@joocer](https://github.com/joocer)
- [[#1491](https://github.com/mabel-dev/opteryx/issues/1491)] New test dataset `$missions`. [@joocer](https://github.com/joocer)
- [[#1300](https://github.com/mabel-dev/opteryx/issues/1300)] Support named Parameters. [@joocer](https://github.com/joocer)
- [[#1516](https://github.com/mabel-dev/opteryx/issues/1516)] Day of Week placeholders for temporal queries. [@joocer](https://github.com/joocer)
- [[#1563](https://github.com/mabel-dev/opteryx/issues/1563)] Add support for Cassandra-based sources[@joocer](https://github.com/joocer)

### Changed

- [[#1448](https://github.com/mabel-dev/opteryx/issues/1448)] Improved error message on `GROUP BY` errors. [@joocer](https://github.com/joocer)
- [[#1447](https://github.com/mabel-dev/opteryx/issues/1447)] Levenshtein implementation rewritten. [@joocer](https://github.com/joocer)
- [[#1451](https://github.com/mabel-dev/opteryx/issues/1451)] Improved IP containment testing performance. [@joocer](https://github.com/joocer)
- [[#1410](https://github.com/mabel-dev/opteryx/issues/1410)]  + [[#190](https://github.com/mabel-dev/opteryx/issues/190)] Rewrite `INNER JOIN` [@joocer](https://github.com/joocer)
- [[#1481](https://github.com/mabel-dev/opteryx/issues/1481)] Improvements to `DATE` +/- `INTERVAL` performance. [@joocer](https://github.com/joocer)
- [[#1486](https://github.com/mabel-dev/opteryx/issues/1486)] Implement bespoke `INTERVAL` operators [@joocer](https://github.com/joocer)
- [[#1535](https://github.com/mabel-dev/opteryx/issues/1535)] Native implementation of `LEFT JOIN` [@joocer](https://github.com/joocer)
- [[#1547](https://github.com/mabel-dev/opteryx/issues/1547)] Buffer Pool implemented using a Memory Pool [@joocer](https://github.com/joocer)

### Fixed

- [[#1462](https://github.com/mabel-dev/opteryx/issues/1462)] Unhandled exception on empty datasets. [@joocer](https://github.com/joocer)
- [[#1465](https://github.com/mabel-dev/opteryx/issues/1465)] Clashing column names not aliased correctly. [@joocer](https://github.com/joocer)
- :octicons-alert-24: [[#1445](https://github.com/mabel-dev/opteryx/issues/1445)] `SHOW EXTENDED COLUMNS` not working as expected - changes made to data profile format. [@joocer](https://github.com/joocer)
- [[#1473](https://github.com/mabel-dev/opteryx/issues/1473)] `INNER JOIN` statistics not correct. [@joocer](https://github.com/joocer)
- [[#1474](https://github.com/mabel-dev/opteryx/issues/1474)] Unhelpful error message when `SELECT *` is mixed with column references [@joocer](https://github.com/joocer)
- [[#1487](https://github.com/mabel-dev/opteryx/issues/1487)] Filters are not applied to scans on specific conditions involving `JOIN`s [@joocer](https://github.com/joocer)
- [[#1480](https://github.com/mabel-dev/opteryx/issues/1480)] `INTERVAL` cannot be compared to durations [@joocer](https://github.com/joocer)
- [[#1485](https://github.com/mabel-dev/opteryx/issues/1485)] Improved handling of `COUNT(*)` when pushing to parquet and SQL [@joocer](https://github.com/joocer)
- [[#1513](https://github.com/mabel-dev/opteryx/issues/1513)] `LIST_CONTAINS_ANY` performance [@joocer](https://github.com/joocer)

## [0.13.3] - 2024-02-13

### Added

- [[#1427](https://github.com/mabel-dev/opteryx/issues/1427)] Boolean simplification optimization strategy. [@joocer](https://github.com/joocer)

### Fixed

- [[#1413](https://github.com/mabel-dev/opteryx/issues/1413)] Regression test failures on Windows. [@joocer](https://github.com/joocer)
- [[#1320](https://github.com/mabel-dev/opteryx/issues/1320)] Errors due to binding memoization. [@joocer](https://github.com/joocer)
- [[#1433](https://github.com/mabel-dev/opteryx/issues/1433)] [Bandit](https://bandit.readthedocs.io/en/latest/index.html) tests misconfigured. [@joocer](https://github.com/joocer)

### Changes

- [[#1421](https://github.com/mabel-dev/opteryx/issues/1421)] Improve `CROSS JOIN UNNEST` performance. [@joocer](https://github.com/joocer)
- [[#1410](https://github.com/mabel-dev/opteryx/issues/1410)] Whilst working on `JOIN` improvements, improvements to `DISTINCT` made. [@joocer](https://github.com/joocer)
- Refactored SQL Fuzzer regression test script. [@joocer](https://github.com/joocer)

## [0.13.0] - 2024-02-03

### Added

- [[#1404](https://github.com/mabel-dev/opteryx/issues/1404)] Optimize single element literal `IN` conditions [@joocer](https://github.com/joocer)

### Fixed

- [[#1402](https://github.com/mabel-dev/opteryx/issues/1402)] Force consistent blob read order. [@joocer](https://github.com/joocer)
- [[#1391](https://github.com/mabel-dev/opteryx/issues/1391)] Rolling Log doesn't truncate records. [@joocer](https://github.com/joocer)
- [[#1395](https://github.com/mabel-dev/opteryx/issues/1395)] Incorrect error raised on type errors on `JOIN`s. [@joocer](https://github.com/joocer)
- [[#1397](https://github.com/mabel-dev/opteryx/issues/1397)] Subscript `SPLIT` results. [@joocer](https://github.com/joocer)
- [[#1379](https://github.com/mabel-dev/opteryx/issues/1379)] Unable to run on ARM. [@joocer](https://github.com/joocer)
- [[#1183](https://github.com/mabel-dev/opteryx/issues/1183)] `JOIN` on literals fails. [@joocer](https://github.com/joocer)

### Changed

- [[#1374](https://github.com/mabel-dev/opteryx/issues/1374)] GCS access improvements (up to 2.5x faster IO). [@joocer](https://github.com/joocer)
- [[#1393](https://github.com/mabel-dev/opteryx/issues/1393)] Performance Tuning blob reading. [@joocer](https://github.com/joocer)
- [[#1411](https://github.com/mabel-dev/opteryx/pull/1411)] Updated [sqlparser-rs](https://github.com/sqlparser-rs/sqlparser-rs) to version 0.43.1 [dependabot](https://github.com/apps/dependabot) 

## [0.12.2] - 2024-01-10

### Added

- [[#1355](https://github.com/mabel-dev/opteryx/issues/1355)] Shortcut `OR` evaluations [@joocer](https://github.com/joocer)
- [[#1363](https://github.com/mabel-dev/opteryx/issues/1363)] Shortcut nested `AND` evaluations [@joocer](https://github.com/joocer)
- [[#21](https://github.com/mabel-dev/opteryx/issues/21)] Support `UNION` statements [@joocer](https://github.com/joocer)
- [[#1354](https://github.com/mabel-dev/opteryx/issues/1354)] New Optimization: Constant Expression Evaluations [@joocer](https://github.com/joocer)

### Fixed

- [[#1370](https://github.com/mabel-dev/opteryx/issues/1370)] Compare `DATE` and `TIMESTAMP`. [@joocer](https://github.com/joocer)

### Changed

- [[#1366](https://github.com/mabel-dev/opteryx/issues/1355)] Subscript refactor for performance (~3x faster). [@joocer](https://github.com/joocer)

## [0.12.0] - 2024-01-02    

### Fixed

- [[#1080](https://github.com/mabel-dev/opteryx/issues/1080)] Windows regression test failures. [@joocer](https://github.com/joocer) 
- Soundex incorrectly evaluated empty strings as '0000'. [@joocer](https://github.com/joocer) 

### Changed

- [[#1083](https://github.com/mabel-dev/opteryx/issues/1083)] Simplify the handling of Query Statistics. [@joocer](https://github.com/joocer)
- [[#1086](https://github.com/mabel-dev/opteryx/pull/1086)] Update [Pythonize](https://github.com/davidhewitt/pythonize) to v0.19 and [py03](https://github.com/PyO3/pyo3) to v0.20.0 [dependabot](https://github.com/apps/dependabot) 
- [[#1042](https://github.com/mabel-dev/opteryx/pull/1042)] Create a generic base connector and use for all access [@joocer](https://github.com/joocer)
- [[#1032](https://github.com/mabel-dev/opteryx/pull/1032)] Introduce a query binder [@joocer](https://github.com/joocer)
- [[#1158](https://github.com/mabel-dev/opteryx/pull/1158)] Resync sqloxide [@joocer](https://github.com/joocer)

### Added

- [[#1117](https://github.com/mabel-dev/opteryx/pull/1117)] Cockroach Labs regression tests [@joocer](https://github.com/joocer)
- [[#1128](https://github.com/mabel-dev/opteryx/pull/1128)] Specialized handlers for `IS NOT TRUE` and `IS NOT FALSE` [@joocer](https://github.com/joocer)
- `DATES SINCE` temporal filter syntax added. [@joocer](https://github.com/joocer)  
- [[#1145](https://github.com/mabel-dev/opteryx/pull/1145)] Debug Logging [@joocer](https://github.com/joocer)
- [[#1156](https://github.com/mabel-dev/opteryx/pull/1156)] Bitwise operators and Hex literals [@joocer](https://github.com/joocer)  
- [[#1141](https://github.com/mabel-dev/opteryx/pull/1141)] BiQuery regression tests and documentation [@joocer](https://github.com/joocer)
- [[#1171](https://github.com/mabel-dev/opteryx/pull/1171)] Support `NATURAL JOIN` syntax [@joocer](https://github.com/joocer)  
- [[#1171](https://github.com/mabel-dev/opteryx/pull/1171)] Support `SEMI` and `ANTI` join syntax [@joocer](https://github.com/joocer)  
- [[#1219](https://github.com/mabel-dev/opteryx/pull/1219)] Extended `FAKE` syntax [@joocer](https://github.com/joocer)
- [[#1219](https://github.com/mabel-dev/opteryx/pull/1219)] `DISTINCT ON` syntax added [@joocer](https://github.com/joocer)
- [[#1339](https://github.com/mabel-dev/opteryx/pull/1339)] Updated [sqlparser-rs](https://github.com/sqlparser-rs/sqlparser-rs) to version 0.41.0 [dependabot](https://github.com/apps/dependabot) 
- [[#1329](https://github.com/mabel-dev/opteryx/pull/1329)] Add Redis as remote read cache option. [@joocer](https://github.com/joocer)
- [[#1337](https://github.com/mabel-dev/opteryx/pull/1337)] Support `RLIKE` [@joocer](https://github.com/joocer)
- [[#1344](https://github.com/mabel-dev/opteryx/pull/1344)] Initial Support for `ANY` and `ALL` array containment syntax [@joocer](https://github.com/joocer)

### Removed

- :octicons-alert-24: Python 3.8 is no longer supported. [@joocer](https://github.com/joocer)  

## [0.11.0] - 2023-06-16

### Fixed

- [[#1069](https://github.com/mabel-dev/opteryx/issues/1069)] Minor improvements identified during code review of code to generate numeric series. [@joocer](https://github.com/joocer) 
- [[#1072](https://github.com/mabel-dev/opteryx/issues/1072)] Minor improvements identified during code review of code to handle dates and intervals. [@joocer](https://github.com/joocer) 
- [[#1026](https://github.com/mabel-dev/opteryx/pull/1026)] Removed pin to version 0.11 of PyArrow [dependabot](https://github.com/apps/dependabot) 
- [[#1077](https://github.com/mabel-dev/opteryx/pull/1077)] Removed pin to version 0.7.1 of DuckDB [dependabot](https://github.com/apps/dependabot) 

### Changed

- [[#808](https://github.com/mabel-dev/opteryx/issues/808)] Rewrite of AST to Logical plan. [@joocer](https://github.com/joocer) 
- [[#1031](https://github.com/mabel-dev/opteryx/issues/1031)] `.to_df` deprecation complete. [@joocer](https://github.com/joocer) 
- [[#356](https://github.com/mabel-dev/opteryx/issues/356)] Prepositioning changes for extended types. [@joocer](https://github.com/joocer) 
- [[#1046](https://github.com/mabel-dev/opteryx/pull/1046)] Updated [sqlparser-rs](https://github.com/sqlparser-rs/sqlparser-rs) to version 0.34.0 [dependabot](https://github.com/apps/dependabot) 
- [[#1017](https://github.com/mabel-dev/opteryx/discussions/1017)] Fuzzy matching for suggestions is punctuation insensitive [@joocer](https://github.com/joocer) 
- [[#1060](https://github.com/mabel-dev/opteryx/issues/1060)] Conditional test execution made more explicit. [@joocer](https://github.com/joocer) 
- [[#1026](https://github.com/mabel-dev/opteryx/pull/1026)] Timeout FireStore connection. [@joocer](https://github.com/joocer) 

### Added

- [[#1034](https://github.com/mabel-dev/opteryx/issues/1034)] Schemas added for the internal sample datasets. [@joocer](https://github.com/joocer) 
- [[#1038](https://github.com/mabel-dev/opteryx/issues/1038)] Able to pass SqlAlchemy Engine to the SQL Connectors, allowing for more complex authentication scenarios. [@joocer](https://github.com/joocer) 
- [[#1065](https://github.com/mabel-dev/opteryx/issues/1065)] Support integer division operator `DIV`. [@joocer](https://github.com/joocer) 

## [0.10.0] - 2023-05-03

### Warnings

- `.to_df()` will be replaced with `.pandas()` in version 0.11.

### Fixed

- [[#929](https://github.com/mabel-dev/opteryx/issues/929)] Improved error messages for malformed temporal clauses. [@joocer](https://github.com/joocer) 
- :octicons-alert-24: [[#735](https://github.com/mabel-dev/opteryx/issues/735)] (correction) Cursor `fetchone` and `fetchmany` step over the record set. [@joocer](https://github.com/joocer)  
- [[#994](https://github.com/mabel-dev/opteryx/issues/994)] `LIMIT` didn't prevent additional files from being read after limit was met. [@joocer](https://github.com/joocer) 
- [[#996](https://github.com/mabel-dev/opteryx/issues/996)] Performance issues with `LIMIT` and serialization steps. [@joocer](https://github.com/joocer) 
- [[#1008](https://github.com/mabel-dev/opteryx/issues/1008)] `JOIN` on a literal fails when attempting to find good match. [@joocer](https://github.com/joocer) 
- [[#1006](https://github.com/mabel-dev/opteryx/issues/1006)] Errors handling filenames with multiple dots in the name. [@joocer](https://github.com/joocer) 
- [[#1010](https://github.com/mabel-dev/opteryx/issues/1010)] Predicates not pushed for ZSTD compressed files. [@joocer](https://github.com/joocer) 
- [[#1007](https://github.com/mabel-dev/opteryx/issues/1007)] Wildcards not interpretted correctly in some projection pushdowns [@joocer](https://github.com/joocer) 
- [[#1015](https://github.com/mabel-dev/opteryx/issues/1015)] Column comparisons not working as expected in predicate pushdowns [@joocer](https://github.com/joocer) 

### Changed

- [[#925](https://github.com/mabel-dev/opteryx/pull/925)] Updated [sqlparser-rs](https://github.com/sqlparser-rs/sqlparser-rs) to version 0.31.0 [dependabot](https://github.com/apps/dependabot) 
- :octicons-alert-24: [[#931](https://github.com/mabel-dev/opteryx/issues/931)] Cursor `fetch` no longer accept `asdict` parameter, instead each tuple (an [orso](https://github.com/mabel-dev/orso) Row) has an `as_dict` method [@joocer](https://github.com/joocer) 
- [[#906](https://github.com/mabel-dev/opteryx/issues/906)] Cursor extends an [orso](https://github.com/mabel-dev/orso) DataFrame, providing additional functionality [@joocer](https://github.com/joocer) 
- [[#938](https://github.com/mabel-dev/opteryx/pull/938)] Updated [sqlparser-rs](https://github.com/sqlparser-rs/sqlparser-rs) to version 0.32.0 [dependabot](https://github.com/apps/dependabot)  
- [[#940](https://github.com/mabel-dev/opteryx/issues/940)] CityHash moved to [orso](https://github.com/mabel-dev/orso).cityhash [@joocer](https://github.com/joocer) 
- [[#942](https://github.com/mabel-dev/opteryx/issues/942)] Profiler (and distogram) moved to [orso](https://github.com/mabel-dev/orso) [@joocer](https://github.com/joocer) 
- :octicons-alert-24: [[#965](https://github.com/mabel-dev/opteryx/issues/965)] (MySQL Compatibility) `SHOW STORES` renamed to `SHOW DATABASES` [@joocer](https://github.com/joocer) 
- [[#973](https://github.com/mabel-dev/opteryx/issues/973)] Improved readability of Sort nodes in `EXPLAIN` queries  [@joocer](https://github.com/joocer) 
- [[#984](https://github.com/mabel-dev/opteryx/pull/984)] Updated [sqlparser-rs](https://github.com/sqlparser-rs/sqlparser-rs) to version 0.33.0 [dependabot](https://github.com/apps/dependabot) 
- [[#999](https://github.com/mabel-dev/opteryx/issues/999)] Improved error messages when using subscript functions [@joocer](https://github.com/joocer) 
- [[#1019](https://github.com/mabel-dev/opteryx/issues/1019)] CircularLog renamed RollingLog [@joocer](https://github.com/joocer) 

### Added

- [[#952](https://github.com/mabel-dev/opteryx/issues/952)] Implement statement-based permissions model [@joocer](https://github.com/joocer) 
- [[#951](https://github.com/mabel-dev/opteryx/issues/951)] Initial Support for Prepared Statements (`EXECUTE` queries) [@joocer](https://github.com/joocer) 
- [[#958](https://github.com/mabel-dev/opteryx/issues/958)] Log of recent queries [@joocer](https://github.com/joocer) 
- [[#905](https://github.com/mabel-dev/opteryx/issues/905)] CLI includes REPL mode [@joocer](https://github.com/joocer) 
- [[#942](https://github.com/mabel-dev/opteryx/issues/942)] CLI has option to output to Markdown format [@joocer](https://github.com/joocer) 
- [[#967](https://github.com/mabel-dev/opteryx/issues/967)] Initial Information Schema capability [@joocer](https://github.com/joocer) 
- [[#978](https://github.com/mabel-dev/opteryx/issues/978)] Initial support for `USE` queries [@joocer](https://github.com/joocer) 
- [[#989](https://github.com/mabel-dev/opteryx/issues/989)] REPL supports limited dot commands `.help` and `.exit` [@joocer](https://github.com/joocer) 
- [[#991](https://github.com/mabel-dev/opteryx/issues/991)] Added `SPLIT` function [@joocer](https://github.com/joocer) 
- [[#969](https://github.com/mabel-dev/opteryx/issues/969)] New functions supporting Power BI integration [@joocer](https://github.com/joocer) 
- [[#999](https://github.com/mabel-dev/opteryx/issues/999)] `STRUCT` casting functions [@joocer](https://github.com/joocer) 
- [[#1003](https://github.com/mabel-dev/opteryx/issues/1003)] DuckDB compatibility tests [@joocer](https://github.com/joocer) 
- [[#1002](https://github.com/mabel-dev/opteryx/issues/1002)] Limit function ignored [@joocer](https://github.com/joocer) 

## [0.9.3] - 2023-03-04

### Fixed

- [[#916](https://github.com/mabel-dev/opteryx/issues/916)] Profile error on morsel with all nulls in column [@joocer](https://github.com/joocer) 
- Correctness of LRU-K algorithm [@joocer](https://github.com/joocer) 
- [[#917](https://github.com/mabel-dev/opteryx/issues/917)] Comparisons failed on very long and skinny tables [@joocer](https://github.com/joocer) 

## [0.9.2] - 2023-02-28

### Fixed

- [[#909](https://github.com/mabel-dev/opteryx/issues/909)] Divide by Zero error handling empty pages [@joocer](https://github.com/joocer) 
- [[#912](https://github.com/mabel-dev/opteryx/issues/912)] Literal expressioned which evaluate to a boolean were ignored [@joocer](https://github.com/joocer) 

### Changed

- :octicons-alert-24: [[#901](https://github.com/mabel-dev/opteryx/issues/901)] Generate Series no longer accepts single numbers or IP ranges, provide explicit start or use `|` to test IP address containment [@joocer](https://github.com/joocer) 
- [[#848](https://github.com/mabel-dev/opteryx/issues/848)] Collection and SQL Connectors dynamically size reads to fill target morsel size [@joocer](https://github.com/joocer) 

## [0.9.1] - 2023-02-23

### Fixed

- [[#888](https://github.com/mabel-dev/opteryx/issues/888)] YAML parser errors. [@joocer](https://github.com/joocer) 


## [0.9.0] - 2023-02-19

### Fixed

- [[#797](https://github.com/mabel-dev/opteryx/issues/797)] Name collisons with aliases cause issues in `ORDER BY`. [@joocer](https://github.com/joocer) 
- [[#833](https://github.com/mabel-dev/opteryx/issues/833)] Unhelpful error when no statement is provided [@joocer](https://github.com/joocer) 
- [[#870](https://github.com/mabel-dev/opteryx/issues/870)] Repeated columns in `GROUP BY` not processed [@joocer](https://github.com/joocer) 
- [[#873](https://github.com/mabel-dev/opteryx/issues/873)] 2 x CodeQL security issues [@joocer](https://github.com/joocer) 

### Changed

- [[#799](https://github.com/mabel-dev/opteryx/issues/799)] Chunk large blob reads. [@joocer](https://github.com/joocer) 
- [[#812](https://github.com/mabel-dev/opteryx/issues/812)] Abstract the tree structure that plans are built from. [@joocer](https://github.com/joocer) 
- [[#808](https://github.com/mabel-dev/opteryx/issues/808)] Split Logical and Physical planning (partial). [@joocer](https://github.com/joocer) 
- [[#825](https://github.com/mabel-dev/opteryx/issues/825)] Remove HyperLogLog from profiling. [@joocer](https://github.com/joocer) 
- [[#750](https://github.com/mabel-dev/opteryx/issues/750)] More CLI improvements. [@joocer](https://github.com/joocer)   
- [[#589](https://github.com/mabel-dev/opteryx/issues/589)] Moved conditional imports out of program initialization [@joocer](https://github.com/joocer) 
- [[#836](https://github.com/mabel-dev/opteryx/issues/836)] Use PyArrow 11s exposure of underlying date values in profiler [@joocer](https://github.com/joocer) 
- [[#853](https://github.com/mabel-dev/opteryx/issues/853)] CaskDB replaces RocksDB as default KV store [@joocer](https://github.com/joocer) 
- :octicons-alert-24: [[#855](https://github.com/mabel-dev/opteryx/issues/853)] Caches have been renamed and separated from KV Stores to disencourage incorrect use; The Memcache Cache is now imported using `from opteryx.managers.cache import MemcachedCache` [@joocer](https://github.com/joocer) 
- [[#857](https://github.com/mabel-dev/opteryx/issues/857)] Removed PyYAML install [@joocer](https://github.com/joocer) 
- [[#865](https://github.com/mabel-dev/opteryx/issues/865)] Replaced third-party `DATE_TRUNC` implementation with a first-party implementation [@joocer](https://github.com/joocer) 
- [[#861](https://github.com/mabel-dev/opteryx/issues/861)] Replaced third-party `bitarray` library with a first-party implementation [@joocer](https://github.com/joocer) 
- :octicons-alert-24: [[#871](https://github.com/mabel-dev/opteryx/issues/871)] Consistently name internal variables relating to chunks of data to 'morsel' (technically breaking, but no user impact expected) [@joocer](https://github.com/joocer) 
- [[#880](https://github.com/mabel-dev/opteryx/issues/880)] Minor performance improvements [@joocer](https://github.com/joocer) 

### Added

- [[#801](https://github.com/mabel-dev/opteryx/issues/801)] New helper function `opteryx.query()`. [@joocer](https://github.com/joocer) 
- [[#818](https://github.com/mabel-dev/opteryx/issues/818)] Save query plans to disk (partial). [@joocer](https://github.com/joocer) 
- [[#163](https://github.com/mabel-dev/opteryx/issues/163)] Initial support for SQL databases as a data source. [@joocer](https://github.com/joocer) 
- [[#844](https://github.com/mabel-dev/opteryx/issues/844)] Materialize results as a [Polars](https://www.pola.rs/) dataframe. [@joocer](https://github.com/joocer) 
- [[#869](https://github.com/mabel-dev/opteryx/issues/869)] Introduce a SQL Fuzzer. [@joocer](https://github.com/joocer) 
- [[#877](https://github.com/mabel-dev/opteryx/issues/877)] Initial experimental implementation of internal KV database, HadroDB [@joocer](https://github.com/joocer) 

## [0.8.3] - 2023-01-10 

### Fixed

- [[#782](https://github.com/mabel-dev/opteryx/issues/782)] Support literal predicates in `JOIN` conditions. [@joocer](https://github.com/joocer) 

### Changed

- [[#789](https://github.com/mabel-dev/opteryx/pull/789)] Updated [sqlparser-rs](https://github.com/sqlparser-rs/sqlparser-rs) to version 0.30.0 [dependabot](https://github.com/apps/dependabot)  

### Added

- [[#521](https://github.com/mabel-dev/opteryx/issues/521)] Query files directly. [@joocer](https://github.com/joocer)  
- [[#786](https://github.com/mabel-dev/opteryx/issues/786)] Save dataset as pandas DataFrame. [@joocer](https://github.com/joocer) 
- [[#787](https://github.com/mabel-dev/opteryx/issues/787)] Run queries against pandas DataFrames. [@joocer](https://github.com/joocer) 

## [0.8.2] - 2023-01-06

### Fixed

- [[#757](https://github.com/mabel-dev/opteryx/issues/757)] Multiple bugs in config manager. [@joocer](https://github.com/joocer) 
- [[#769](https://github.com/mabel-dev/opteryx/issues/769)] `ARRAY_AGG` couldn't be nested. [@joocer](https://github.com/joocer) 
- [[#775](https://github.com/mabel-dev/opteryx/issues/775)] Connection function `.arrow()` materializes before applying limit. [@joocer](https://github.com/joocer) 

### Changed

- Internal refactoring relating to creation of metadata service. [@joocer](https://github.com/joocer)  
- [[#761](https://github.com/mabel-dev/opteryx/pull/761)] Updated [sqlparser-rs](https://github.com/sqlparser-rs/sqlparser-rs) to version 0.29.0 [dependabot](https://github.com/apps/dependabot) 

### Added

- [[#750](https://github.com/mabel-dev/opteryx/issues/750)] CLI improvements. [@joocer](https://github.com/joocer)   
- [[#758](https://github.com/mabel-dev/opteryx/issues/758)] Support AVRO and TSV formatted files. [@joocer](https://github.com/joocer) 

## [0.8.1] - 2022-12-30

### Fixed

- [[#754](https://github.com/mabel-dev/opteryx/issues/754)] Occassional segfaults on Aggregates. [@joocer](https://github.com/joocer) 

## [0.8.0] - 2022-12-27

### Fixed

- [[#703](https://github.com/mabel-dev/opteryx/issues/703)] `ORDER BY` columns not in `SELECT` clause. [@joocer](https://github.com/joocer) 
- [[#712](https://github.com/mabel-dev/opteryx/issues/712)] Aggregates on literals when combined with a `GROUP BY` clause. [@joocer](https://github.com/joocer) 
- [[#710](https://github.com/mabel-dev/opteryx/issues/710)] `SEARCH` mishandles pages with empty values in first row. [@joocer](https://github.com/joocer) 
- [[#711](https://github.com/mabel-dev/opteryx/issues/711)] `DATE_TRUNC` is case sensitive. [@joocer](https://github.com/joocer) 

### Changed

- [[#707](https://github.com/mabel-dev/opteryx/issues/707)] First try to estimate unique values using the Distogram for `SHOW EXTENDED COLUMNS`. [@joocer](https://github.com/joocer) 
- [[#707](https://github.com/mabel-dev/opteryx/issues/707)] `SHOW EXTENDED COLUMNS` creates histograms of 20 bins. [@joocer](https://github.com/joocer) 
- [[#707](https://github.com/mabel-dev/opteryx/issues/707)] Distogram (data profiler) significant performance improvements. [@joocer](https://github.com/joocer) 
- [[#722](https://github.com/mabel-dev/opteryx/issues/722)] Allow temporal `FOR` after alias `AS` clauses. [@joocer](https://github.com/joocer) 
- [[#743](https://github.com/mabel-dev/opteryx/issues/743)] 'Did you mean' prompt for columns better suggestions when casing is different. [@joocer](https://github.com/joocer) 

### Added

- [[#515](https://github.com/mabel-dev/opteryx/issues/515)] Implement various new functions. [@joocer](https://github.com/joocer)  
- [[#19](https://github.com/mabel-dev/opteryx/issues/19)] Initial support for CTE expressions. [@joocer](https://github.com/joocer)  
- [[#204](https://github.com/mabel-dev/opteryx/issues/204)] Initial support predicate pushdowns. [@joocer](https://github.com/joocer)  
- [[#721](https://github.com/mabel-dev/opteryx/issues/721)] Improved temporal range error messages. [@joocer](https://github.com/joocer)  

## [0.7.0] - 2022-12-02

### Fixed

- [[#653](https://github.com/mabel-dev/opteryx/issues/653)] `LIKE` and `FOR` clauses cannot coexist in `SHOW` queries. [@joocer](https://github.com/joocer)  
- [[#669](https://github.com/mabel-dev/opteryx/issues/669)] `COUNT(*)` cannot be mixed with other aggregates. [@joocer](https://github.com/joocer)  
- [[#518](https://github.com/mabel-dev/opteryx/issues/518)] `SELECT *` and `GROUP BY` can't be used together. [@joocer](https://github.com/joocer)  
- [[#689](https://github.com/mabel-dev/opteryx/issues/689)] `IS` comparisons cannot be combined with other comparisons when optimization is off. [@joocer](https://github.com/joocer)  

### Changed

- [[#662](https://github.com/mabel-dev/opteryx/pull/662)] Updated [sqlparser-rs](https://github.com/sqlparser-rs/sqlparser-rs) to version 0.27.0 [dependabot](https://github.com/apps/dependabot) 

### Added

- [[#629](https://github.com/mabel-dev/opteryx/issues/629)] Optimizer pre-evaluates constant expressions. [@joocer](https://github.com/joocer)   
- [[#439](https://github.com/mabel-dev/opteryx/issues/439)] Support `SHOW STORES`. [@joocer](https://github.com/joocer)   
- [[#542](https://github.com/mabel-dev/opteryx/issues/542)] Support `POSITION`. [@joocer](https://github.com/joocer)   
- [[#22](https://github.com/mabel-dev/opteryx/issues/22)] Support `CASE` statements. [@joocer](https://github.com/joocer)   
- [[#665](https://github.com/mabel-dev/opteryx/issues/665)] Partial support of `ARRAY_AGG` function. [@joocer](https://github.com/joocer)   
- [[#668](https://github.com/mabel-dev/opteryx/issues/668)] Optimizer exchanges functions with constant results. [@joocer](https://github.com/joocer)   
- [[#300](https://github.com/mabel-dev/opteryx/issues/300)] Support advanced `TRIM` syntax. [@joocer](https://github.com/joocer)   
- [[#570](https://github.com/mabel-dev/opteryx/issues/570)] Optimizer implements De Morgan's Law. [@joocer](https://github.com/joocer)   

## [0.6.0] - 2022-11-08

### Fixed

- [[#568](https://github.com/mabel-dev/opteryx/issues/568)] Unable to perform aggregates on literals. [@joocer](https://github.com/joocer)   
- [[#592](https://github.com/mabel-dev/opteryx/issues/592)] Dates not always handled correctly. [@joocer](https://github.com/joocer)   
- [[#600](https://github.com/mabel-dev/opteryx/issues/600)] Parameterization when used on query batches fails. [@joocer](https://github.com/joocer)   
- [[#580](https://github.com/mabel-dev/opteryx/issues/580)] Empty result sets have no column information. [@joocer](https://github.com/joocer)   
- [[#548](https://github.com/mabel-dev/opteryx/issues/548)] 'did you mean' message restored for dataset `WITH` hints. [@joocer](https://github.com/joocer) 
- [[#640](https://github.com/mabel-dev/opteryx/issues/640)] `COUNT(*)` shortcut only used when in uppercase. [@joocer](https://github.com/joocer) 
- :octicons-alert-24: [[#645](https://github.com/mabel-dev/opteryx/issues/645)] (correction) `null` values not handled correctly in comparisions. [@joocer](https://github.com/joocer) 
- Problem installing on M1 Mac. [@joocer](https://github.com/joocer) 
- Support `AND`, `OR`, and `XOR` in `SELECT` statement. [@joocer](https://github.com/joocer) 
- [[#646](https://github.com/mabel-dev/opteryx/issues/646)] Temporal clauses in incorrect place were ignored [@joocer](https://github.com/joocer) 

### Changed

- [[#566](https://github.com/mabel-dev/opteryx/issues/566)] Change from using SQLite3 to [DuckDB](https://duckdb.org/) for SQL comparision tests in [Wrenchy-Bench](https://github.com/mabel-dev/wrenchy-bench). [@joocer](https://github.com/joocer)   
- :octicons-alert-24: [[#584](https://github.com/mabel-dev/opteryx/issues/584)] (clarity) `enable_page_management` configuration and parameter renamed `enable_page_defragmentation` with some minor refactoring of approach to defragmentation. [@joocer](https://github.com/joocer)   
- :octicons-alert-24: (alignment) `TIMESTAMP` casting no longer supports casting from a number. [@joocer](https://github.com/joocer)   
- [[#588](https://github.com/mabel-dev/opteryx/issues/588)] Integrate [sqloxide](https://github.com/wseaton/sqloxide) into Opteryx to reduce lag with [sqlparser-rs](https://github.com/sqlparser-rs/sqlparser-rs) updates. [@joocer](https://github.com/joocer)   
- [[#619](https://github.com/mabel-dev/opteryx/issues/619)] Page defragmentation moved to an Operator and positioned by the Optimizer. [@joocer](https://github.com/joocer)   
- :octicons-alert-24: (correction) cursor 'fetch*' methods return Python tuple, rather than Python lists. [@joocer](https://github.com/joocer)   

### Added

- [[#533](https://github.com/mabel-dev/opteryx/issues/533)] Support `LIKE` on `SHOW FUNCTIONS`, see [sqlparser-rs/#620](https://github.com/sqlparser-rs/sqlparser-rs/pull/620). [@joocer](https://github.com/joocer)   
- [[#570](https://github.com/mabel-dev/opteryx/issues/570)] Query Optimizer rule to reduce steps in expression evaluation by partial elimination of negatives. [@joocer](https://github.com/joocer)   
- [[#129](https://github.com/mabel-dev/opteryx/issues/129)] Support `FOR` clauses for all datasets. [@joocer](https://github.com/joocer)   
- [[#543](https://github.com/mabel-dev/opteryx/issues/543)] Support 'type string' notation for casting values. [@joocer](https://github.com/joocer)   
- [[#596](https://github.com/mabel-dev/opteryx/issues/596)] Optimizer replaces `ORDER BY` and `LIMIT` plan steps with a single 'HeapSort' plan step. [@joocer](https://github.com/joocer)   
- [[#515](https://github.com/mabel-dev/opteryx/issues/515)] `NULLIF` function. [@joocer](https://github.com/joocer)   
- [[#581](https://github.com/mabel-dev/opteryx/issues/581)] New SQL Battery test that tests results, and initial set of tests. [@joocer](https://github.com/joocer)  
- [[#577](https://github.com/mabel-dev/opteryx/issues/577)] Hierarchical buffer pool and configuration. [@joocer](https://github.com/joocer)    

## [0.5.0] - 2022-10-02

### Fixed

- [[#528](https://github.com/mabel-dev/opteryx/issues/528)] `.shape()` and `.count()` not working as expected. [@joocer](https://github.com/joocer)   
- Numbers expressed in the form `+n` not parsed correctly. [@joocer](https://github.com/joocer)   

### Changed

- :octicons-alert-24: (alignment) `.as_arrow()` renamed to `.arrow()` to align to [DuckDB](https://duckdb.org/docs/api/python/overview#apache-arrow) naming. [@joocer](https://github.com/joocer)   
- :octicons-alert-24: (consistency) `SHOW COLUMNS` returns the column name in the `name` column, previously `column_name` [@joocer](https://github.com/joocer)   
- :octicons-alert-24: (correction) cursor 'fetch*' methods returns tuples rather than dictionaries as defaults, this is correcting a bug in [PEP249](https://peps.python.org/pep-0249/) compatibility. [@joocer](https://github.com/joocer)   
- :octicons-alert-24: [[#517](https://github.com/mabel-dev/opteryx/issues/517)] (security) Placeholder changed from '%s' to '?'. [@joocer](https://github.com/joocer)   
- [[#522](https://github.com/mabel-dev/opteryx/issues/522)] Implementation of LRU-K(2) for cache evictions. [@joocer](https://github.com/joocer)   
- [[#537](https://github.com/mabel-dev/opteryx/issues/537)] Significant refactor of Query Planner. [@joocer](https://github.com/joocer)   

### Added

- [[#397](https://github.com/mabel-dev/opteryx/issues/397)] Time Travel with '$planets' dataset. [@joocer](https://github.com/joocer)   
- [[#519](https://github.com/mabel-dev/opteryx/issues/519)] Introduce a size limit on `.as_arrow()`. [@joocer](https://github.com/joocer)   
- [[#324](https://github.com/mabel-dev/opteryx/issues/324)] Support `IN UNNEST()`. [@joocer](https://github.com/joocer)   
- [[#386](https://github.com/mabel-dev/opteryx/issues/386)] Support `SET` statements. [@joocer](https://github.com/joocer)   
- [[#531](https://github.com/mabel-dev/opteryx/issues/531)] Support `SHOW VARIABLES` and `SHOW PARAMETERS`. [@joocer](https://github.com/joocer)   
- [[#464](https://github.com/mabel-dev/opteryx/issues/464)] Support `LEFT JOIN <relation> USING` [@joocer](https://github.com/joocer)   
- [[#402](https://github.com/mabel-dev/opteryx/issues/402)] `INNER JOIN ON` supports multiple conditions [@joocer](https://github.com/joocer)   
- [[#551](https://github.com/mabel-dev/opteryx/issues/551)] Document stores (MongoDb + FireStore) return '_id' column holding string version of document ID. [@joocer](https://github.com/joocer)   
- [[#532](https://github.com/mabel-dev/opteryx/issues/532)] Runtime parameters are able to be altered using the `SET` statement. [@joocer](https://github.com/joocer)  
- [[#524](https://github.com/mabel-dev/opteryx/issues/524)] Query Optimizer - conjunctive predicate splitter. [@joocer](https://github.com/joocer)  


## [0.4.1] - 2022-09-12

### Fixed

- Fixed missing `__init__` file. [@joocer](https://github.com/joocer)  

## [0.4.0] - 2022-09-12

### Added

- [[#366](https://github.com/mabel-dev/opteryx/issues/336)] Implement 'function not found' suggestions. [@joocer](https://github.com/joocer)    
- [[#443](https://github.com/mabel-dev/opteryx/issues/443)] Introduce a CLI. [@joocer](https://github.com/joocer)   
- [[#351](https://github.com/mabel-dev/opteryx/issues/351)] Support `SHOW FUNCTIONS`. [@joocer](https://github.com/joocer)   
- [[#442](https://github.com/mabel-dev/opteryx/issues/442)] Various functions. [@joocer](https://github.com/joocer)   
- [[#483](https://github.com/mabel-dev/opteryx/issues/483)] Support `SHOW CREATE TABLE`. [@joocer](https://github.com/joocer)   
- [[#375](https://github.com/mabel-dev/opteryx/issues/375)] Results to an Arrow Table. [@joocer](https://github.com/joocer)   
- [[#486](https://github.com/mabel-dev/opteryx/issues/486)] Support functions on aggregates and aggregates on functions. [@joocer](https://github.com/joocer)   
- Initial support for `INTERVAL`s. [@joocer](https://github.com/joocer)   
- [[#395](https://github.com/mabel-dev/opteryx/issues/395)] Support reading CSV files. [@joocer](https://github.com/joocer)   
- [[#498](https://github.com/mabel-dev/opteryx/issues/498)] CLI support writing CSV/JSONL/Parquet. [@joocer](https://github.com/joocer)   

### Changed

- :octicons-alert-24: [[#457](https://github.com/mabel-dev/opteryx/issues/457)] (correction) `null` values are removed before performing `INNER JOIN USING`. [@joocer](https://github.com/joocer)  

### Fixed

- [[#448](https://github.com/mabel-dev/opteryx/issues/448)] `VERSION()` failed and missing from regression suite. [@joocer](https://github.com/joocer)  
- [[#404](https://github.com/mabel-dev/opteryx/issues/404)] `COALESCE` fails for NaN values. [@joocer](https://github.com/joocer)    
- [[#453](https://github.com/mabel-dev/opteryx/issues/453)] PyArrow bug with long lists creating new columns. [@joocer](https://github.com/joocer)    
- [[#444](https://github.com/mabel-dev/opteryx/issues/444)] Very low cardinality `INNER JOINS` exceed memory allocation. [@joocer](https://github.com/joocer)    
- [[#459](https://github.com/mabel-dev/opteryx/issues/459)] Functions lose some detail on non-first page. [@joocer](https://github.com/joocer)   
- [[#465](https://github.com/mabel-dev/opteryx/issues/465)] Pages aren't matched to schema for simple queries. [@joocer](https://github.com/joocer)  
- [[#468](https://github.com/mabel-dev/opteryx/issues/468)] Parquet reader shows some fields as "item". [@joocer](https://github.com/joocer)  
- [[#471](https://github.com/mabel-dev/opteryx/issues/471)] Column aliases not correctly applied when the relation has an alias. [@joocer](https://github.com/joocer)  
- [[#489](https://github.com/mabel-dev/opteryx/issues/489)] Intermittent behaviour on hash `JOIN` algorithm. [@joocer](https://github.com/joocer)  

## [0.3.0] - 2022-08-28

### Added

- [[#196](https://github.com/mabel-dev/opteryx/issues/196)] Partial implementation of projection pushdown (Parquet Only). [@joocer](https://github.com/joocer)    
- [[#41](https://github.com/mabel-dev/opteryx/issues/41)] Enable the results of functions to be used as parameters for other functions. [@joocer](https://github.com/joocer)   
- [[#42](https://github.com/mabel-dev/opteryx/issues/42)] Enable inline operations. [@joocer](https://github.com/joocer)  
- [[#330](https://github.com/mabel-dev/opteryx/issues/330)] Support `SIMILAR TO` alias for RegEx match. [@joocer](https://github.com/joocer)  
- [[#331](https://github.com/mabel-dev/opteryx/issues/331)] Support `SAFE_CAST` alias for `TRY_CAST`. [@joocer](https://github.com/joocer)  
- [[#419](https://github.com/mabel-dev/opteryx/issues/419)] Various simple functions (`SIGN`, `SQRT`, `TITLE`, `REVERSE`). [@joocer](https://github.com/joocer)  
- [[#364](https://github.com/mabel-dev/opteryx/issues/364)] Support `SOUNDEX` function. [@joocer](https://github.com/joocer)  
- [[#401](https://github.com/mabel-dev/opteryx/issues/401)] Support SHA-based hash algorithm functions. [@joocer](https://github.com/joocer)  

### Changed

- :octicons-alert-24: (alignment) Paths to storage adapters has been updated to reflect 'connector' terminology.
- :octicons-alert-24: (sensible defaults) Default behaviour changed from Mabel partitioning to no partitioning.
- :octicons-alert-24: (correction) - Use of aliases defined in the `SELECT` clause can no longer be used in `WHERE` and `GROUP BY` clauses - this is a correction to align to standard SQL behaviour.
- :octicons-alert-24: (correction) - Use of 'None' as an alias for `null` is no longer supported - this is a correction to align to standard SQL behaviour.
- [[#326](https://github.com/mabel-dev/opteryx/issues/326)] Prefer pyarrow's 'promote' over manually handling missing fields. [@joocer](https://github.com/joocer)    
- [[#39](https://github.com/mabel-dev/opteryx/issues/39)] Rewrite Aggregation Node to use Pyarrow `group_by()`. [@joocer](https://github.com/joocer)   
- [[#338](https://github.com/mabel-dev/opteryx/issues/338)] Remove Evaluation Node. [@joocer](https://github.com/joocer)  
- [[#58](https://github.com/mabel-dev/opteryx/issues/58)] Performance of `ORDER BY RAND()` improved. [@joocer](https://github.com/joocer)  

### Fixed

- [[#334](https://github.com/mabel-dev/opteryx/issues/334)] All lists should be cast to lists of strings. ([@joocer](https://github.com/joocer))
- [[#382](https://github.com/mabel-dev/opteryx/issues/382)] `INNER JOIN` on `UNNEST` relation. ([@joocer](https://github.com/joocer))
- [[#320](https://github.com/mabel-dev/opteryx/issues/320)] Can't execute functions on results of `GROUP BY`. ([@joocer](https://github.com/joocer))
- [[#399](https://github.com/mabel-dev/opteryx/issues/399)] Strings in double quotes aren't parsed. ([@joocer](https://github.com/joocer))

## [0.2.0] - 2022-07-31

### Added

- [[#232](https://github.com/mabel-dev/opteryx/issues/232)] Support `DATEPART` and `EXTRACT` date functions. [@joocer](https://github.com/joocer)    
- [[#63](https://github.com/mabel-dev/opteryx/issues/63)] Estimate row counts when reading blobs. ([@joocer](https://github.com/joocer))
- [[#231](https://github.com/mabel-dev/opteryx/issues/231)] Implement `DATEDIFF` function. ([@joocer](https://github.com/joocer))
- [[#301](https://github.com/mabel-dev/opteryx/issues/301)] Optimizations for `IS` conditions. ([@joocer](https://github.com/joocer))
- [[#229](https://github.com/mabel-dev/opteryx/issues/229)] Support `TIME_BUCKET` function. ([@joocer](https://github.com/joocer))

### Changed

- [[#35](https://github.com/mabel-dev/opteryx/issues/35)] Table scan planning done during query planning. [@joocer](https://github.com/joocer)    
- [[#173](https://github.com/mabel-dev/opteryx/issues/173)] Data not found raises different errors under different scenarios. ([@joocer](https://github.com/joocer))
- Implementation of `LEFT` and `RIGHT` functions to reduce execution time. ([@joocer](https://github.com/joocer))
- [[#258](https://github.com/mabel-dev/opteryx/issues/258)] Code release approach. ([@joocer](https://github.com/joocer))
- [[#295](https://github.com/mabel-dev/opteryx/issues/295)] Removed redundant projection when `SELECT *`. ([@joocer](https://github.com/joocer))
- [[#297](https://github.com/mabel-dev/opteryx/issues/297)] Filters on `SHOW COLUMNS` execute before profiling. ([@joocer](https://github.com/joocer))

### Fixed

- [[#252](https://github.com/mabel-dev/opteryx/issues/252)] Planner should gracefully convert byte strings to ascii strings. ([@joocer](https://github.com/joocer))
- [[#184](https://github.com/mabel-dev/opteryx/issues/184)] Schema changes cause unexpected and unhelpful failures. ([@joocer](https://github.com/joocer))
- [[#261](https://github.com/mabel-dev/opteryx/issues/216)] Read fails if buffer cache is unavailable. ([@joocer](https://github.com/joocer))
- [[#277](https://github.com/mabel-dev/opteryx/issues/277)] Cache errors should be transparent. ([@joocer](https://github.com/joocer))
- [[#285](https://github.com/mabel-dev/opteryx/issues/285)] `DISTINCT` on nulls throws error. ([@joocer](https://github.com/joocer))
- [[#281](https://github.com/mabel-dev/opteryx/issues/281)] `SELECT` on empty aggregates reports missing columns. ([@joocer](https://github.com/joocer))
- [[#312](https://github.com/mabel-dev/opteryx/issues/312)] Invalid dates in `FOR` clauses treated as `TODAY`. ([@joocer](https://github.com/joocer))

## [0.1.0] - 2022-07-02

### Added

- [[#165](https://github.com/mabel-dev/opteryx/issues/165)] Support S3/MinIO data stores for blobs. ([@joocer](https://github.com/joocer))
- `FAKE` dataset constructor (part of [#179](https://github.com/mabel-dev/opteryx/issues/179)). ([@joocer](https://github.com/joocer))
- [[#177](https://github.com/mabel-dev/opteryx/issues/177)] Support `SHOW FULL COLUMNS` to read entire datasets rather than just the first blob. ([@joocer](https://github.com/joocer))
- [[#194](https://github.com/mabel-dev/opteryx/issues/194)] Functions that are abbreviations, should have the full name as an alias. ([@joocer](https://github.com/joocer))
- [[#201](https://github.com/mabel-dev/opteryx/issues/201)] `generate_series()` supports CIDR expansion. ([@joocer](https://github.com/joocer))
- [[#175](https://github.com/mabel-dev/opteryx/issues/175)] Support `WITH (NO_CACHE)` hint to disable using cache. ([@joocer](https://github.com/joocer))
- [[#203](https://github.com/mabel-dev/opteryx/issues/203)] When reporting that a column doesn't exist, it should suggest likely correct columns. ([@joocer](https://github.com/joocer))
- 'Not' Regular Expression match operator, `!~` added to supported set of operators. ([@joocer](https://github.com/joocer))
- [[#226](https://github.com/mabel-dev/opteryx/issues/226)] Implement `DATE_TRUNC` function. ([@joocer](https://github.com/joocer))
- [[#230](https://github.com/mabel-dev/opteryx/issues/230)] Allow addressing fields as numbers. ([@joocer](https://github.com/joocer))
- [[#234](https://github.com/mabel-dev/opteryx/issues/234)] Implement `SEARCH` function. ([@joocer](https://github.com/joocer))
- [[#237](https://github.com/mabel-dev/opteryx/issues/237)] Implement `COALESCE` function. ([@joocer](https://github.com/joocer))

### Changed

- Blob-based readers (disk & GCS) moved from 'local' and 'network' paths to a new 'blob' path. ([@joocer](https://github.com/joocer))
- Query Execution rewritten. ([@joocer](https://github.com/joocer))
- [[#20](https://github.com/mabel-dev/opteryx/issues/20)] Split query planner and query plan into different modules. ([@joocer](https://github.com/joocer))
- [[#164](https://github.com/mabel-dev/opteryx/issues/164)] Split dataset reader into specific types. ([@joocer](https://github.com/joocer))
- Expression evaluation short-cuts execution when executing evaluations against an array of `null`. ([@joocer](https://github.com/joocer))
- [[#244](https://github.com/mabel-dev/opteryx/issues/244)] Improve performance of `IN` test against literal lists. ([@joocer](https://github.com/joocer))

### Fixed

- [[#172](https://github.com/mabel-dev/opteryx/issues/172)] `LIKE` on non string column gives confusing error ([@joocer](https://github.com/joocer))
- [[#179](https://github.com/mabel-dev/opteryx/issues/179)] Aggregate Node creates new metadata for each chunk ([@joocer](https://github.com/joocer))
- [[#183](https://github.com/mabel-dev/opteryx/issues/183)] `NOT` doesn't display in plan correctly ([@joocer](https://github.com/joocer))
- [[#182](https://github.com/mabel-dev/opteryx/issues/182)] Unable to evaluate valid filters ([@joocer](https://github.com/joocer))
- [[#178](https://github.com/mabel-dev/opteryx/issues/178)] `SHOW COLUMNS` returns type OTHER when it can probably work out the type ([@joocer](https://github.com/joocer))
- [[#128](https://github.com/mabel-dev/opteryx/issues/128)] `JOIN` fails, using PyArrow .join() ([@joocer](https://github.com/joocer))
- [[#189](https://github.com/mabel-dev/opteryx/issues/189)] Explicit `JOIN` algorithm exceeds memory ([@joocer](https://github.com/joocer))
- [[#199](https://github.com/mabel-dev/opteryx/issues/199)] `SHOW EXTENDED COLUMNS` blows memory allocations on large tables ([@joocer](https://github.com/joocer))
- [[#169](https://github.com/mabel-dev/opteryx/issues/169)] Selection nodes in `EXPLAIN` have nested parentheses. ([@joocer](https://github.com/joocer))
- [[#220](https://github.com/mabel-dev/opteryx/issues/220)] `LIKE` clause fails for columns that contain nulls. ([@joocer](https://github.com/joocer))
- [[#222](https://github.com/mabel-dev/opteryx/issues/222)] Column of `NULL` detects as `VARCHAR`. ([@joocer](https://github.com/joocer))
- [[#225](https://github.com/mabel-dev/opteryx/issues/225)] `UNNEST` does not assign a type to the column when all of the values are `NULL`. ([@joocer](https://github.com/joocer))

## [0.0.2] - 2022-06-03

### Added

- [[#72](https://github.com/mabel-dev/opteryx/issues/72)] Configuration is now read from `opteryx.yaml` rather than the environment. ([@joocer](https://github.com/joocer))
- [[#139](https://github.com/mabel-dev/opteryx/issues/139)] Gather statistics on planning reading of segements. ([@joocer](https://github.com/joocer))
- [[#151](https://github.com/mabel-dev/opteryx/issues/151)] Implement `SELECT table.*`. ([@joocer](https://github.com/joocer))
- [[#137](https://github.com/mabel-dev/opteryx/issues/137)] `GENERATE_SERIES` function. ([@joocer](https://github.com/joocer))

### Fixed

- [[#106](https://github.com/mabel-dev/opteryx/issues/106)] `ORDER BY` on qualified fields fails ([@joocer](https://github.com/joocer))
- [[#103](https://github.com/mabel-dev/opteryx/issues/103)] `ORDER BY` after `JOIN` errors ([@joocer](https://github.com/joocer))
- [[#110](https://github.com/mabel-dev/opteryx/issues/110)] SubQueries `AS` statement ignored ([@joocer](https://github.com/joocer))
- [[#112](https://github.com/mabel-dev/opteryx/issues/112)] `SHOW COLUMNS` doesn't work for non sample datasets ([@joocer](https://github.com/joocer))
- [[#113](https://github.com/mabel-dev/opteryx/issues/113)] Sample data has "NaN" as a string, rather than the value `NaN` ([@joocer](https://github.com/joocer))
- [[#111](https://github.com/mabel-dev/opteryx/issues/111)] `CROSS JOIN UNNEST` should return a `NONE` when the list is empty (or `NONE`) ([@joocer](https://github.com/joocer))
- [[#119](https://github.com/mabel-dev/opteryx/issues/119)] 'NoneType' object is not iterable error on `UNNEST` ([@joocer](https://github.com/joocer))
- [[#127](https://github.com/mabel-dev/opteryx/issues/127)] Reading from segments appears to only read the first segment ([@joocer](https://github.com/joocer))
- [[#132](https://github.com/mabel-dev/opteryx/issues/132)] Multiprocessing regressed Caching functionality ([@joocer](https://github.com/joocer))
- [[#140](https://github.com/mabel-dev/opteryx/issues/140)] Appears to have read both frames rather than the latest frame ([@joocer](https://github.com/joocer))
- [[#144](https://github.com/mabel-dev/opteryx/issues/144)] Multiple `JOINS` in one query aren't recognized ([@joocer](https://github.com/joocer))

## [0.0.1] - 2022-05-09

### Added

- Additional statistics recording the time taken to scan partitions ([@joocer](https://github.com/joocer))
- Support for `FULL JOIN` and `RIGHT JOIN` ([@joocer](https://github.com/joocer))

### Changed

- Use PyArrow implementation for `INNER JOIN` and `LEFT JOIN` ([@joocer](https://github.com/joocer))

### Fixed

- [[#99](https://github.com/mabel-dev/opteryx/issues/99)] Grouping by a list gives an unhelpful error message  ([@joocer](https://github.com/joocer))
- [[#100](https://github.com/mabel-dev/opteryx/issues/100)] Projection ignores field qualifications ([@joocer](https://github.com/joocer))

## [0.0.0]

- Initial Version
