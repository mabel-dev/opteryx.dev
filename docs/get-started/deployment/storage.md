# Data Storage

## Connectors

**Built-In Connectors**

Platform             | Connector Name           | Disposition
-------------------- | ------------------------ | ---------------------
Google Cloud Storage | GcpCloudStorageConnector | Blob/File Store
AWS S3               | AwsS3Connector           | Blob/File Store
MinIo                | AwsS3Connector           | Blob/File Store
Google FireStore     | GcpFireStoreConnector    | Document Store
MongoDB              | MongoDbConnector         | Document Store
Local Disk           | DiskConnector            | Blob/File Store

Connectors are registered with the storage engine using the `register_store` method. Multiple prefixes can be added, using different connectors - multiple storage types can be combined into a single query.

~~~python
opteryx.storage.register_store("tests", DiskConnector)
~~~

A more complete example using the `register_store` method to set up a connector to Google Cloud Storage (GCS) and then query data on GCS is below:

~~~python
import opteryx
from opteryx.connectors import GcpCloudStorageConnector

# Tell the storage engine that datasets with the prefix 'your_bucket'
# are to be read using the GcpCloudStorageConnector connector.
# Multiple prefixes can be added and do not need to be the same
# connector.
opteryx.register_store("your_bucket", GcpCloudStorageConnector)

connextion = opteryx.connect()
cursor = connection.cursor()
cursor.execute("SELECT * FROM your_bucket.folder;")

print(cursor.fetchone())
~~~

## Blob/File Stores

### Datasets

Opteryx references datasets using their relative path as the table name. For example in the following folder structure

~~~
/
 ├─ products/
 ├─ customers/
 │   ├─ profiles/
 │   └─ preferences/
 │       ├─ marketing/
 │       └─ site/
 └── purchases/ 
~~~

Would have the following datasets available (assuming leaf folders have data files within them)

- products
- customers.profiles
- customers.preferences.marketing
- customers.preferences.site
- purchases

These are queryable like this:

~~~sql
SELECT *
  FROM customers.profiles
~~~

### Temporal Structures

To enable temporal queries, data must be structured into date hierarchy folders below the dataset folder. Using just the _products_ dataset from the above example, below the _products_ folder must be year, month and day folders like this:

~~~
/
 └─ products/
     └─ year_2022/
         └─ month_05/
             └─ day_01/
~~~

To query the data for today with this structure, you can execute:

~~~sql
SELECT *
  FROM products
~~~

To query just the folder shown in the example (1st May 2022), you can execute:

~~~sql
SELECT *
  FROM products
   FOR '2022-05-01'
~~~

This is the default structure created by [Mabel](https://github.com/mabel-dev/mabel) and within Opteryx this is called Mabel Partitioning.

### File Types

Opteryx is primarily designed for use with [Parquet](https://parquet.apache.org/) to store data, Parquet is fast to process and offers optimizations not available for other formats, however, in some benchmarks [ORC](https://orc.apache.org/) out performs Parquet.

Opteryx supports:

- Parquet formatted files
- CSV formatted files
- [JSONL](https://jsonlines.org/) formatted files
- JSONL formatted files which have been [Zstandard](http://facebook.github.io/zstd/) compressed (`.zstd`)
- ORC formatted files
- Feather (Arrow) formatted files

### File Sizes

Opteryx loads entire files (pages) into memory one at a time, this requires the following to be considered:

- Reading one record from a file loads the entire page. If you regularly only read a few records, prefer smaller pages.
- Reading each page, particularly from Cloud Storage (S3/GCS), incurs a per-read overhead. If you have large datasets, prefer larger pages.

If you are unsure where to start, 64Mb (before compression) is a recommended general-purpose page size.

<!---
## Document Stores
--->