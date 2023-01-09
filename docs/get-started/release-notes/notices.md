# Notices

## Incorporated Components

Opteryx is built on the shoulders of other great libraries and components:

Library           | Disposition       | Copyright            | Licence   
:---------------- | :---------------- | :------------------- | :--------------- 
[cityhash](https://github.com/escherba/python-cityhash)    | Installed   |  | [Bespoke](https://github.com/escherba/python-cityhash/blob/master/LICENSE)  
[cython](https://github.com/cython/cython)                 | Installed   |  | [Apache 2.0](https://github.com/cython/cython/blob/master/LICENSE.txt)
[datasketch](https://github.com/ekzhu/datasketch)          | Integrated  | 2015 [Eric Zhu](https://github.com/ekzhu) | [MIT](https://github.com/ekzhu/datasketch/blob/master/LICENSE)
[datetime_truncate](https://github.com/mediapop/datetime_truncate) | Integrated | 2020 [Media Pop](https://github.com/mediapop) | [MIT](https://github.com/mediapop/datetime_truncate/blob/master/LICENSE)
[distogram](https://github.com/maki-nage/distogram)        | Integrated  | 2020 [Romain Picard](https://github.com/MainRo) | [MIT](https://github.com/maki-nage/distogram/blob/master/LICENSE.txt)
[fuzzy](https://github.com/yougov/fuzzy)                   | Integrated | [Jason R. Coombs](https://github.com/jaraco) | [MIT](https://github.com/yougov/fuzzy/blob/master/LICENSE)
[levenshtein](https://gist.github.com/vatsal220/6aefbc245216bc9f2da8556f42e1c89c#file-lev_dist-py) | Integrated | [Vatsal Patel](https://gist.github.com/vatsal220) | Public Domain (assumed)
[mbleven](https://github.com/fujimotos/mbleven)            | Integrated  | 2018 [Fujimoto Seiji](https://github.com/fujimotos) | [Public Domain](https://github.com/fujimotos/mbleven/blob/master/LICENSE)
[numpy](https://github.com/numpy/numpy)                    | Installed   |  | [BSD-3](https://github.com/numpy/numpy/blob/main/LICENSE.txt)
[orjson](https://github.com/ijl/orjson)                    | Installed   |  | [Apache 2.0](https://github.com/ijl/orjson/blob/master/LICENSE-APACHE)
[pyarrow](https://github.com/apache/arrow/)                | Installed   |  | [Apache 2.0](https://github.com/apache/arrow/blob/master/LICENSE.txt)
[pyarrow_ops](https://github.com/TomScheffers/pyarrow_ops) | Derived  | [TomScheffers](https://github.com/TomScheffers) (assumed) | [Apache 2.0](https://github.com/TomScheffers/pyarrow_ops/blob/main/LICENSE)
[pyyaml](https://pyyaml.org/)                              | Installed   |  | [MIT](https://github.com/yaml/pyyaml/blob/master/LICENSE)
[sqloxide](https://github.com/wseaton/sqloxide)            | Integrated  | 2020 [Will Eaton](https://github.com/wseaton) | [MIT](https://github.com/wseaton/sqloxide/blob/master/LICENSE)
[sqlparser-rs](https://github.com/sqlparser-rs/sqlparser-rs) | Installed |  | [Apache 2.0](https://github.com/sqlparser-rs/sqlparser-rs/blob/main/LICENSE.TXT)
[typer](https://github.com/tiangolo/typer)                 | Installed   |   | [MIT](https://github.com/tiangolo/typer/blob/master/LICENSE)

&emsp;**Derived** components originated from this module but has undergone significant change.  
&emsp;**Installed** components are installed from PyPI/Cargo.  
&emsp;**Integrated** components have their source code (or significant parts of) included in the Opteryx codebase.  

This list does not include transitive dependencies nor is guaranteed to be complete. Only components which have been integrated have copyright information noted, best efforts have been made to ensure this information is correct. Corrections should be [raised as issues](https://github.com/mabel-dev/opteryx/issues/new?assignees=joocer&labels=Bug+%F0%9F%AA%B2&template=bug_report.md&title=%F0%9F%AA%B2) for remediation. 

Integrated components may differ from their original form. Cosmetic changes are not generally noted however where functionality has been added or altered, this is recorded in comments. 

!!! Note   
    License information was last checked on 2022-06-03, or when specific entries were added to this document, if later.

## Other Assets

The [Icarus Opteryx](../../icarus-opteryx.png) image based on '[Evening: Fall of Day](https://collections.mfa.org/objects/30905)' by William Rimmer (Public Domain), more commonly associated with Led Zepplin's [Swan Song](https://en.wikipedia.org/wiki/Swan_Song_Records). The Icarus Opteryx image is created using visual components from 'Archaeopteryx' fossil image by Caro Asercion ([CC BY 3.0](https://github.com/game-icons/icons/blob/master/license.txt)).

Satellite and Planet datasets acquired from [devstronomy](https://github.com/devstronomy/nasa-data-scraper/tree/f610e541a053f05e26573570604aed50b358cc43/data/json).

Astronaut dataset acquired from [Kaggle](https://www.kaggle.com/nasa/astronaut-yearbook).

Exoplanet dataset acquire from [Kaggle](https://www.kaggle.com/datasets/nasa/kepler-exoplanet-search-results).

Diagrams created using [ASCII Flow](https://asciiflow.com/) or [draw.io](https://github.com/jgraph/drawio).

Website build using [mkdocs-material](https://github.com/squidfunk/mkdocs-material).

SQL-92 conformity tests are based on [sqltest](https://github.com/elliotchance/sqltest).