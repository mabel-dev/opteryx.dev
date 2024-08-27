# Optimization Strategies

Strategy                                                      | Type         | Status
:------------------------------------------------------------ | :----------- | :----------
[Split Conjunctive Predicates](#split-conjunctive-predicates) | Heuristic    | Implemented
[Predicate Pushdown](#predicate-pushdown)                     | Schema-Aware | Implemented
[Projection Pushdown](#projection-pushdown)                   | Schema-Aware | Implemented
[Constant Folding](#constant-folding)                         | Heuristic    | Implemented
[Predicate Rewriter](#predicate-rewriter)                     | Heuristic    | Implemented
[Morsel Defragmentation](#morsel-defragmentation)             | Heuristic    | Attempted
[Aggregate Pushdown](#aggregate-pushdown)                     | Schema-Aware | Considered
[IN (literal) to JOIN](#in-literal-to-join)                   | Schema-Aware | Considered
[Use Heap Sort](#use-heap-sort)                               | Heuristic    | Implemented
[Use pass-thru DISTINCT](#use-pass-thru-distinct)             | Heuristic    | Considered
[Limit Pushdown](#limit-pushdown)                             | Heuristic    | Considered
[IN (subquery) to JOIN](#in-subquery-to-join)                 | Schema-Aware | Considered
[CTE rewrite](#cte-rewrite)                                   | Heuristic    | Considered
[Subquery flattening](#subquery-flattening)                   | Schema-Aware | Considered
[JOIN ordering](#join-ordering)                               | Cost-Based   | Considered
[Predicate Ordering](#join-ordering)                          | Cost-Based   | Attempted
[Predicate Flattening](#predicate-flattening)                 | Schema-Aware | Attempted
[Predicate Compaction](#predicate-compaction)                 | Schema-Aware | Designed
[Correlated Predicates](#correlated-predicates)               | Schema-Aware | Considered
[Predicate Elimination](#predicate-elimination)               | Heuristic    | Implemented
[JOIN Elimination](#join-elimination)                         | Schema-Aware | Considered


### Split Conjunctive Predicates

**status** implemented  
**goal** prepare  
**description** Split ANDed (conjunctions) predicates into separate steps in the query plan

This optimization step is preparing for later optimizations, it splits filter conditions at ANDs to try to create smaller, simpler individual conditions (predicates). These predicates are then handled in subsequent strategies, for example [Predicate Pushdown](#predicate-pushdown) and [Predicate Ordering](#predicate-ordering).

To split conditions, no information is needed about the schema or about costs, this strategy is executed before the binder.

### Predicate Pushdown

**status** implemented  
**goal** reduce rows  
**description** Move filters earlier in the query plan 

This optimization aims to reduce the number of records as quickly as possible running through the execution engine by executing filters as soon as possible. This can include pushing filters into the actual data read (e.g. for SQL and parquet), straight after reading, or into JOIN conditions.

This optimization needs to know which relation identifiers are from to be able to push toward the correct scan/JOIN, this strategy is run after the binder.

**improvements**
- Push complex predicates (e.g. ORed) to SQL sources
- Where filters can be inferred from statistics and JOINs, create and push these

### Projection Pushdown

**status** implemented  
**goal** reduce columns  
**description** Trim unwanted columns at read 

This optimization aims to increase the number of records per morsel by removing unwanted columns from relations. This is generally done during the actual read, or straight after reading (e.g. for JSONL and CSV).

This optimization needs to know which relation identifiers are from to be able to push toward the correct scan, this strategy is run after the binder.

**improvements**
- Push common functions and transforms to SQL sources

### Constant Folding

**status** implemented  
**goal** reduce calculations  
**description** Pre-evaluate expressions  

This optimization aims to reduce the work done to evaluate expressions by pre-evaluating expressions which don't rely on data from relations. This includes fixed constants (e.g. literals, `PI()`), variable constants (`current_time`) and variables.

This optimization requires variables to be resolved so is run after the binder.

**improvements**
- filters which evaluate to FALSE (when ANDed) should prune the scan(s) below it
- filters which evaluate to TRUE (when ORed) should remove the entire filter

### Morsel Defragmentation

**status** designed  
**goal** reduce morsels  
**description** Combine small morsels together

This optimization aims to reduce the number of times the execution engine executes each step by combining small morsels together. Morsels are up to 64Mb in size, but as filters and other operations are run to eliminate records, the engine may be processing 100 morsels of 0.5Mb each. By combining, we have fewer function calls and steps which benefit from seeing as much data as possible (e.g. JOINs) execute faster.

This optimization does not require any information about schemas, but operates on a nearly finished plan so is run after the binder.

**notes**
- This should be implemented to run after filters (including when pushed into readers)

### Predicate Rewriter

**status** implemented  
**goal** faster implementations  
**description** replace predicates with faster versions

Some predicates can support complex filtering but are used to perform trivial filtering, where a complex predicate is used to perform a trivial check, replace the check with an simpler function call which is faster.

- demorgans laws
- negative filter reduction
- LIKE to STARTS_WITH, ENDS_WITH, SEARCH
- Single element IN to equals
- No wildcard LIKE to equals

**improvements**
Identify other functions which have faster versions.

### Aggregate Pushdown

into SQL sources

### IN (literal) to JOIN

### Use Heap Sort

**status** implemented  
**goal** reduce memory usage & sort complexity   
**description** incremental sort  

When performing an ORDER BY and a LIMIT, use a heap sort in batches to avoid loading the entire dataset into memory.

This works by acquiring tuples to sort in batches, sorting the batch, keeping the number of tuples to satisfy the limit and then fetching the next batch.

### Use pass-thru LIMIT

When dealing with large number of records, rather than load them all into memory to to the distinct, use a pass-thru limit approach

### Limit Pushdown

Push limits to the SQL reader

### IN (subquery) to JOIN

### CTE rewrite

### Subquery flattening

### JOIN ordering

### Predicate Ordering

### Predicate Flattening

### Predicate Elimination

Where logical expressions contain boolean literals, these can be removed sometimes resulting in the entire expression being removed. E.g. `1 = 1 OR name = 'Alice'` can be completely removed avoiding any further handling of the check against the name column.

### Correlated Predicates

If a column participating in a JOIN has a known value range, push down corresponding filters to both sides of the JOIN, reducing the size of the datasets that need to be joined.

### JOIN Elimination

Value range information for fields participating in JOINs could lead to the identification of redundant JOINs. Where the value ranges of the joining columns do not overlap, the JOIN will not produce any results, the entire sub-tree below the JOIN could be pruned.