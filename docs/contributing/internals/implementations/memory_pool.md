# Memory Pool

The memory pool is a block of contiguous memory that we manage the allocation of.

**Buffer Pool**

Where we store blobs and files read from storage in memory for faster recall.

**Read Buffers**

When we use concurrent readers to fetch data, they use the read buffers to hold the data until it's ready for processing.