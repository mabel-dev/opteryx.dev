# Optimization Strategies

Strategy                                                      | Type         | Status
:------------------------------------------------------------ | :----------- | :----------
[Split Conjunctive Predicates](#split-conjunctive-predicates) | Heuristic    | Implemented
[Predicate Pushdown](#predicate-pushdown)                     | Schema-Aware | Implemented
[Projection Pushdown](#projection-pushdown)                   | Schema-Aware | Implemented
[Constant Folding](#constant-folding)                         | Heuristic    | Implemented
[Predicate Rewriter](#predicate-rewriter)                     | Heuristic    | Implemented
[Aggregate Pushdown](#aggregate-pushdown)                     | Schema-Aware | Considered
[IN (literal) to JOIN](#in-literal-to-join)                   | Schema-Aware | Considered
[Use Heap Sort](#use-heap-sort)                               | Heuristic    | Implemented
[Use pass-thru DISTINCT](#use-pass-thru-distinct)             | Heuristic    | Implemented
[Limit Pushdown](#limit-pushdown)                             | Heuristic    | Implemented
[Distinct Pushdown](#distinct-pushdown)                       | Heuristic    | Implemented
[IN (subquery) to JOIN](#in-subquery-to-join)                 | Schema-Aware | Considered
[CTE rewrite](#cte-rewrite)                                   | Heuristic    | Considered
[Subquery flattening](#subquery-flattening)                   | Schema-Aware | `Considered`
[JOIN ordering](#join-ordering)                               | Cost-Based   | Considered
[Predicate Ordering](#predicate-ordering)                     | Cost-Based   | Partial
[Predicate Compaction](#predicate-compaction)                 | Schema-Aware | Designed
[Correlated Predicates](#correlated-predicates)               | Schema-Aware | Implemented
[Predicate Elimination](#predicate-elimination)               | Heuristic    | Implemented
[JOIN Elimination](#join-elimination)                         | Schema-Aware | Considered


### Split Conjunctive Predicates

**status** implemented  
**goal** prepare  
**description** Split `AND`ed (conjunctions) predicates into separate steps in the query plan

_SplitConjunctivePredicatesStrategy_

This optimization step is preparing for later optimizations, it splits filter conditions at `AND`s to try to create smaller, simpler individual conditions (predicates). These predicates are then handled in subsequent strategies, for example [Predicate Pushdown](#predicate-pushdown) and [Predicate Ordering](#predicate-ordering).

To split conditions, no information is needed about the schema or about costs, this strategy is executed before the binder.

### Predicate Pushdown

**status** implemented  
**goal** reduce rows  
**description** Move filters earlier in the query plan 

_PredicatePushdownStrategy_

This optimization aims to reduce the number of records as quickly as possible running through the execution engine by executing filters as soon as possible. This can include pushing filters into the actual data read (e.g. for SQL and parquet), straight after reading, or into `JOIN` conditions.

This optimization needs to know which relation identifiers are from to be able to push toward the correct scan/`JOIN`, this strategy is run after the binder.

**improvements**
- Push complex predicates (e.g. `OR`ed) to SQL sources
- Where filters can be inferred from statistics and `JOIN`s, create and push these

### Projection Pushdown

**status** implemented  
**goal** reduce columns  
**description** Trim unwanted columns at read 

_ProjectionPushdownStrategy_

This optimization aims to increase the number of records per morsel by removing unwanted columns from relations. This is generally done during the actual read, or straight after reading (e.g. for JSONL and CSV).

This optimization needs to know which relation identifiers are from to be able to push toward the correct scan, this strategy is run after the binder.

**improvements**
- Push common functions and transforms to SQL sources

### Constant Folding

**status** implemented  
**goal** reduce calculations  
**description** Pre-evaluate expressions  

_ConstantFoldingStrategy_

This optimization aims to reduce the work done to evaluate expressions by pre-evaluating expressions which don't rely on data from relations. This includes fixed constants (e.g. literals, `PI()`), variable constants (`current_time`) and variables.

This optimization requires variables to be resolved so is run after the binder.

**improvements**
- filters which evaluate to `false` (when `AND`ed) should prune the scan(s) below it

### Predicate Rewriter

**status** implemented  
**goal** faster implementations  
**description** replace predicates with faster versions

_BooleanSimplificationStrategy_  
_PredicateRewriteStrategy_  

Some predicates can support complex filtering but are used to perform trivial filtering, where a complex predicate is used to perform a trivial check, replace the check with an simpler function call which is faster.

- demorgans laws
- negative filter reduction
- `LIKE` to `STARTS_WITH`, `ENDS_WITH`, `SEARCH`/`INSTR`
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

_OperatorFusionStrategy_

When performing an `ORDER BY` and a `LIMIT`, use a heap sort in batches to avoid loading the entire dataset into memory.

This works by acquiring tuples to sort in batches, sorting the batch, keeping the number of tuples to satisfy the limit and then fetching the next batch.

### Use pass-thru DISTINCT

**status** implemented  
**goal** reduce memory usage
**description** incremental distinct  

When dealing with large number of records, rather than load them all into memory to to the distinct, use a pass-thru limit approach by maintaining a HashSet of the seen values and checking each morsel against the HashSet.

### Limit Pushdown

**status** implemented  
**goal** reduce data movement
**description** incremental sort  

_LimitPushdownStrategy_

Push limits to the SQL reader to reduce the amount of data trnasferred and processed by the engine.

**improvements**
Push limit to other readers.

### Distinct Pushdown

**status** implemented  
**goal** reduce size of internal table creation   

_DistinctPushdownStrategy_

Push `DISTINCT` clause into `CROSS JOIN UNNEST`.

### IN (subquery) to JOIN

### CTE rewrite

### Subquery flattening

### JOIN ordering

### Predicate Ordering

**status** partial
**goal** fastest order to execute filters

_PredicateOrderingStrategy_

Use execution statistics to determine a 'good' order to execute filters in. This is currently implemented to use the time to execute filters based on the datatype only (e.g. comparing `INTEGER` values is faster than `VARCHAR` values) and does not account for the selectivity of the filtering.

### Predicate Elimination

Where logical expressions contain boolean literals, these can be removed sometimes resulting in the entire expression being removed. E.g. `1 = 1 OR name = 'Alice'` can be completely removed avoiding any further handling of the check against the name column.

### Correlated Predicates

**status** implemented  
**goal** reduce records processed in joins

_CorrelatedFiltersStrategy_

If a column participating in a `JOIN` has a known value range, push down corresponding filters to both sides of the `JOIN`, reducing the size of the datasets that need to be joined.

### JOIN Elimination

Value range information for fields participating in `JOIN`s could lead to the identification of redundant `JOIN`s. Where the value ranges of the joining columns do not overlap, the `JOIN` will not produce any results, the entire sub-tree below the `JOIN `could be pruned.