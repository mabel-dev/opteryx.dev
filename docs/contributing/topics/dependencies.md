# Managing External Dependencies

Opteryx undertakes two approaches to managing external dependencies:

- Assimilation into the Opteryx codebase, where possible   
- Automatic Installation via package managers

## Assimilation

This approach provides maximum control over the dependency and simplifies the complexities of installing and managing them. It creates opportunities for parts to be optimized or removed and subjects the components to the same quality controls as first-party Opteryx code. Criteria for assimilation often include stability of the library, a compatible set of onward dependencies, and alignment with Opteryx's performance goals.

## Installation

Some components are not good candidates for assimilation. This is primarily due to their complexity or because their feature set is rapidly evolving, making snapshotting a version counterproductive in the long term. These components are typically installed automatically via package managers like PyPI or Cargo, requiring no manual intervention from the end user.

## Guiding Principles

Opteryx is designed with the philosophy of adaptability and incremental evolution. Unlike systems that rely heavily on version pinning, leading to fragility and increased vulnerability, Opteryx prioritizes:

- **Robust Regression Testing**: A comprehensive suite of regression tests ensures that updates to dependencies do not break existing functionality.
- **Security Vigilance**: Being in a constant state of adaptability allows us to quickly respond to security vulnerabilities in dependent libraries, minimizing risk and exposure.
- **Incremental Evolution**: Instead of large-scale rewrites, our approach allows for more manageable, incremental changes, thereby reducing both development time and the likelihood of introducing new issues.

By adhering to these principles, Opteryx aims to circumvent the common pitfalls of software stagnation and vulnerability risks associated with tightly bound component versions.

## Summary

Managing external dependencies in a way that aligns with Opteryx's core principles of robustness, security, and incremental evolution ensures that the system remains agile and resilient against both software stagnation and security vulnerabilities.