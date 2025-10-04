# Binder

The Binder is a critical component in the Opteryx query engine that bridges the gap between the logical query plan and the physical execution. It resolves all identifiers (table names, column names, aliases) to their actual schemas and validates that the query is semantically correct.

## Purpose

The primary purposes of the Binder are:

1. **Identifier Resolution**: Map all column and table references to their actual data sources
2. **Schema Binding**: Associate each identifier with complete schema information (data type, nullable, source relation, etc.)
3. **Type Checking**: Validate that operations are performed on compatible data types
4. **Ambiguity Detection**: Identify and report ambiguous column references that could refer to multiple sources
5. **Variable Substitution**: Replace query parameters and variables with their actual values
6. **Temporal Binding**: Add temporal information for time-travel queries

## How It Works

### Column Resolution

When the binder encounters a column reference, it must determine which relation (table, subquery, CTE) the column comes from. The process is:

1. Search all available schemas in the current context
2. Check if the column exists in exactly one schema (if multiple matches, report ambiguity)
3. Create a `FlatColumn` object with the column's metadata:
   - Column name and any alias
   - Data type
   - Source relation
   - Source column name (may differ from the reference if aliased)

### Schema Context

The binder maintains a context of available schemas as it traverses the query plan. This context includes:

- Schemas from scanned relations (tables, views)
- Schemas from subqueries and CTEs
- Schemas created by previous operators in the plan

As operators are bound, the available schema context changes. For example, a projection changes which columns are available to downstream operators.

### Column Types

The binder works with different types of columns:

#### Identifier Columns

These reference columns from relations:

- `node_type` is `IDENTIFIER`
- `schema_column` is a `FlatColumn`
- `source` is the relation (remote dataset, subquery, CTE)
- `source_column` is the name of the column at the source

```python
FlatColumn(
    alias=alias,  # AS alias, if provided
    source_column=branch[-1]["value"],  # the source column name
    source=".".join(p["value"] for p in branch[:-1]),  # the source relation
)
```

#### Literal Columns

These are constant values in the query:

- `node_type` is `LITERAL`
- `schema_column` is a `ConstantColumn`
- `type` is the data type of the constant

The value is retrieved from `schema_column.value`.

#### Computed Columns

These are expressions that produce new columns (e.g., `price * quantity`).

## Examples

### Simple Query

```sql
SELECT name, age FROM users
```

The binder will:
1. Resolve `users` to a data source and load its schema
2. Confirm `name` and `age` columns exist in the `users` schema
3. Create bound column references with full type information

### Ambiguous Reference

```sql
SELECT id 
  FROM users 
  JOIN orders 
    ON users.id = orders.user_id
```

If both `users` and `orders` have an `id` column, the binder will raise an `AmbiguousIdentifierError` because it cannot determine which `id` is being requested in the SELECT clause.

### With Alias

```sql
SELECT u.name, o.total 
  FROM users AS u 
  JOIN orders AS o 
    ON u.id = o.user_id
```

The binder will:
1. Register `users` with alias `u`
2. Register `orders` with alias `o`  
3. Resolve `u.name` to `users.name`
4. Resolve `o.total` to `orders.total`

## Implementation Details

The binder is implemented in `/opteryx/planner/binder/` with several key files:

- `binder.py`: Main binding logic and helper functions
- `binder_visitor.py`: Traverses the query plan and applies binding
- `binding_context.py`: Manages the schema context during binding
- `operator_map.py`: Maps operators to their schema transformations

The binder operates after the logical planner creates the initial query plan, but before optimization. This ensures the optimizer has complete schema information to make informed decisions.
