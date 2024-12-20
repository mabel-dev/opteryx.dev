# Reducing GCS ReadTimes

When observing performance statistics for Opteryx one thing is clear, IO is the single largest contributor to query time; a simple query over a gigabytes of data can take 10s of seconds, with IO being over 90% of the execution time.

Our exemplar user runs Opteryx on the Google Cloud Platform with the bulk of their data in buckets on GCS. This is a great low-cost platform and it holds terabytes of data which Opteryx is used to query.

Seeing GCS access times were a significant part of the execution time, Opteryx implemented the ability to use Memcache, Redis or Valkey as a cache, this is great and it brings the performance of reading blobs not far away from local spinning disk speeds.

But there's two key things this doesn't solve:
1) Fresh or infrequently access blobs.
2) Getting the list of blobs to read.

Slow to access infrequently accessed blobs may not sound like a huge issue, except about 20% of queries are looking at historical data. Data from the last few days is cached, but much further back and it's not. They could size Memcache to hold more data, but that's not cost effective.

