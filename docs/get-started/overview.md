# Opteryx Overview

Opteryx is a SQL query engine designed to query large datasets in low-cost serverless environments. While it can respond to a subset of SQL statements like a database, Opteryx is not a database itself and does not support activities that insert, update, or delete data.

Opteryx is not intended to replace databases like SQL Server, MySQL, or Postgres. Instead, it's designed to allow querying of data sources as part of a data analytics process.

Opteryx doesn't rely on any internal state between queries. This means it can run in serverless environments where servers can be created and destroyed regularly, or even between every query. While the engine does use caching to improve performance, it doesn't maintain any persistent state, making it an ideal solution for cloud-based analytics. (_the engine does use caching to improve performance_)

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

## Why Opteryx rather than 'X'

'X' is great, and for your use case it may be a better option. Opteryx isn't for all users and all use cases - and we're okay with that.

SQLite and DuckDB are great choices if you're looking for an embedded database engine. We like them so much we have SQLite and DuckDB integration tests in our CI test-suite.

Postgres and MySQL are great choices if you're looking for a server/client style database engine. They are tried and tested and solve this problem very well. We like them so much we have Postgres and MySQL integration tests in our CI test-suite.
