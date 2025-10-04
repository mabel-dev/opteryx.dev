# JOINs

JOINs are a fundamental operation in SQL that combine rows from two or more relations based on related columns. Opteryx implements several JOIN algorithms optimized for different scenarios.

## JOIN Types

Opteryx supports the following JOIN types:

- **INNER JOIN**: Returns rows when there is a match in both relations
- **LEFT OUTER JOIN**: Returns all rows from the left relation and matching rows from the right
- **RIGHT OUTER JOIN**: Returns all rows from the right relation and matching rows from the left
- **FULL OUTER JOIN**: Returns all rows when there is a match in either relation
- **CROSS JOIN**: Returns the Cartesian product of both relations
- **ANTI JOIN**: Returns rows from the left relation that have no match in the right
- **SEMI JOIN**: Returns rows from the left relation that have a match in the right

## JOIN Implementations

### Inner Join

Opteryx implements optimized INNER JOINs with multiple strategies:

**Implementation**: `inner_join_node.py`

The inner join operator uses hash-based joining for efficiency:

1. Build a hash table from the smaller relation (build side)
2. Probe the hash table with rows from the larger relation (probe side)
3. Return matching rows

This approach provides O(n + m) average-case performance where n and m are the sizes of the relations.

### Cross Join

**Implementation**: `cross_join_node.py`

Cross joins return the Cartesian product of two relations. These are optimized for:

- Streaming execution to avoid materializing the full product
- Integration with `UNNEST` operations for array expansion
- Memory-efficient chunked processing

### Nested Loop Join

**Implementation**: `nested_loop_join_node.py`

The nested loop join is used when:

- Hash-based joining is not suitable (e.g., non-equality predicates)
- One relation is very small
- As a fallback when other join strategies cannot be applied

This has O(n × m) complexity but works for all join conditions.

### Outer Joins

**Implementation**: `outer_join_node.py`

Outer joins (LEFT, RIGHT, FULL) are currently delegated to PyArrow for execution. This ensures:

- Correct null-extension semantics
- Efficient processing of large datasets
- Compatibility with PyArrow's optimized implementations

### Filter Join

**Implementation**: `filter_join_node.py`

Filter joins are an optimization where:

- A filter predicate is pushed down into a join condition
- Reduces the amount of data that needs to be joined
- Can significantly improve performance when filters are selective

### UNNEST Join

**Implementation**: `unnest_join_node.py`

UNNEST joins are specialized for expanding array or list columns:

- Each array element becomes a separate row
- Combined with CROSS JOIN for efficient expansion
- Preserves proper relationships between parent and expanded rows

## JOIN Optimization

The query optimizer applies several strategies to improve JOIN performance:

### Join Ordering

The optimizer can reorder joins to process smaller intermediate results:

- Statistics from the catalog help estimate relation sizes
- Smaller relations are typically used as the build side
- Filter pushdown reduces relation sizes before joining

### Predicate Pushdown

Filters are pushed as close to data sources as possible:

- Reduces the number of rows entering the join
- Can push predicates into storage engines (e.g., SQL databases, Parquet files)
- Applies both before and during join operations

### Correlated Filters

When a column in a JOIN has a known value range:

- Push corresponding filters to both sides of the JOIN
- Reduces the size of datasets that need to be joined
- Implemented in the `CorrelatedFiltersStrategy`

## Performance Considerations

### Hash Join Performance

Hash joins work best when:

- The join condition uses equality predicates
- The build side fits in memory
- Hash keys have good distribution (low collisions)

### Memory Management

Opteryx manages JOIN memory carefully:

- Streams data in chunks (morsels) to limit memory usage
- Uses the buffer pool for temporary storage
- Spills to disk for very large joins (future optimization)

### Join Statistics

The executor tracks JOIN statistics:

- Number of rows from each side
- Number of matches produced
- Hash table size and collision rate
- Time spent in build vs. probe phases

## Example Query Plans

### Simple Inner Join

```sql
SELECT u.name, o.total
FROM users u
JOIN orders o ON u.id = o.user_id
```

Plan:
```
Project [u.name, o.total]
  InnerJoin [u.id = o.user_id]
    Scan [users] AS u
    Scan [orders] AS o
```

### Join with Filter Pushdown

```sql
SELECT u.name, o.total
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE u.status = 'active'
```

Plan (after optimization):
```
Project [u.name, o.total]
  InnerJoin [u.id = o.user_id]
    Filter [status = 'active']
      Scan [users] AS u
    Scan [orders] AS o
```

The filter is pushed before the join to reduce the number of users that need to be joined.

## Future Enhancements

Planned improvements to JOIN processing:

- Implement all outer joins natively (not delegated to PyArrow)
- Add sort-merge join for ordered inputs
- Implement join spilling for very large joins
- Cost-based join algorithm selection
- Parallel hash joins
- Bloom filter pushdown for distributed joins
