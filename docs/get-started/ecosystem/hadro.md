# Hadro

An implementation of an LSM Tree system.

The Memtable records data as it is written to the system. Each file

Hadro Files are based on the concepts from [SSTables](https://opensource.docs.scylladb.com/stable/architecture/sstable/sstable3/sstables-3-data-file-format.html) but opinionated for blob storage. This puts the parts of the SSTable into a single file to reduce chattiness of requests to remote storage.

Files are written with a [Lamport Timestamp](https://en.wikipedia.org/wiki/Lamport_timestamp) and a clock timestamp to determine order. 

Compaction is used to garbage collect and consolidate records to simplify read activities.