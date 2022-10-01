# Building our first Optimizer

_1st October 2022_

Building a SQL query engine is no trivial task, we started building [Opteryx](https://opteryx.dev) about 10 months ago on a complete rewrite of our first query engine. It's only recently we've started to focus on improving performance, initially the performance of the new engine was such a massive improvement over the old, almost purely due to architectural differences, there is a lot of room for improvement.

We since users started using the engine about five months ago we've been able to implement some point improvements.

- Selection before Aggregation, this isn't implemented by an Optimizer, instead it was part of the Aggregator Operator.
- We've also implemented page merging into the Selection Operator to make the most of SIMD and parallel execution.

This week saw the first iteration of plan-based optimization, where the Optimizer receives a query plan and uses rules to rewrite it to run faster.

All complex systems are built on something simple. Our first iteration of the Optimizer is simple. It currently does one action - it takes AND conjunctions in the WHERE and HAVING clauses and splits them into individual Selection Operators to run in serial.

The effect of doing this, with no intelligence to the order or other factors, has been observed to be up to a 85% reduction in the execution time of the Selection step of real-world queries - i.e. ones we see being written and run by users.

The query time is still dominated by the read time in most situations, but saving 6 seconds on a 42 second query is still meaningful.

The Optimizer is heuristic, that is, it has some simple rules when it applies. It is not cost-based as we've not built a statistics model and store to compliment the Optimizer yet. This is the expected evolution of the planner, but for now we will focus on extending the rule-based planner with more rules.

We look forward to being able to update you on other major updates and improvements to [Opteryx](https://opteryx.dev).
