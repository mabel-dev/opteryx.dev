
Version 0.11 looks pretty bare on the changelog, however a lot of work has been going on writing the new query planner. This is a major overhaul of this component and is the core part of phase one of a two-phase piece of work which aims to improve performance of the engine by implementing the following:

- Parallel execution of plans
- Predicate and Projection Pushdowns (*)

(*) This currently is done by trial-and-error and only on queries on a single relation

The second phase is primarily focused on rewriting the execution engine.

Writing the query planner isn't a small task, it's one of the four big components of Opteryx:

- The planner
- The optimizer
- The operators
- The execution engine

We took a serious look at SQLGlot, submitting some PRs whilst we reviewed to help ensure we were familiar with the internals of this library. We would recommend that if you're looking at writing an query engine in Python from scratch, it has a lot of great features included.

We're continuing to use sqlparser-rs, this is in part because there's some syntax SQLGlot doesn't support and there is already a wealth of supporting code in Opteryx for sqlparser-rs.

Why?

The need for significant changes to the planning phase was primarily driven by wanting to improve the optimizer. Whilst some heuristic optimizations have been implemented, some relied on queries only having a single table (predicate pushdowns) or relied on run-time trial-and-error (projection pushdowns). This was almost entirely due to not knowing the columns in the table before the execution step ran.

We knew we wanted to start moving towards a cost-based optimizer, and have been looking at data profiling approaches, but if we were waiting until the data was being read to learn its schema, we weren't going to be able to optimize based on statistics.

Whilst query optimization was the feature that we thought we had to rewrite the planner; there had been a number of bugs and feature requests which the existing planner could be forced to support, but would be easier with a new planner (e.g. support for UNION queries and support for CTEs to reference other CTEs).