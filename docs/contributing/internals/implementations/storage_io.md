# Storage IO


**Capabilities**
- async
- cachable

Some implemented as serial only, some implemented with async.

Async uses a read buffer to throttle the reads and prevent complex processing not consuming reads fast enough from blowing memory limits.

## Caching

Up to two layers of cache:
- Buffer Pool
- Remote Cache

### Buffer Pool

One of the few process-scoped resources (i.e. is shared across connections and queries). This is an in memory cache of files and blobs. This is implemented on top of a memory pool.

## Buffering

> Note that Buffer Pool is covered in Caching

Buffering is used to enable prefetching of files of blobs. This is most useful with remote filestores (e.g. GCS) which are generally quite slow to retrieve data from. Buffering allows us to use multiple workers to fetch data, and populate buffers as a strategy to ensure data is being fed into the system at similar rate to the processing of this data.

We use a memory pool here to limit the amount of data waiting and prevent the readers from exhausting system resources, we also use the memory pool to remove the need to transfer large quantities of data between threads, we pass the pool reference.

## Monitoring

**stalls**
The number of items a process has had to wait before it could continue. 

write to buffer stalls indicates the workers reading from storage are having to wait before they can add their payload to the read buffers.

read from buffer stalls indicate the processing of the data is having to wait for more data to be added to the buffers.

## Terminology

**stall** when work is still to be done but a process is waiting on other part of the system.