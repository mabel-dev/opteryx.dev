# Configuration Guide

## Configuration File

Configuration values are set a [`opteryx.yaml`](opteryx.yaml) file in the directory the application is run from.

These items can also be set via Environment Variables.

`DISABLE_OPTIMIZER`=False
**DANGEROUS** This will cause most queries to fail.

`OPTERYX_DEBUG`=False
**DANGEROUS** Diagnostic and debug mode - generates a lot of log entries.

`MAX_CACHE_EVICTIONS_PER_QUERY`=64
Maximum number of buffer pool evictions by a single query.

`MAX_CACHEABLE_ITEM_SIZE`=2097152
Maximum size for items saved to the remote buffer.

`MAX_CONSECUTIVE_CACHE_FAILURES`=10
Maximum number of consecutive cache failures before disabling cache usage.

`MAX_LOCAL_BUFFER_CAPACITY`=0.2
Local buffer pool size in either bytes or fraction of system memory.

`MAX_READ_BUFFER_CAPACITY`=0.1
Read buffer pool size in either bytes or fraction of system memory.

`CONCURRENT_READS`=4
Number of read workers per data source.


## Environment Variables

The environment is the preferred location for secrets, although the engine will read `.env` files if [dotenv](https://pypi.org/project/python-dotenv/) has also been installed.

- `MONGO_CONNECTION`
- `MINIO_END_POINT`
- `MINIO_ACCESS_KEY`
- `MINIO_SECRET_KEY`
- `MINIO_SECURE`
- `VALKEY_CONNECTION`
- `REDIS_CONNECTION`
- `MEMCACHED_SERVER`

## Caching for Blob Stores

### Read Cache

The observed bottleneck for query performance is almost always IO. It is not uncommon for 90% of the execution time is initial load of data - this can vary considerably by storage and query.

The Read Cache currently can make use of [Memcached](https://memcached.org/), [Redis](https://redis.io/), or [Valkey](https://valkey.io/).

When your main storage is local disk, using a Read Cache is unlikely to provide significant performance improvement. However, when using remote storage, such as S3 or GCS, Read Cache can provide significant improvements. 

As will all optimization recommendations, test in your unique set of circumstances before assuming this to always be true.

Read Cache is only used for Blob stores, and is not used for Document stores.

### Buffer Pool

The [Buffer Pool](https://www.ibm.com/docs/en/db2/11.5?topic=databases-buffer-pools) is similar to the Read Cache with two key differences; 

- The Buffer Pool is held in local memory.
- The Buffer Pool is a read-through for the Read Cache.

That means that reads try to locate the fastest access to a blob in this order:

1) Check the Buffer Pool (in memory)   
1) Check the Read Cache (fast KV store)   
1) Read from storage   

The Buffer Pool and Read Cache creates a storage heirarchy, where blobs more likely to be read (based on what has been read in the past) are more likely to be in a location which is faster to read.

Buffer Pools are local to the asset serving the requests, in a serverless environment this asset may only serve one or two requests before terminating. If your environment is configured like this, have a small Buffer Pool and a large Read Cache. If assets serve 10s or more requests before terminating, have a large Buffer Cache.

As will all optimization recommendations, test in your unique set of circumstances before assuming this to always be true.

Buffer Pool is only used for Blob stores, and is not used for Document stores.