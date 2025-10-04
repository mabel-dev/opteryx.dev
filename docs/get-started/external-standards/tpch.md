---
title: TPC-H Benchmark - Opteryx Query Performance Testing
description: Opteryx performance on TPC-H decision support benchmark. Query execution results and analytical workload testing.
---

# TPC-H Benchmark

!!! Note   
    Conformance is a work in progress. This page reflects the current implementation status to provide transparent insight into Opteryx’s capabilities and development progress.

!!! Note   
    PPerformance benchmarks should always be viewed with healthy skepticism. Benchmarks tend to be optimized for specific characteristics and workload patterns, and may not represent all factors that should be considered when comparing systems in real-world scenarios.

The [Transaction Processing Performance Council (TPC)](https://www.tpc.org/) publishes industry-standard benchmarks for evaluating database and computer system performance. [TPC-H](https://www.tpc.org/tpch/default5.asp) is a decision support benchmark comprising a suite of complex, business-oriented queries. It simulates real-world analytical workloads that scan large volumes of data, perform intensive joins and aggregations, and answer critical business questions.

## Why We Use TPC-H

We use TPC-H to evaluate Opteryx's capabilities in handling complex analytical queries typical of decision support systems. The benchmark helps us:

- **Identify feature gaps** - Understand which SQL features need implementation or improvement
- **Validate functionality** - Ensure query correctness and completeness
- **Track compatibility** - Monitor progress toward supporting industry-standard SQL patterns
- **Guide development** - Prioritize features based on real-world query patterns

## Query Results

Query   | Modified | Pass   | Issue
:------ | :------- | :----- | :-----
query1  | no       | yes    | -
query2  | yes      | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query3  | no       | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query4  | yes      | yes    | [Support EXISTS](https://github.com/mabel-dev/opteryx/issues/538)
query5  | no       | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query6  | no       | yes    | -
query7  | no       | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query8  | no       | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query9  | no       | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query10 | no       | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query11 | yes      | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query12 | no       | no     | [TPC-H 12 failure](https://github.com/mabel-dev/opteryx/issues/1920)
query13 | yes      | yes    | [Non-Equi JOINs](https://github.com/mabel-dev/opteryx/issues/1921)
query14 | no       | no     | Temporal Clauses
query15 | yes      | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query16 | no       | no     | [Implied Aliases](https://github.com/mabel-dev/opteryx/issues/1683) & [IN Subquery](https://github.com/mabel-dev/opteryx/issues/1361)
query17 | no       | no     | [Reimplement CTEs](https://github.com/mabel-dev/opteryx/issues/1352)
query18 | yes      | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query19 | no       | yes    | -
query20 | no       | no     | [IN Subquery](https://github.com/mabel-dev/opteryx/issues/1361)
query21 | yes      | no     | [Non-Equi JOINs](https://github.com/mabel-dev/opteryx/issues/1921)
query22 | yes      | no     | [Reimplement CTEs](https://github.com/mabel-dev/opteryx/issues/1352)

> :octicons-dot-16: query doesn't complete within a reasonable time

## Notes on Query Modifications

All queries have been modified to refer to the location of the datasets. The **Modified** column in the above table indicates where the SQL has been rewritten to replace unsupported functionality with supported functionality. This primarily occurs where the original query created a view or a temporary table—both of these have been replaced with Common Table Expression (CTE) definitions.

## Testing and Reproducibility

The test suite for this benchmark is maintained in the [Opteryx Benchmarking](https://github.com/mabel-dev/wrenchy-bench) repository. This allows for transparent verification of results and provides a framework for tracking progress as new features are implemented.

**Legal Notice**

TPC-H is Copyright © 1993-2022 Transaction Processing Performance Council.   
The full TPC-H specification in PDF format can be found [here](https://www.tpc.org/TPC_Documents_Current_Versions/pdf/TPC-H_v3.0.1.pdf).

TPC, TPC Benchmark, TPC-H are trademarks of the Transaction Processing Performance Council.