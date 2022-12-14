# Changelog

All notable changes to this project will be documented in this file, where appropriate the GitHub issue reference will be noted along with the change. Breaking changes will be clearly indicated with the :octicons-alert-24: icon.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Fixed

- [[#797](https://github.com/mabel-dev/opteryx/issues/797)] Name collisons with aliases and `ORDER BY`s. [@joocer](https://github.com/joocer) 

### Changed

- [[#799](https://github.com/mabel-dev/opteryx/issues/799)] Chunk large blob reads. [@joocer](https://github.com/joocer) 

### Added

- [[#801](https://github.com/mabel-dev/opteryx/issues/801)] Helper function `opteryx.query`. [@joocer](https://github.com/joocer) 

## [0.8.3] - 2023-01-10 

### Fixed

- [[#782](https://github.com/mabel-dev/opteryx/issues/782)] Support literal predicates in `JOIN` conditions. [@joocer](https://github.com/joocer) 

### Changed

- Updated [sqlparser-rs](https://github.com/sqlparser-rs/sqlparser-rs) to version 0.30.0 [@joocer](https://github.com/joocer)  

### Added

- [[#521](https://github.com/mabel-dev/opteryx/issues/521)] Query files directly. [@joocer](https://github.com/joocer)  
- [[#786](https://github.com/mabel-dev/opteryx/issues/786)] Save dataset as pandas DataFrame. [@joocer](https://github.com/joocer) 
- [[#787](https://github.com/mabel-dev/opteryx/issues/787)] Run queries against pandas DataFrames. [@joocer](https://github.com/joocer) 

## [0.8.2] - 2023-01-06

### Fixed

- [[#757](https://github.com/mabel-dev/opteryx/issues/757)] Multiple bugs in config manager. [@joocer](https://github.com/joocer) 
- [[#769](https://github.com/mabel-dev/opteryx/issues/769)] `ARRAY_AGG` couldn't be nested. [@joocer](https://github.com/joocer) 
- [[#775](https://github.com/mabel-dev/opteryx/issues/775)] Connection `arrow` materializes before applying limit. [@joocer](https://github.com/joocer) 

### Changed

- Internal refactoring relating to creation of metadata service. [@joocer](https://github.com/joocer)  
- Updated [sqlparser-rs](https://github.com/sqlparser-rs/sqlparser-rs) to version 0.29.0 [@joocer](https://github.com/joocer)  

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

- Updated [sqlparser-rs](https://github.com/sqlparser-rs/sqlparser-rs) to version 0.27.0 [@joocer](https://github.com/joocer)  

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

- [[#528](https://github.com/mabel-dev/opteryx/issues/528)] `.shape` and `.count` not working as expected. [@joocer](https://github.com/joocer)   
- Numbers expressed in the form `+n` not parsed correctly. [@joocer](https://github.com/joocer)   

### Changed

- :octicons-alert-24: (alignment) `as_arrow` renamed to `arrow` to align to [DuckDB](https://duckdb.org/docs/api/python/overview#apache-arrow) naming. [@joocer](https://github.com/joocer)   
- :octicons-alert-24: (consistency) `SHOW COLUMNS` returns the column name in the `name` column, previously `column_name` [@joocer](https://github.com/joocer)   
- :octicons-alert-24: (correction) cursor 'fetch*' methods returns tuples rather than dictionaries as defaults, this is correcting a bug in [PEP249](https://peps.python.org/pep-0249/) compatibility. [@joocer](https://github.com/joocer)   
- :octicons-alert-24: [[#517](https://github.com/mabel-dev/opteryx/issues/517)] (security) Placeholder changed from '%s' to '?'. [@joocer](https://github.com/joocer)   
- [[#522](https://github.com/mabel-dev/opteryx/issues/522)] Implementation of LRU-K(2) for cache evictions. [@joocer](https://github.com/joocer)   
- [[#537](https://github.com/mabel-dev/opteryx/issues/537)] Significant refactor of Query Planner. [@joocer](https://github.com/joocer)   

### Added

- [[#397](https://github.com/mabel-dev/opteryx/issues/397)] Time Travel with '$planets' dataset. [@joocer](https://github.com/joocer)   
- [[#519](https://github.com/mabel-dev/opteryx/issues/519)] Introduce a size limit on `as_arrow()`. [@joocer](https://github.com/joocer)   
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
- [[#39](https://github.com/mabel-dev/opteryx/issues/39)] Rewrite Aggregation Node to use Pyarrow `group_by`. [@joocer](https://github.com/joocer)   
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
- [[#201](https://github.com/mabel-dev/opteryx/issues/201)] `generate_series` supports CIDR expansion. ([@joocer](https://github.com/joocer))
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
