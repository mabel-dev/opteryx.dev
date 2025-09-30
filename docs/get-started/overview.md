# Get Started with Opteryx

Opteryx is a cloud-native SQL query engine that lets you query data across multiple systems without needing to centralize or duplicate it. Whether your data lives in Postgres, Parquet, JSONL, or somewhere else, Opteryx gives you a unified SQL interface — so you can focus on **analytics, not integration**.

It’s not a replacement for databases like Postgres or MySQL. Instead, Opteryx acts as a **federated query layer**, ideal for analytics workflows where data lives in many places and fast answers matter more than transactional support.

## Why Opteryx?

- **Query across formats and systems** Combine Parquet, Postgres, DuckDB, JSONL, and more — all in a single query. No ETL required.
- **Designed for the cloud** Opteryx is stateless and fast to start, making it perfect for serverless platforms like Google Cloud Run. No persistent state, no storage to manage.
- **Cost-efficient by design** Built for consumption-based infrastructure. Start fast, scale down to zero, pay only when used.
- **Python-native** Use directly from Python or Jupyter notebooks. It speaks PEP 249 (DB API v2.0), so it plugs into your data science stack with minimal friction.
- **Time-travel support**
Query your data as it was at a specific point in time — ideal for replaying decisions or debugging past behavior.

## What Can You Use It For?

- **Analytics over distributed data** Run joins across logs in JSONL, user tables in Postgres, and reports in Parquet — without moving anything.
- **Data warehousing without the warehouse** Skip the duplication step. Query data where it already lives.
- **Serverless data apps** Use Opteryx in cloud functions or ephemeral containers — no need for warm state or persistent infrastructure.
- **Decision auditing and retrospectives** Re-run your logic against how the data looked at any given point in time.
- **Python-based pipelines**
Drop Opteryx into your existing Python workflows. It behaves like a normal SQL engine, with native table and result access.

## When Not to Use Opteryx

Opteryx isn’t a general-purpose OLTP database. It doesn’t support inserts, updates, or deletes, and it doesn’t try to replace your existing databases.

If you need:  
- A full SQL engine with ACID guarantees → Use Postgres or MySQL  
- An embedded analytics database → Use DuckDB or SQLite  

We love those tools too — you can even query these using Opteryx.

Opteryx is for when you need to query across those tools, want to query ad hoc data in files.

## Why Opteryx rather than 'X'

'X' is great, and for your use case it may be a better option. Opteryx isn't for all users and all use cases - and we're okay with that.

Want to query:  
- Customers in Postgres   
- Web logs in JSONL  
- Sales reports in Excel  

…all in one go?
Opteryx handles that, with SQL you already know.

## Architecture Fit

Opteryx is stateless between queries. That means:  
- No session management  
- No background jobs   
- No persistent config  

Just fast, predictable, read-only querying. It caches what it can, but if the container goes away, nothing breaks. Perfect for **serverless**, **batch**, or **ephemeral compute environments**.

⸻

Want to run a query now? Check out the [Quickstart Guide](quickstart/)  
Want to wire it into Python? See the [Python Integration Docs](python-client/)