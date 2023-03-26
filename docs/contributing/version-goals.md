# Version Goals

Version goals are set out to provide a view of a road map. Goals are intended to demonstrate direction of enhancements and evolution of the engine, inclusion on the list does not guarantee delivery at a particular point in time, or at all. As always, conditions on the road may require you to consider your current path.

## Version 1.0

Version 1.0 goals will be delivered across various minor versions building toward v1.0. These minor releases will also include bug fixes, performance improvements and functional completeness. The items listed below are major pieces of functionality or milestones. Version numbers in brackets indicate when this feature was first introduced.

- :octicons-checkbox-24: CTEs (`WITH`) statements supported _(v0.8)_
- :octicons-checkbox-24: Read across multiple data sources (e.g. GCS and Postgres in the same query) _(v0.2)_
- :octicons-checkbox-24: Support different plaform data sources (e.g. FireStore _(v0.3)_ and Postgres _(v0.9)_)
- :octicons-checkbox-24: Rule-based query optimizer _(v0.5)_
- :octicons-checkbox-24: `JOIN` statements supported _(v0.1)_
- :octicons-checkbox-24: Functions using the result of Functions (e.g. `LENGTH(LIST(field))`) _(v0.3)_
- :octicons-checkbox-24: Inline operators (e.g. `firstname || surname`) _(v0.3)_
- :octicons-checkbox-24: Local Buffer Cache implemented _(v0.6)_

## After Version 1.0

These goals indicate which items are considered important for the engine to support, but we are willing to lower the priority against other items.

- :fontawesome-regular-square: Python PEP249 compatibility
- :fontawesome-regular-square: ANSI SQL92 compatibility
- :fontawesome-regular-square: All TPH-C statements execute
- :fontawesome-regular-square: Persisted materialized views
- :fontawesome-regular-square: Distributed execution
- :fontawesome-regular-square: Metastore used in planning and optimization
- :fontawesome-regular-square: Permissions Model for query types _(v.10)_ and dataset access
- :fontawesome-regular-square: Correctness benchmarks written _(v0.6)_, _(v0.9)_ and acceptable pass-rate obtained
- :fontawesome-regular-square: Performance benchmarks written _(v0.5)_, _(v0.9)_ and monitored
- :fontawesome-regular-square: JDBC connector
