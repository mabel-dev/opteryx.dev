# Deployment Guide

## Requirements

### Host Specifications

**Minimum**: 1 CPU, 1 Gb RAM (Intel/x86 CPU)   
**Recommended**: 4 CPUs, 8 Gb RAM (Intel/x86 CPU)

Opteryx balances memory consumption with performance, however, being able to process large datasets will require larger memory specifications compared to what is needed to process smaller datasets. The reference implementation of Opteryx regularly processes 100Gb of data in a container with 4 CPUs and 8Gb of memory allocated.

!!! Note
    This is a general recommendation and is a good place to start, your environment and specific problem may require, or perform significantly better, with a different configuration.

!!! Warning
    Non x86 environments, such as Raspberry Pi or the M series of Mac CPUs, may require additional set up steps.

### Python Environment

**Recommended Version**: 3.10

Opteryx supports Python versions 3.8, 3.9 and 3.10.

Opteryx has builds for Python 3.8, 3.9 and 3.10 on 64-bit (x86) versions of Windows, MacOS and Linux. The full regression suite is run on Ubuntu (Ubuntu 20.04) for Python version 3.8, 3.9 and 3.10.

Opteryx is primarily developed on workstations running Python 3.10 (Debian, MacOS) and is known to be deployed in production environments running Python 3.9 (Debian)

### Jupyter Notebooks

Opteryx can run in Jupyter Notebooks to access data locally or, if configured, remotely on systems like GCS and S3. This approach will result in raw data being moved from the data platform (GCS or S3) to the host running Jupyter to be processed. This is most practical when the connection to the data platform is fast - such as running Vertex AI Notebooks on GCP, or querying local files.

### Docker & Kubernetes

There is no Docker image for Opteryx, this is because Opteryx is an embedded Python library. However, system built using Opteryx can be deployed via Docker or Kubernetes.

### Google Cloud

**Cloud Run**

Opteryx is well-suited for running data manipulation tasks in Cloud Run as this was the target platform for the initial development.

Running in the Generation 2 container environment is likely to result in faster query processing, but has a slower start-up time. Opteryx runs in Generation 1 container, taking approximately 10% longer to execute queries.

!!! Note  
    Opteryx contains no specific optimiations to make use of multiple CPUs, although multiple CPUs may be beneficial to allow higher memory allocations and libraries Opteryx is built on may use multiple CPUs.

## Data Storage

### Connectors

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