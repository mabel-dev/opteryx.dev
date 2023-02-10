# Version Goals

Version goals are set out to provide a view of a road map. Goals are intended to demonstrate direction of enhancements and evolution of the engine, inclusion on the list does not guarantee delivery at a particular point in time, or at all. As always, conditions on the road may require you to consider your current path.

## Version 1.0

Version 1.0 goals will be delivered across various minor versions building toward v1.0. These minor releases will also include bug fixes, performance improvements and functional completeness. The items listed below are major pieces of functionality or milestones.

- :octicons-checkbox-24: CTEs (`WITH`) statements supported [v0.8]
- :octicons-checkbox-24: Read across multiple data sources (e.g. GCS and Postgres in the same query) [v0.2]
- :octicons-checkbox-24: Support different plaform data sources (e.g. FireStore [v0.3] and Postgres [v0.9])
- :octicons-checkbox-24: Rule-based query optimizer [v0.5]
- :octicons-checkbox-24: `JOIN` statements supported [v0.1]
- :octicons-checkbox-24: Functions using the result of Functions (e.g. `LENGTH(LIST(field))`) [v0.3]
- :octicons-checkbox-24: Inline operators (e.g. `firstname || surname`) [v0.3]
- :octicons-checkbox-24: Local Buffer Cache implemented [v0.6]

## After Version 1.0

These goals indicate which items are considered important for the engine to support, but we are willing to lower the priority against other items.

- :fontawesome-regular-square: Python PEP249 compatibility
- :fontawesome-regular-square: ANSI SQL92 compatibility
- :fontawesome-regular-square: All TPH-C statements execute
- :fontawesome-regular-square: Persisted materialized views
- :fontawesome-regular-square: Distributed execution
- :fontawesome-regular-square: Metastore used in planning and optimization
- :fontawesome-regular-square: Permissions Model
- :fontawesome-regular-square: Correctness benchmarks written [v0.6, v0.9] and acceptable pass-rate obtained
- :fontawesome-regular-square: Performance benchmarks written [v0.5, v0.9] and monitored
