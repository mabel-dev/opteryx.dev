# TPC-H Benchmark

!!! Note   
    Conformance is a work in progress and this information represents the current state in order to provide transparent information about progress and capability.

[TPC](https://www.tpc.org/) publish a set of benchmarks for computer and database systems. [TPC-H](https://www.tpc.org/tpch/default5.asp) is a decision support benchmark which consists of a set of business-oriented queries. This benchmark demonstrates a decision support system that examines large amounts of data, executes highly complex queries, and answers key business questions. 

Query   | Modified | Pass
:------ | :------- | :-----
query1  | no       | yes
query2  | yes      | no
query3  | no       | no
query4  | no       | no
query5  | no       | no
query6  | no       | yes
query7  | no       | no
query8  | no       | no
query9  | no       | no
query10 | no       | no
query11 | yes      | no
query12 | no       | no
query13 | no       | no
query14 | no       | unknown
query15 | yes      | no
query16 | no       | no
query17 | no       | no
query18 | yes      | no
query19 | no       | unknown
query20 | no       | no
query21 | yes      | no
query22 | yes      | no

All queries have been modified to refer to the location of the datasets, **modified** in the above table is where the SQL has been written to replace unsupported functionality with supported functionality - this is where the original query either created a view or a temporary table, both of these have been replaced with a CTE definition.

The test suite for this benchmark is in the [Opteryx Benchmarking](https://github.com/mabel-dev/wrenchy-bench) repository.

TPC-H is Copyright © 1993-2022 Transaction Processing Performance Council. The full TPC-H specification in PDF format can be found [here](https://www.tpc.org/TPC_Documents_Current_Versions/pdf/TPC-H_v3.0.1.pdf).

TPC, TPC Benchmark, TPC-H are trademarks of the Transaction Processing Performance Council.