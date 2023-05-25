

Writing the query planner isn't a small task, it's one of the four big components of Opteryx:

- The planner
- The optimizer
- The operators
- The execution engine

Looked at SQLGlot, which I recommend if you're looking at writing an engine from scratch; it comes with a hueristic optimizer.

We're continuing to use sqlparser-rs, this is in part because there's some syntax SQLGlot doesn't support and there is already a wealth of supporting code in Opteryx for sqlparser-rs.

Why?

The need for significant changes to the planning phase was primarily driven by wanting to improve the optimizer. Whilst some heuristic optimizations have been implemented, some relied on queries only having a single table (predicate pushdowns) or relied on run-time trial-and-error (projection pushdowns). This was almost entirely due to not knowing the columns in the table before the execution step ran.

We knew we wanted to start moving towards a cost-based optimizer, and have been looking at data profiling approaches, but if we were waiting until the data was being read to learn its schema, we weren't going to be able to optimize based on statistics.

Whilst query optimization was the feature that we thought we had to rewrite the planner; there had been a number of bugs and feature requests which the existing planner could be forced to support, but would be easier with a new planner (e.g. support for UNION queries and support for CTEs to reference other CTEs).