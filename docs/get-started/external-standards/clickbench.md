---
title: ClickBench Performance - Opteryx Benchmark Results
description: Opteryx performance on ClickBench benchmark. Compare query execution speed against other SQL engines and databases.
---

# ClickBench

!!! Note   
    Performance benchmarks should always be viewed with healthy skepticism. Benchmarks tend to be optimized for specific characteristics and workload patterns, and may not represent all factors that should be considered when comparing systems in real-world scenarios.

## What is ClickBench?

[ClickBench](https://benchmark.clickhouse.com/) is a public benchmarking suite developed by [ClickHouse, Inc.](https://clickhouse.com/), designed to evaluate the performance of analytical databases under real-world, single-table summarization workloads. It provides a standardized environment for comparing query execution speed, efficiency, and scalability across different database systems and query engines.

The benchmark uses the ClickHouse Hits dataset, which contains 100 million rows of anonymized web analytics data, testing a variety of analytical queries including aggregations, filters, and group-by operations.

## Why We Use ClickBench

We use ClickBench to measure how well Opteryx performs on a variety of analytical queries compared to similarly architected and industry-leading databases and query engines. These standardized results help us:

- **Identify optimization opportunities** - Understanding where Opteryx can improve relative to other systems
- **Validate performance** - Ensuring our engine meets established performance expectations
- **Track progress** - Monitoring performance improvements over time as we enhance the engine
- **Provide transparency** - Giving users objective data to inform their technology decisions

## Reproducing Our Results

You can find detailed information on how to reproduce Opteryx's ClickBench results in the [ClickBench GitHub repository](https://github.com/ClickHouse/ClickBench/tree/main/opteryx).

Our benchmarking process is fully documented and reproducible, allowing you to:

- **Verify results** - Run the same benchmarks in your own environment
- **Compare performance** - Evaluate Opteryx against other engines with your data
- **Understand methodology** - Review the exact configuration and dataset used
- **Customize tests** - Adapt benchmarks to your specific use case

## Interpreting Results

When reviewing ClickBench results, consider:

- **Hardware variations** - Performance can vary significantly based on CPU, memory, and storage
- **Configuration differences** - Settings and optimizations affect results
- **Data characteristics** - Your data may have different patterns than the benchmark dataset
- **Query patterns** - Real-world workloads may differ from standardized benchmarks
- **Version differences** - Performance improves over time as engines are optimized

Use benchmark results as one data point among many when evaluating query engines for your specific needs.

---

ClickHouse is a registered trademark of ClickHouse, Inc. https://clickhouse.com
