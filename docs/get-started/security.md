# Security

## Statement Execution Restrictions

Opteryx allows you to prevent users from executing classes of query, for example you may limit a population of users to just being able to run `SELECT` statements, and prevent them from running other types of query.

This can be used to limit user's ability to perform certain actions on the engine; for example limiting users to only perform `EXECUTE` queries.

Below is the complete list of permissions and the SQL query keyword which indicates that query type:

Permission    | Query Keyword
------------- | -------------------
Analyze       | `ANALYZE` :octicons-beaker-24: 
Execute       | `EXECUTE` :octicons-beaker-24: 
Explain       | `EXPLAIN`
Query         | `SELECT`
SetVariable   | `SET`
ShowColumns   | `SHOW COLUMNS`
ShowCreate    | `SHOW CREATE`
ShowFunctions | `SHOW FUNCTIONS`
ShowVariables | `SHOW VARIABLES`
ShowVariable  | `SHOW`

!!! Note
    - `Analyze` and `Execute` and not fully supported statements.
    - `ShowVariable` only applies to queries that are not one of the more specific `SHOW` query types.