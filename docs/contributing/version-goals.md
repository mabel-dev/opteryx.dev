# Version Goals

Version goals are set out to provide a view of a road map. Goals are intended to demonstrate direction of enhancements and evolution of the engine, inclusion on the list does not guarantee delivery at a particular point in time, or at all. As always, conditions on the road may require you to consider your current path.

## Version 1.0

Version 1.0 goals will be delivered across various minor versions building toward v1.0. These minor releases will also include bug fixes, performance improvements and functional completeness. The items listed below are major pieces of functionality or milestones.

- :fontawesome-regular-square: **Connection** Python PEP249 compatibility
- :fontawesome-regular-square: **Planner** ANSI SQL92 compatibility
- :fontawesome-regular-square: **Planner** CTEs (`WITH`) statements supported
- :octicons-checkbox-24: **Planner** Read across multiple data sources (e.g. GCS and Postgres in the same query) [v0.2]
- :fontawesome-regular-square: **Planner** Support different plaform data sources (e.g. FireStore [v0.3] and BigQuery)
- :octicons-checkbox-24: **Planner** Rule-based query optimizer [v0.5]
- :fontawesome-regular-square: **Planner** Metastore used in planning an optimizing
- :octicons-checkbox-24: **Execution** `JOIN` statements supported [v0.1]
- :octicons-checkbox-24: **Execution** Functions using the result of Functions (e.g. `LENGTH(LIST(field))`) [v0.3]
- :octicons-checkbox-24: **Execution** Inline operators (e.g. `firstname || surname`) [v0.3]
- :octicons-checkbox-24: **Execution** Local Buffer Cache implemented [v0.6]
- :fontawesome-regular-square: **Operation** Correctness benchmarks written [v0.6] and acceptable pass-rate obtained
- :fontawesome-regular-square: **Operation** Performance benchmarks written [v0.5] and monitored

## Version 2.0

Version 2.0 goals indicate which items are considered important for the engine to support, but we are willing to lower the priority against other items.

- :fontawesome-regular-square: **Operation** Persisted materialized views
- :fontawesome-regular-square: **Execution** Distributed execution
