# Version Goals

Until version 1.0 is released, a set of goals for an initial version are set out in place of a Road Map.

## Version 1.0

Version 1.0 goals will be delivered across various minor versions building toward v1.0. These minor releases will also include bug fixes, performance improvements and functional completeness. The items listed below are major pieces of functionality.

- 🔲 **Connection** Python PEP249 compatibility
- 🔲 **Planner** ANSI SQL92 compatibility
- 🔲 **Planner** CTEs (`WITH`) statements supported
- ✅ **Planner** Read across multiple data sources (e.g. GCS and Postgres in the same query) [v0.2]
- 🔲 **Planner** Support different plaform data sources (e.g. FireStore and BigQuery)
- ✅ **Planner** Rule-based query optimizer [v0.5]
- 🔲 **Planner** Metastore used in planning an optimizing
- ✅ **Execution** `JOIN` statements supported [v0.1]
- ✅ **Execution** Functions using the result of Functions (e.g. `LENGTH(LIST(field))`) [v0.3]
- ✅ **Execution** Inline operators (e.g. `firstname || surname`) [v0.3]
- 🔲 **Execution** Local Buffer Cache implemented
- 🔲 **Operation** Correctness benchmarks written and acceptable pass-rate obtained
- 🔲 **Operation** Performance benchmarks written and monitored
