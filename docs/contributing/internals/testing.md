# How Opteryx is Tested

Opteryx utilizes a number of test approaches to help ensure the system is performant, secure and correct. The key test harnesses which are used to test Opteryx are listed here.

Most testing is part of the main Opteryx repository on GitHub, however, some testing is located in other respositories.

## Unit Testing

**Frequency**: CI  
**Maturity**: Medium  
**Location**: [mabel-dev/opteryx](https://github.com/mabel-dev/opteryx/tree/main/tests)

Part of the CI process. Tests specific aspects of the internals.

Combined with the SQL Battery test, the aim is for 95% coverage (with explicit exceptions). Whilst 95% coverage does not ensure the tests are 'good', it does help ensures any material changes to the function of the system are captured early.

## SQL Battery

**Frequency**: CI  
**Maturity**: Medium  
**Location**: [mabel-dev/opteryx](https://github.com/mabel-dev/opteryx/tree/main/tests)

Part of the CI process. Executes hundreds of hand-crafted SQL statements against the engine.

The SQL Battery helps to ensure the entire system performs as expected and when used in tandem with Unit Testing, which primarily focuses on ensuring parts work as they should, this provides a level of confidence that the system continues to perform as expected.

The battery essentially has three variations:

- Does the Query run - with no checking or validation of the outputs
- Does the Query fail - for scenarios when the query is expected to fail
- Is the shape of the results as expected - only the row and column counts are checked

The SQL Battery testing is currently the most effective test to identify broken functionality.

## Performance Testing

**Frequency**: Ad hoc  
**Maturity**: Low  
**Location**: [mabel-dev/wrenchy-bench](https://github.com/mabel-dev/wrenchy-bench)

To measure impact of changes.

## SQL Logic Test

**Frequency**: Ad hoc  
**Maturity**: Low  
**Location**: [mabel-dev/wrenchy-bench](https://github.com/mabel-dev/wrenchy-bench)

Runs SQL statements against Operyx and DuckDB to verify Opteryx returns the same answer as DuckDB.

## Fuzzing

**Frequency**: CI & Nightly  
**Maturity**: Low  
**Location**: [mabel-dev/opteryx](https://github.com/mabel-dev/opteryx/tree/main/tests)

As part of the CI process, executes 100 iterations of random inputs.

As part of a nightly test, executes 100,000 iterations of random inputs.

Fuzzing supplies some key functions with random data to try to capture scenarios which are unexpected or unhandled.

## Security & Code Quality Testing

**Frequency**: CI  
**Maturity**: Medium  
**Location**: [mabel-dev/opteryx](https://github.com/mabel-dev/opteryx/tree/main/tests)

Various other tests are performed to help ensure code quality is maintained, these include security, form, typing, secret detection and test coverage checks using the following tools: Bandit, Semgrep, Black, MyPy, PyLint, PerfLint, Fides, SonarCloud, and Coverage.