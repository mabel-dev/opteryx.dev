# How Opteryx is Tested

Testing in Opteryx is a cornerstone to ensure the system's performance, security, and correctness. This document outlines the key test harnesses used to maintain the high-quality standard of Opteryx.

Most testing is part of the main Opteryx repository on GitHub; however, some testing is located in other repositories.

## Unit Testing

**Frequency**: On Commit to GitHub   
**Maturity**: Medium  
**Location**: [mabel-dev/opteryx](https://github.com/mabel-dev/opteryx/tree/main/tests)

These tests are part of the CI process and focus on specific aspects of the internals (for example do functions like `SOUNDEX` produce the correct result). Combined with the SQL Battery test, the aim is for 95% coverage, with explicit exceptions. While 95% coverage does not guarantee that the tests are 'good,' it helps ensure that any material changes to the system function are captured early.

## SQL Battery

**Frequency**: On Commit to GitHub    
**Maturity**: Medium  
**Location**: [mabel-dev/opteryx](https://github.com/mabel-dev/opteryx/tree/main/tests)

Part of the CI process. Executes hundreds of hand-crafted (and some random) SQL statements against the engine.

The SQL Battery helps to ensure the entire application stack continues to perform as expected, when used in tandem with Unit Testing, which primarily focuses on ensuring parts work as they should, this provides a good level of confidence that all components are working together correctly.

The SQL battery has five types of test:

- Does the Query run - with no checking or validation of the outputs. Focussed on testing syntax and parsing.
- Does the Query fail - for scenarios when the query is expected to fail. Focused on negative testing.
- Is the shape of the results as expected - only the row and column counts are checked. Focused on high-volume query execution testing.
- Does the Query return the right results - the returned dataset is checked. Focused on ensuring results are correct.

The SQL Battery is the most effective test to identify when functionality has been broken or changed by updates. The shape testing is currently considered the best value of this suite - it is fast and easy to write new tests for, and the execution gives reasonable confidence in the correctness of the result in most situations.

## Performance Testing

**Frequency**: Ad hoc  
**Maturity**: Low  
**Location**: [mabel-dev/wrenchy-bench](https://github.com/mabel-dev/wrenchy-bench)

The performance testing framework can only be run ad hoc, and there is currently no meaningful treatment or tracking of outcomes. It is currently used to confirm that optimizations do reduce query execution times.

## SQL Logic Test

**Frequency**: Ad hoc  
**Maturity**: Very Low  
**Location**: [mabel-dev/wrenchy-bench](https://github.com/mabel-dev/wrenchy-bench)

Runs SQL statements in both Opteryx and DuckDB to verify Opteryx returns the same answer as DuckDB. This has a growing set of tests which are executed, but due to how relations are referenced in these systems, most queries require some hand-tuning and many are not possible with the framework as it is currently written.

What has been able to be tested has demonstrated some deviation between these systems, so is a valuable and useful test, even in its current form.

## Fuzzing

**Frequency**: On Commit to GitHub  
**Maturity**: Low  
**Location**: [mabel-dev/opteryx](https://github.com/mabel-dev/opteryx/tree/main/tests)

Fuzzing executes randomized data against the engine. There are currently three fuzzers:

- Random inputs fuzzer - used to help ensure the robustness of parameter handling
- Random `SELECT` statements - generates single table queries 
- Random `JOIN` statements - generates random JOIN conditions

The variation created by the statement fuzzers is limited and primarily is focused on creating variation in testing and in removing developer bias from test cases.

## Security & Code Quality Testing

**Frequency**: On Commit to GitHub    
**Maturity**: Medium  
**Location**: [mabel-dev/opteryx](https://github.com/mabel-dev/opteryx/tree/main/tests)

Various other tests are performed to help ensure code quality is maintained, these include security, form, typing, secret detection and test coverage checks using the following tools: Bandit, Ruff, MyPy, PyLint, PerfLint, Fides, SonarCloud, and Coverage.

## Summary

Opteryx employs a multifaceted testing approach, ranging from Unit Testing and SQL Battery to specialized performance and security assessments, all geared towards ensuring the SQL query engine's performance, security, and reliability. With robust regression testing, incremental evolution, and a focus on adaptability, we're committed to continually refining our test suites as the system evolves, aiming for the highest standards of quality and resilience in SQL query engine technology.