# Notices

## Incorporated Components

Opteryx, mesos, and orso are built on the shoulders of other great libraries and components:

Library           | Inclusion Type    | Copyright            | Licence   
:---------------- | :---------------- | :------------------- | :--------------- 
[cityhash](https://github.com/google/cityhash)             | Installed  | 2011 [Google](https://github.com/google) | [MIT](https://github.com/google/cityhash/blob/master/COPYING)  
[cython](https://github.com/cython/cython)                 | Installed   |  | [Apache 2.0](https://github.com/cython/cython/blob/master/LICENSE.txt)
[distogram](https://github.com/maki-nage/distogram)        | Integrated  | 2020 [Romain Picard](https://github.com/MainRo) | [MIT](https://github.com/maki-nage/distogram/blob/master/LICENSE.txt)
[fuzzy](https://github.com/yougov/fuzzy)                   | Integrated  | [Jason R. Coombs](https://github.com/jaraco) | [MIT](https://github.com/yougov/fuzzy/blob/master/LICENSE)
[mbleven](https://github.com/fujimotos/mbleven)            | Integrated  | 2018 [Fujimoto Seiji](https://github.com/fujimotos) | [Public Domain](https://github.com/fujimotos/mbleven/blob/master/LICENSE)
[mysql-mimic](https://github.com/kelsin/mysql-mimic)       | Derived     | 2022 [Christopher Giroir](https://github.com/kelsin) | [MIT](https://github.com/kelsin/mysql-mimic/blob/main/LICENSE)
[numpy](https://github.com/numpy/numpy)                    | Installed   |  | [BSD-3](https://github.com/numpy/numpy/blob/main/LICENSE.txt)
[orjson](https://github.com/ijl/orjson)                    | Installed   |  | [Apache 2.0](https://github.com/ijl/orjson/blob/master/LICENSE-APACHE)
[pyarrow](https://github.com/apache/arrow/)                | Installed   |  | [Apache 2.0](https://github.com/apache/arrow/blob/master/LICENSE.txt)
[pyarrow_ops](https://github.com/TomScheffers/pyarrow_ops) | Derived  | [TomScheffers](https://github.com/TomScheffers) (assumed) | [Apache 2.0](https://github.com/TomScheffers/pyarrow_ops/blob/main/LICENSE)
[query-builder](https://death.andgravity.com/query-builder-how) | Integrated | 2021 [lemon24](https://github.com/lemon24) (assumed) | [BSD-3](https://github.com/lemon24/reader/blob/15121f667a6f2e388f0072a3fcd715f533883899/LICENSE)
[sqloxide](https://github.com/wseaton/sqloxide)            | Integrated  | 2020 [Will Eaton](https://github.com/wseaton) | [MIT](https://github.com/wseaton/sqloxide/blob/master/LICENSE)
[sqlparser-rs](https://github.com/sqlparser-rs/sqlparser-rs) | Installed |  | [Apache 2.0](https://github.com/sqlparser-rs/sqlparser-rs/blob/main/LICENSE.TXT)
[travers](https://github.com/joocer/travers)               | Integrated  | 2023 [Justin Joyce](https://github.com/joocer)  | [Apache 2.0](https://github.com/joocer/travers/blob/main/LICENSE)
[typer](https://github.com/tiangolo/typer)                 | Installed   |   | [MIT](https://github.com/tiangolo/typer/blob/master/LICENSE)

Inclusion Types in this table:

- **Derived** components originated from this module but have undergone significant change.  
- **Installed** components are installed from PyPI/Cargo.  
- **Integrated** components have their source code (or significant parts of) included in the Opteryx codebase.  

This list does not include transitive dependencies nor is guaranteed to be complete. See the [dependency graph on GitHub](https://github.com/mabel-dev/opteryx/network/dependencies) for a more complete view of components used.

Only integrated components have copyright information listed, and best efforts have been made to ensure this information is accurate. However, if the copyright information is crucial for your use-case, we recommend verifying it independently. Should you find any inaccuracies, please [raise them as issues](https://github.com/mabel-dev/opteryx/issues/new?assignees=joocer&labels=Bug+%F0%9F%AA%B2&template=bug_report.md&title=%F0%9F%AA%B2) for prompt remediation. 

Integrated components may differ from their original versions. While we generally do not note cosmetic changes (e.g. PEP8 formatting), any alterations or additions to functionality are documented in the code comments. For derived components, we do not provide individual change notes, as these parts of the codebase have usually undergone substantial modifications, making such annotations less meaningful.

!!! Note   
    License information was last checked on 2022-06-03, or when specific entries were added to this document, if later.

## Other Assets

The [Icarus Opteryx](../../icarus-opteryx.png) image based on '[Evening: Fall of Day](https://collections.mfa.org/objects/30905)' by William Rimmer (Public Domain), more commonly associated with Led Zepplin's [Swan Song](https://en.wikipedia.org/wiki/Swan_Song_Records). The Icarus Opteryx image is created using visual components from 'Archaeopteryx' fossil image by Caro Asercion ([CC BY 3.0](https://github.com/game-icons/icons/blob/master/license.txt)).

Satellite and Planet datasets acquired from [devstronomy](https://github.com/devstronomy/nasa-data-scraper/tree/f610e541a053f05e26573570604aed50b358cc43/data/json).

Astronaut dataset acquired from [Kaggle](https://www.kaggle.com/nasa/astronaut-yearbook).

Exoplanet dataset acquired from [Kaggle](https://www.kaggle.com/datasets/nasa/kepler-exoplanet-search-results).

English wordlist acquired from [wordlists](https://github.com/kkrypt0nn/wordlists).

Spotify Charts dataset acquired from [Kaggle](https://www.kaggle.com/datasets/dhruvildave/spotify-charts) on September 17, 2023.

Space Mission dataset acquired from [Kaggle](https://www.kaggle.com/datasets/agirlcoding/all-space-missions-from-1957).

Diagrams created using [ASCII Flow](https://asciiflow.com/) or [draw.io](https://github.com/jgraph/drawio).

Website built using [mkdocs-material](https://github.com/squidfunk/mkdocs-material).

SQL-92 conformity tests are based on [sqltest](https://github.com/elliotchance/sqltest).

Documentation code color scheme based on [Dracula](https://draculatheme.com/).

## References and Guides

The following resources have been used as guides, references or patterns:

- [sqlglot](https://github.com/tobymao/sqlglot) Python Library
- [CMU DB Group](https://www.youtube.com/c/CMUDatabaseGroup) Lectures
- [DuckDB](https://duckdb.org/) embedded OLAP SQL Engine

## Uncredited Authors

ChatGPT has been used to assist in designing, refactoring, testing, debugging and documenting code.
