# Notices

## Incorporated Components

Opteryx, mesos, and orso are built on the shoulders of other great libraries and components:

Library           | Inclusion Type    | Copyright            | Licence   
:---------------- | :---------------- | :------------------- | :--------------- 
[abseil-cpp](https://github.com/abseil/abseil-cpp)         | Vendored   | 2017 [Abseil](https://abseil.io/#) | [Apache 2.0](https://github.com/abseil/abseil-cpp/blob/master/LICENSE)
[base64](https://github.com/alantsd/base64)                | Vendored   | 2018 [Rafa Garcia](https://github.com/rafagafe), 2020 [Alan Tong](https://github.com/alantsd) | [MIT](https://github.com/alantsd/base64/blob/master/LICENSE)
[cython](https://github.com/cython/cython)                 | Dependency |  | [Apache 2.0](https://github.com/cython/cython/blob/master/LICENSE.txt)
[datafusion-sqlparser-rs](https://github.com/apache/datafusion-sqlparser-rs) | Dependency |  | [Apache 2.0](https://github.com/apache/datafusion-sqlparser-rs/blob/main/LICENSE.TXT)
[fast_float](https://github.com/fastfloat/fast_float)      | Vendored   | 2021 fast_float authors | [Apache 2.0](https://github.com/fastfloat/fast_float/blob/main/LICENSE-APACHE)  
[fuzzy](https://github.com/yougov/fuzzy)                   | Vendored   | [Jason R. Coombs](https://github.com/jaraco) | [MIT](https://github.com/yougov/fuzzy/blob/master/LICENSE)
[mbleven](https://github.com/fujimotos/mbleven)            | Vendored   | 2018 [Fujimoto Seiji](https://github.com/fujimotos) | [Public Domain](https://github.com/fujimotos/mbleven/blob/master/LICENSE)
[mysql-mimic](https://github.com/kelsin/mysql-mimic)       | Derived    | 2022 [Christopher Giroir](https://github.com/kelsin) | [MIT](https://github.com/kelsin/mysql-mimic/blob/main/LICENSE)
[nanoarrow](https://github.com/apache/arrow-nanoarrow)     | Vendored   | 2023 [Apache Foundation](https://github.com/apache/arrow-nanoarrow/blob/main/NOTICE.txt) | [Apache 2.0](https://github.com/apache/arrow-nanoarrow/blob/main/LICENSE.txt)
[numpy](https://github.com/numpy/numpy)                    | Dependency |  | [BSD-3](https://github.com/numpy/numpy/blob/main/LICENSE.txt)
[orjson](https://github.com/ijl/orjson)                    | Dependency |  | [Apache 2.0](https://github.com/ijl/orjson/blob/master/LICENSE-APACHE)
[pyarrow](https://github.com/apache/arrow/)                | Dependency |  | [Apache 2.0](https://github.com/apache/arrow/blob/master/LICENSE.txt)
[pyarrow_ops](https://github.com/TomScheffers/pyarrow_ops) | Derived    | [TomScheffers](https://github.com/TomScheffers) (assumed) | [Apache 2.0](https://github.com/TomScheffers/pyarrow_ops/blob/main/LICENSE)
[pysimdjson](https://github.com/TkTech/pysimdjson)         | Vendored   | 2019 [Tyler Kennedy](https://github.com/TkTech) | [Apache 2.0](https://github.com/TkTech/pysimdjson/blob/master/LICENSE)
[query-builder](https://death.andgravity.com/query-builder-how) | Vendored | 2021 [lemon24](https://github.com/lemon24) (assumed) | [BSD-3](https://github.com/lemon24/reader/blob/15121f667a6f2e388f0072a3fcd715f533883899/LICENSE)
[ryu](https://github.com/ulfjack/ryu)                      | Vendored   | 2018 [Ulf Adams](https://github.com/ulfjack) (assumed) | [Apache 2.0](https://github.com/ulfjack/ryu/blob/master/LICENSE-Apache2)
[sqloxide](https://github.com/wseaton/sqloxide)            | Vendored   | 2020 [Will Eaton](https://github.com/wseaton) | [MIT](https://github.com/wseaton/sqloxide/blob/master/LICENSE)
[xxHash](https://github.com/Cyan4973/xxHash)               | Vendored   | 2023 [Yann Collet](https://github.com/Cyan4973) | [BSD-2](https://github.com/Cyan4973/xxHash/blob/dev/LICENSE)

Inclusion Types in this table:

- **Derived** components originated from this module but have undergone significant change.  
- **Dependency** components are installed from PyPI/Cargo.  
- **Vendored** components have their source code (or significant parts of) included in the Opteryx/Orso codebase.  

This list does not include transitive dependencies nor is guaranteed to be complete. See the [dependency graph on GitHub](https://github.com/mabel-dev/opteryx/network/dependencies) for a more complete view of components used.

Only integrated components have copyright information listed, and best efforts have been made to ensure this information is accurate. 

If the copyright or licence information is crucial for your use-case, we recommend verifying it independently. Should you find any inaccuracies, please [raise them as issues](https://github.com/mabel-dev/opteryx/issues/new?assignees=joocer&labels=Bug+%F0%9F%AA%B2&template=bug_report.md&title=%F0%9F%AA%B2) for correction. 

Integrated components may differ from their original versions. While we generally do not note cosmetic changes (e.g. PEP8 formatting), any alterations or additions to functionality are documented in the code comments. For derived components, we do not provide individual change notes, as these parts of the codebase have usually undergone substantial modifications, making such annotations less meaningful.

!!! Note   
    License information was last checked on 2022-06-03, or when specific entries were added to this document, if later.

## Other Assets

The [Icarus Opteryx](../../icarus-opteryx.png) image based on '[Evening: Fall of Day](https://collections.mfa.org/objects/30905)' by William Rimmer (Public Domain), more commonly associated with Led Zeppelin's [Swan Song](https://en.wikipedia.org/wiki/Swan_Song_Records). The Icarus Opteryx image is created using visual components from 'Archaeopteryx' fossil image by Caro Asercion ([CC BY 3.0](https://github.com/game-icons/icons/blob/master/license.txt)).

Satellite and Planet datasets acquired from [devstronomy](https://github.com/devstronomy/nasa-data-scraper/tree/f610e541a053f05e26573570604aed50b358cc43/data/json).

Astronaut dataset acquired from [Kaggle](https://www.kaggle.com/nasa/astronaut-yearbook).

Exoplanet dataset acquired from [Kaggle](https://www.kaggle.com/datasets/nasa/kepler-exoplanet-search-results).

English wordlist acquired from [wordlists](https://github.com/kkrypt0nn/wordlists).

Space Mission dataset acquired from [Kaggle](https://www.kaggle.com/datasets/agirlcoding/all-space-missions-from-1957).

Diagrams created using [ASCII Flow](https://asciiflow.com/) or [draw.io](https://github.com/jgraph/drawio).

Website built using [mkdocs-material](https://github.com/squidfunk/mkdocs-material).

SQL-92 conformity tests are based on [sqltest](https://github.com/elliotchance/sqltest).

Documentation code color scheme based on [Dracula](https://draculatheme.com/).

Opteryx creates charts and graphs compatible with [Mermaid](https://mermaid.js.org/).

## References and Guides

The following resources have been used as guides, references or patterns:

- [sqlglot](https://github.com/tobymao/sqlglot) Python Library
- [CMU DB Group](https://www.youtube.com/c/CMUDatabaseGroup) Lectures
- [DuckDB](https://duckdb.org/) embedded OLAP SQL Engine

## Uncredited Authors

ChatGPT has been used to assist in designing, refactoring, testing, debugging and documenting code.
