# Configuration Guide

## Configuration File

Configuration values are set a `opteryx.yaml` file in the directory the application is run from.

 Key                        | Default     | Description
--------------------------- | ----------: | -----------
`INTERNAL_BATCH_SIZE`       | 500         | Batch size for left-table of a join processes
`MAX_JOIN_SIZE`             | 10000       | Maximum records created in a `CROSS JOIN` frame
`MEMCACHED_SERVER`          | _not set_   | Address of Memcached server, in `IP:PORT` format
`DATASET_PREFIX_MAPPING`    | _not set_   | Data store prefix mapping
`PARTITION_SCHEME`          | _none_      | How the blob/file data is partitioned
`MAX_SIZE_SINGLE_CACHE_ITEM` | 1048576    | The maximum size of an item to store in the cache
`MAX_CACHE_EVICTIONS`       | 50          | The maximum number of evictions from in-memory read cache per query
`PAGE_SIZE`                 | 67108864    | The size to try to make data pages as they are processed
`LOCAL_BUFFER_POOL_SIZE`    | 50          | The size of the in-memory Buffer Pool (blob size)
`MAX_BUFFER_POOL_EVICTIONS` | 20          | The maximum number of evictions from Buffer Pool per query
`DISABLE_HIGH_PRIORITY`     | False       | Disable trying to set the process priority

## Environment Variables

The environment is the preferred location for secrets, although the engine will read `.env` files if [dotenv](https://pypi.org/project/python-dotenv/) has also been installed.

- `MONGO_CONNECTION`
- `MINIO_END_POINT`
- `MINIO_ACCESS_KEY`
- `MINIO_SECRET_KEY`
- `MINIO_SECURE`

## Caching for Blob Stores

### Read Cache

The observed bottleneck for query performance is almost always IO. It is not uncommon for 90% of the execution time is initial load of data - this can vary considerably by storage and query.

The Read Cache currently has two implementations, In Memory Cache and Memcached Cache. When your main storage is local disk, using Memcached as your Read Cache is unlikely to provide significant performance improvement, however  the In Memory Cache may; when using remote storage such as S3 or GCS, Memcached Cache can provide significant improvements. However, as will all optimization, test in your unique set of circumstances before assuming it to be true.

### Buffer Pool

The [Buffer Pool](https://www.ibm.com/docs/en/db2/11.5?topic=databases-buffer-pools) is similar to the Read Cache with two key differences; the Buffer Pool must be held in local memory, Memcache or external system cannot be used and the Buffer Pool is a read through to the Read Cache. That means that reads to the Read Cache check if the items is in the Buffer Pool before checking the Read Cache. This creates a storage heirarchy, where frequently read blobs are likely to be in memory, and never, or infrequently accessed blobs are fetched from storage.

If your Read Cache is in memory, you are unlikely to see considerable benefits from the Buffer Pool.

**In Memory Cache**

Uses the main memory of the host machine to cache pages. This is usually fastest, but most limiting and volatile. This is a good fit for high specification hosts.

The size of the cache is set by the number of pages to hold in memory. No checks are made if the pages actually fit in memory and setting the cache too large, or running on a host where there is high contention for memory where memory is swapped to disk, may result in negative performance.

**Memcached Cache**

Uses a Memcached instance to cache pages. Is a good option when remote reads are slow, for example from GCS or S3.

This is also recommended in an environment where multiple servers, or container instances, may be serving customers. Here, the shared cache allows users to benefit from caching even on their first query if another user's query has populated the cache with the files being read.

## Operating System Support

The regression suite coverage:

OS            | Python 3.8 | Python 3.9 | Python 3.10 | Python 3.11 | PyPy 3.9
------------- | :--------: | :--------: | :---------: | :---------: | :------: 
MacOS (Intel) | Partial    | Partial    | Partial     | None        | None
MacOS (M1)    | None       | None       | None        | None        | None
Windows       | Partial    | Partial    | Partial     | None        | None
Ubuntu (x86)  | Full       | Full       | Full        | Failing     | Failing
Debian (ARM)  | None       | Partial    | None        | None        | None

!!! Note
    - **Full** indicates no tests are excluded from the test suite - coverage statistics are from **Full** tests.
    - **None** indicates there is no automated test for this configuration.
    - **Partial** coverage indicates some tests are excluded.
    - Windows regression suite fails some tests due to issues with Apache Arrow.
    - PyPy regression suite fails due to issues with Apache Arrow.
    - Python 3.11 regression suite fails due to lack of 3.11 support on the test platform.
    - M1 Mac (ARM) is not included in the regression suite but there is known usage on this platform.