# Information Schema Conformity (MySQL)

!!! Note   
    Conformance is a work in progress and this information represents the current state in order to provide transparent information about progress and capability.

Opteryx aims to implement parts of the [MySQL Information Schema](https://dev.mysql.com/doc/refman/8.0/en/information-schema-table-reference.html) interface. If a view is not listed below, the current intention is to not support it.

The initial use cases for support for the Information Schema is to allow tools like Power BI to connect to Opteryx (via [mesos](https://github.com/mabel-dev/mesos)).

## Schema

View                              | Support
:-------------------------------- | :----------------
information_schema.columns        | None
information_schema.schemata       | None
information_schema.tables         | Empty Response
information_schema.views          | Empty Response


Support statuses in this table:
 
- **None** The feature is not supported.  
- **Empty Response** Responses are empty or incomplete