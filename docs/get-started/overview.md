# Opteryx Overview

Opteryx revolutionizes your data landscape by serving as a seamless federator for diverse data sources. With Opteryx, you're not just querying a database — you're operating a data control room. Unify your data sources, viewing across Postgres databases, Parquet files, and even more specialized storage solutions, all through a single pane of glass. Opteryx empowers you to transcend data silos, synchronize insights, and command your entire data ecosystem with unparalleled speed and reliability.

Opteryx is not intended to replace databases like SQL Server, MySQL, or Postgres. Instead, it's designed to allow querying of data sources as part of a data analytics process. By bridging the gap between various data storages, Opteryx enhances your analytics pipeline, enabling you to focus on drawing actionable insights rather than wrestling with data access and compatibility issues.

## Benefits

- **Querying large datasets across multiple platforms** - Opteryx allows you to query multiple query engines and storage formats in a single query. This makes it useful for querying large datasets that are stored in different formats or locations.
- **Analyzing data in real-time** - Opteryx is designed to run in serverless environments where servers can be created and destroyed regularly or even between every query. This makes it well-suited for real-time data analytics, where you need to analyze data quickly and efficiently.
- **Cost-effective data analytics** - Opteryx is consumption-based billing friendly, making it great for low-volume usage or situations where you have many environments. This makes it a cost-effective alternative to traditional database deployment.
- **Replaying decisions against past data** - Opteryx allows you to query data at a point in time in the past to replay decision algorithms against facts as they were known in the past. This makes it useful for situations where you need to analyze data retroactively.
- **Integration with Python** - Opteryx is Python native and can be easily integrated into Python code, including Jupyter Notebooks. This makes it useful for data analysts and data scientists who use Python as their primary programming language.

## Uses for Opteryx

1. **Data Analytics** - Opteryx is designed for querying large data sets and can support complex analytics use cases. Its time travel feature allows you to query data as it existed in the past, making it well-suited for replaying decision algorithms against past facts.
2. **Cloud-Native Data Processing** - Opteryx is designed to run in low-cost, serverless environments like Google Cloud Run. This makes it a great choice for organizations that want to minimize infrastructure costs while still being able to query large datasets.
3. **Data Warehousing** - Opteryx allows you to query data directly in the systems where it is stored, eliminating the need to duplicate data into a common store for analytics. This can save you the cost and effort of maintaining duplicates, and is a good option for data warehousing use cases.
4. **Python-Based Data Processing** - Opteryx is written in Python and can be easily integrated into Python code, including Jupyter Notebooks. This makes it a good choice for data processing and analytics workflows that are already written in Python.
5. **Consolidating Backend Systems** - Opteryx creates a common SQL-layer over multiple data platforms, allowing you to upgrade, migrate, or consolidate backend systems without changing any Opteryx code. This makes it a good choice for organizations that want to streamline their data infrastructure.

Opteryx supports accessing multiple database backends, each with their own authentication and access controls. This capability allows Opteryx to serve as a unified access tool for external databases, simplifying challenges such as shifting data schemas and inconsistent API behaviors.

## Why Opteryx rather than 'X'

'X' is great, and for your use case it may be a better option. Opteryx isn't for all users and all use cases - and we're okay with that.

SQLite and DuckDB are great choices if you're looking for an embedded database engine. We like them so much we have SQLite and DuckDB integration tests in our CI test-suite.

Postgres and MySQL are great choices if you're looking for a server/client style database engine. They are tried and tested and solve this problem very well. We like them so much we have Postgres and MySQL integration tests in our CI test-suite.

Opteryx allows you to have the right database or datastore for the job, and combine them all together. Want to combine Customer database in Postgres, logs in JSONL and monthly sales reports in Parquet; do it - you have the freedom to choose the right tool for a specific task and still be able to join and search across all of them with Opteryx.

## Cloud Native

Opteryx is a SQL query engine designed to query large datasets in low-cost serverless environments. While it can respond to a subset of SQL statements like a database, Opteryx is not a database itself and does not support activities that insert, update, or delete data.

Opteryx doesn't rely on any internal state between queries. This means it can run in serverless environments where servers can be created and destroyed regularly, or even between every query. While the engine does use caching to improve performance, it doesn't maintain any persistent state, making it an ideal solution for cloud-based analytics. (_the engine does use caching to improve performance_)
