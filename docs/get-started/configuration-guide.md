# Configuration Guide

## Configuration File

Configuration values are set a [`opteryx.yaml`](opteryx.yaml) file in the directory the application is run from.

 Key                        | Default     | Description
--------------------------- | ----------: | -----------
`INTERNAL_BATCH_SIZE`       | 500         | Batch size for left-table of a join processes
`MAX_JOIN_SIZE`             | 10000       | Maximum records created in a `CROSS JOIN` frame
`MEMCACHED_SERVER`          | _not set_   | Address of Memcached server, in `IP:PORT` format
`DATASET_PREFIX_MAPPING`    | _not set_   | Data store prefix mapping
`PARTITION_SCHEME`          | _none_      | How the blob/file data is partitioned
`MAX_SIZE_SINGLE_CACHE_ITEM` | 1048576    | The maximum size of an item to store in the cache
`MAX_CACHE_EVICTIONS`       | 25          | The maximum number of evictions from in-memory read cache per query
`PAGE_SIZE`                 | 67108864    | The size to try to make data pages as they are processed
`LOCAL_BUFFER_POOL_SIZE`    | 256         | The size of the in-memory Buffer Pool (blob size)
`DISABLE_HIGH_PRIORITY`     | False       | Disable trying to set the process priority
`PROFILE_LOCATION`          | _not set_   | :octicons-beaker-24: Save information about the query planning and execution to disk

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

The Read Cache currently has one implementation, using [Memcached](https://memcached.org/).

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