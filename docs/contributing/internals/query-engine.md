# Query Engine

<!--- https://www.cockroachlabs.com/docs/stable/architecture/sql-layer.html --->

> If you are interested in how databases work, I recommend the resources from [The CMU Database Group](https://db.cs.cmu.edu/), and the collection of resources at [Awesome Database Learning](https://github.com/pingcap/awesome-database-learning) and [Awesome Database Development](https://github.com/huachaohuang/awesome-dbdev).

The Opteryx query engine has the following key components and processing queries follows this high-level series of steps:

&emsp;**SQL Rewriter** preprocesses the SQL query to handle special syntax and prepare for parsing.  
&emsp;**Parser & Lexer** receives the user SQL and builds an Abstract Syntax Tree (AST).  
&emsp;**AST Rewriter** transforms the AST to simplify and normalize the structure.  
&emsp;**Logical Planner** creates a logical query plan from the AST.  
&emsp;**Binder** maps contextual information to the plan, resolving identifiers to schemas.  
&emsp;**Optimizer** receives a Query Plan and rewrites it to improve performance.   
&emsp;**Physical Planner** converts the optimized logical plan into a physical execution plan.  
&emsp;**Executor** receives the Query Plan and returns the result dataset.  

## SQL Rewriter

The SQL Rewriter is the first component in the query processing pipeline. It performs preprocessing on the SQL query before it reaches the parser. This includes:

- Handling temporal `FOR` clauses which are Opteryx-specific syntax
- Normalizing SQL syntax variations
- Expanding macros and syntactic sugar
- Preparing the query for standard SQL parsing

The SQL Rewriter allows Opteryx to support custom extensions while still using a standard SQL parser.

## Parser & Lexer

The primary goal of the Parser and Lexer (which in some engines is two separate components) is to interpret the SQL provided by the user. This is generally done in two steps, the first is the break the query into separate tokens (or words) and the second is to understand the meaning of those tokens.

For example for this statement

~~~sql
SELECT SELECT
  FROM FROM
~~~

The Parser and Lexer will understand that we're requesting the field `SELECT` from the relation `FROM`.

Opteryx uses [sqlparser-rs](https://github.com/sqlparser-rs/sqlparser-rs) as its Parser and Lexer, as a Rust library, Opteryx creates Python bindings for sqlparser-rs (derived from [sqloxide](https://github.com/wseaton/sqloxide)). Opteryx does not support all features and functionality provided by this library.

This sqlparser-rs interprets all SQL except for the Temporal `FOR` clause which is handled by the SQL Rewriter.

## AST Rewriter

After the Parser & Lexer creates the AST, the AST Rewriter performs transformations on the tree structure to:

- Normalize and simplify the AST structure
- Apply early optimizations that are easier to perform on the AST than on the query plan
- Resolve certain syntactic constructs into their canonical forms
- Prepare the AST for the logical planning stage

The AST Rewriter operates before the Binder, so it works with unbound identifiers and doesn't require schema information.

## Logical Planner

The Logical Planner converts the AST into a logical query plan - a directed acyclic graph (DAG) that represents the operations needed to answer the query without concern for how they will be physically executed.

The logical plan focuses on *what* needs to be done, not *how* to do it efficiently. This separation allows the optimizer to work on a clean, normalized representation.

## Binder

The Binder's primary goal is to resolve and validate identifiers in the query plan, connecting them to actual schemas and data sources.

Key responsibilities of the Binder include:

- **Identifier Resolution**: Maps column and table references to their actual sources and schemas
- **Schema Binding**: Associates each identifier with its schema information (data type, source relation, etc.)
- **Variable Substitution**: Replaces query variables with their literal values
- **Temporal Information**: Adds temporal information to relations for time-travel queries
- **Validation**: Ensures referenced columns and tables exist and are accessible
- **Ambiguity Detection**: Identifies and reports ambiguous column references

The Binder transforms a logical plan with unresolved identifiers into a bound plan where all references are validated and connected to their schemas. This bound plan is essential for subsequent optimization and execution stages.

For example, when you write `SELECT name FROM users`, the Binder:
1. Resolves `users` to an actual data source
2. Confirms the `name` column exists in the `users` schema  
3. Records the data type and source information for the `name` column
4. Creates schema information that later stages can use

## Physical Planner

The Physical Planner takes the optimized logical plan and converts it into a physical execution plan that can be executed by the query executor.

While the logical plan describes *what* to do, the physical plan describes *how* to do it, including:

- Choosing specific algorithms for operations (e.g., hash join vs. nested loop join)
- Determining data flow and memory management strategies
- Setting up operator nodes for execution
- Preparing for the volcano-style execution model

The physical plan is the final plan that gets executed.

## Operator Execution

The Query Plan is composed of operator nodes which process data as it flows through the plan. Different node types exist for processing actions like Aggregations (`GROUP BY`), Selection (`WHERE`) and Distinct (`DISTINCT`).

Query plans follow a generally accepted order of execution. This does not match the order queries are usually written in, instead it follows this order:

![OPERATOR ORDER](operator-order.svg) 

The planner ensures the processes to be applied to the data reflect this order and creates the most convenient plan to achieve this.

The Query Plan can be seen for a given query using the `EXPLAIN` query.

## Query Optimizer

The goal of the Query Optimizer is to rewrite the Query Plan to a plan which will return result to users faster. This is generally achieved through reducing the data being handled as early in the query as possible (such as projection push-down), reducing the complexity of steps (such as using logical equivelences to make expressions simpler) or combining steps (such as sort and limit into a heap sort).

The current optimizer in Opteryx is immature with very few rules and requires hand-tuning of the input query for the optimizer to achieve best results.

## Query Executor

The goal of the Query Executor is to produce the results for the user. It takes the Plan and executes the steps in the plan.

Opteryx implements a vectorized Volcano model executor. This means that the planner starts at the node closest to the end of the plan (e.g. `LIMIT`) and asks it for a chunk of data. This node asks its preceeding node for a chunk of data, etc etc until it gets to the node which aquires data from source. The data is then processed by each node until it is returned to the `LIMIT` node at the end.

## Performance Features

The following features are build into the query engine to improve performance

- Small chunks are merged together (referred to as 'defragmentation') before activities which operate on the entire chunk-at-a-time (such as selections)
- Projections are pushed to the blob parser, either to prevent parsing of unwanted fields (Parquet), or before passing to the next operation
- A buffer pool is used to maintain an in-memory cache of blobs
- A shared blob cache can be used (e.g. memcached, redis or valkey) to reduce reads to attached or remote storage
- An [LRU-K](https://en.wikipedia.org/wiki/Page_replacement_algorithm#Variants_on_LRU) cache eviction strategy with a fixed eviction budget per query to help ensure effective use of the blob cache
- Aggressive pruning of date partitioned datasets
- SIMD and vectorized execution where available (via [Numpy](https://numpy.org/devdocs/reference/simd/index.html) and [PyArrow](https://arrow.apache.org/docs/format/Columnar.html))
- Projection before `GROUP BY` to reduce data handled by the aggregators
- `null` values are eliminated from filters before they are executed, and added back in after values have been compared, reducing the pointless work of comparing `null` values