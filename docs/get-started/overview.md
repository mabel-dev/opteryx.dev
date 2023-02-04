# Opteryx Overview

Opteryx is a SQL query engine to query large data sets designed to run in low-cost serverless environments.

Opteryx is not a database, it does understand and respond to a subset of SQL statements like a database, but it does not support any activities which insert, update or delete data. It is not a replacement for databases like SQL Server, MySQL or Postgres, it is designed to allow querying of data sources as part of an data analytics process.

Opteryx doesn't rely on any internal state between queries, meaning it can run in serverless environments where servers can be created and destroyed regularly or even between every query. (_the engine does use caching to improve performance_)

## Use Cases

Where you need to query data across different data platforms but don't want the cost or effort to move this data to a common platform.

Great for use in cost-optimized environments, where a traditional data solution like Hadoop is out of reach.

Querying ad hoc data stores for third-party systems, such as querying logs output to storage.

Where you have many different environments, and each would require their own database to query static data.

Where you occassionally query data, and don't want the effort of loading into a database or the cost of maintaining a database for infrequent use.

Where time to respond to queries is not time sensitive.