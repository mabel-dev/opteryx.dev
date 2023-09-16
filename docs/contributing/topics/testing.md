# How Opteryx is Tested

Testing in Opteryx is a cornerstone to ensure the system's performance, security, and correctness. This document outlines the key test harnesses used to maintain the high-quality standard of Opteryx.

Most testing is part of the main Opteryx repository on GitHub, however, some testing is located in other respositories.

## Unit Testing

**Frequency**: On Commit to GitHub   
**Maturity**: Medium  
**Location**: [mabel-dev/opteryx](https://github.com/mabel-dev/opteryx/tree/main/tests)

These tests are part of the CI process and focus on specific aspects of the internals. Combined with the SQL Battery test, the aim is for 95% coverage, with explicit exceptions. While 95% coverage does not guarantee that the tests are 'good,' it helps ensure that any material changes to the system function are captured early.

## SQL Battery

**Frequency**: On Commit to GitHub    
**Maturity**: Medium  
**Location**: [mabel-dev/opteryx](https://github.com/mabel-dev/opteryx/tree/main/tests)

Part of the CI process. Executes hundreds of hand-crafted (and some random) SQL statements against the engine.

The SQL Battery helps to ensure the entire application stack continues to perform as expected, when used in tandem with Unit Testing, which primarily focuses on ensuring parts work as they should, this provides a good level of confidence that all components are working together correctly.

The SQL battery has five types of test:

- Does the Query run - with no checking or validation of the outputs. Focussed on testing syntax and parsing.
- Does the Query fail - for scenarios when the query is expected to fail. Focused on negative testing.
- Is the shape of the results as expected - only the row and column counts are checked. Focused on high volume query execution testing.
- Does the Query return the right results - the returned dataset is checked. Focused on ensuring results are correct.
- SQL Fuzzing - execute randomly generated SQL queries. Focused on removing developer bias from test cases.

The SQL Battery the most effective test to identify when functionality has been broken or changed by updates. The shape testing is currently considered the best value of this suite - it is fast and easy to write new tests for this suite, and the execution give reasonable considence in the correctness of the result in most situations.

## Performance Testing

**Frequency**: Ad hoc  
**Maturity**: Low  
**Location**: [mabel-dev/wrenchy-bench](https://github.com/mabel-dev/wrenchy-bench)

The performance testing framework is only able to be run ad hoc, and there is currently no meaningful treatment or tracking out outcomes. It us currently used to confirm optimizations do have the impact of reducing query execution times.

## SQL Logic Test

**Frequency**: Ad hoc  
**Maturity**: Low  
**Location**: [mabel-dev/wrenchy-bench](https://github.com/mabel-dev/wrenchy-bench)

Runs SQL statements in both Operyx and DuckDB to verify Opteryx returns the same answer as DuckDB. This has a growing set of tests which are executed, but as how relations are referenced in these systems, most queries require some hand-tuning and many are not possible with the framework as it currently is written.

What has been able to be tested has demonstrated some deviation between these systems, so is a valuable and useful test, even in its current form.

## Fuzzing

**Frequency**: On Commit to GitHub & Nightly  
**Maturity**: Low  
**Location**: [mabel-dev/opteryx](https://github.com/mabel-dev/opteryx/tree/main/tests)

As part of the CI process, executes 100 iterations of random inputs.

As part of a nightly test, executes 100,000 iterations of random inputs.

Fuzzing supplies some key functions with random data to try to capture scenarios which are unexpected or unhandled.

## Security & Code Quality Testing

**Frequency**: On Commit to GitHub    
**Maturity**: Medium  
**Location**: [mabel-dev/opteryx](https://github.com/mabel-dev/opteryx/tree/main/tests)

Various other tests are performed to help ensure code quality is maintained, these include security, form, typing, secret detection and test coverage checks using the following tools: Bandit, Semgrep, Black, MyPy, PyLint, PerfLint, Fides, SonarCloud, and Coverage.

## Summary

Opteryx employs a multifaceted testing approach, ranging from Unit Testing and SQL Battery to specialized performance and security assessments, all geared towards ensuring the SQL query engine's performance, security, and reliability. With robust regression testing, incremental evolution, and a focus on adaptability, we're committed to continually refining our test suites as the system evolves, aiming for the highest standards of quality and resilience in SQL query engine technology.