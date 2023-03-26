# Writing a SQL Engine

## Motivation

No-one in their right mind would write a SQL Engine if they didn't need to. There are a lot of options in the space of providing SQL query access to distributed data - with a few players prominent in the market like DuckDB and SQLite.

We had a problem where we wanted a SQL interface to our data, but none of the existing tools were a good fit for our situation. We could change ourselves to fit an existing toolset, but wanted to explore other options before committing to vendor-defined design.

## Prior Attempts

The data store we're working with was designed to be transctional (read a row of data, process it, save the result, repeat). We use JSON lines files, which for this use case we were unable to find anything better in the sweet spot of human and machine readable, and performance to read and write.

With this as the datastore, our first attempt at a SQL engine was also row-based, following what is known as the Volcano Model. This aligned well with the tools that we had written to process the data so most of the effort was with translating the SQL syntax to filters that the existing tools could understand. Functionality like `GROUP BY` was added to make it feel more like a database and less like a log-viewer.

This provided an acceptable level of functionality for single-table queries (the pre-existing tools only ever read from one table and write to one table) and the engine was implemented into user-facing systems.

As data grew, we started to hit problems. Reading tens of million of rows, constraints outside the control of the system meant that jobs that ran for longer than 180 seconds were terminated. This generally meant that queries with more than about 30 million records (or far fewer records but with calculations) timed out. A lot of queries were still able to be run as not everything hit these thresholds, but it couldn't be used for large data analysis.

## Redesign

The decision to write the SQL Engine as a new library separate from the existing data handling library was made early it freed us from some of the implementation decisions of the existing solution.

**SQL Statement Parsing**

Writing a robust SQL parser is hard, there are a considerable number of rules and exceptions that need to be followed. We chose SqlOxide to parse the statements to an AST. There is still a lot of work to convert the AST to a query plan - but the AST removes ambiguity, something like `SELECT SELECT FROM FROM FROM` would be difficult to parse with a regex-based parser.

**Query Planning**

The previous SQL Engine had a fixed execution plan, this meant that no matter what your query was it followed the same steps, with some steps doing nothing. This was simplier to write, but will have affected performance. Opteryx creates a query plan, the initial version doesn't optimize this plan by doing things like running selections and projections early, but it does only add steps to the plan that are required. 

**Internal Data Respresentation**

Leveraging Apache Arrow to help improve performance. Parquet was assessed for the transactional use case but the optimized JSONL implementation in Mabel consistently outperformed Parquet. However, reassessing performance for a SQL engine, Parquet outperforms JSONL. 

**Data Storage**

We've since moved all of our data from JSONL to Parquet, whilst this is a performance hit to the row-by-row processing, the benefits when performing SQL queries of the data are significant. This not only includes read performance (especicially when we can push filters), but having an enforced schema helps prevent some issues with data ()

