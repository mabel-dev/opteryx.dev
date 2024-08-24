# TPC-H Benchmark

!!! Note   
    Conformance is a work in progress and this information represents the current state in order to provide transparent information about progress and capability.

[TPC](https://www.tpc.org/) publish a set of benchmarks for computer and database systems. [TPC-H](https://www.tpc.org/tpch/default5.asp) is a decision support benchmark which consists of a set of business-oriented queries. This benchmark demonstrates a decision support system that examines large amounts of data, executes highly complex queries, and answers key business questions. 

Query   | Modified | Pass   | Issue
:------ | :------- | :----- | :-----
query1  | no       | yes    | -
query2  | yes      | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query3  | no       | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query4  | no       | no     | [Support EXISTS](https://github.com/mabel-dev/opteryx/issues/538)
query5  | no       | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query6  | no       | yes    | -
query7  | no       | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query8  | no       | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query9  | no       | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query10 | no       | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query11 | yes      | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query12 | no       | no     | [TPC-H 12 failure](https://github.com/mabel-dev/opteryx/issues/1920)
query13 | no       | no     | [Non-Equi JOINs](https://github.com/mabel-dev/opteryx/issues/1921)
query14 | no       | no     | Temporal Clauses
query15 | yes      | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query16 | no       | no     | [Implied Aliases](https://github.com/mabel-dev/opteryx/issues/1683) & [IN Subquery](https://github.com/mabel-dev/opteryx/issues/1361)
query17 | no       | no     | [Reimplement CTEs](https://github.com/mabel-dev/opteryx/issues/1352)
query18 | yes      | no     | [Multiway CROSS JOINs](https://github.com/mabel-dev/opteryx/issues/1438)
query19 | no       | no     | Internal Error
query20 | no       | no     | [IN Subquery](https://github.com/mabel-dev/opteryx/issues/1361)
query21 | yes      | no     | [Non-Equi JOINs](https://github.com/mabel-dev/opteryx/issues/1921)
query22 | yes      | no     | [Reimplement CTEs](https://github.com/mabel-dev/opteryx/issues/1352)

> :octicons-dot-16: query doesn't complete within a reasonable time

All queries have been modified to refer to the location of the datasets, **modified** in the above table is where the SQL has been written to replace unsupported functionality with supported functionality - this is where the original query either created a view or a temporary table, both of these have been replaced with a CTE definition.

The test suite for this benchmark is in the [Opteryx Benchmarking](https://github.com/mabel-dev/wrenchy-bench) repository.

TPC-H is Copyright © 1993-2022 Transaction Processing Performance Council. The full TPC-H specification in PDF format can be found [here](https://www.tpc.org/TPC_Documents_Current_Versions/pdf/TPC-H_v3.0.1.pdf).

TPC, TPC Benchmark, TPC-H are trademarks of the Transaction Processing Performance Council.