# Storage Formats

This document primarily applies to the Blob and File stores, such as GCS, S3 and local disk.

## The Rugo File Engine

File reads and writes for Parquet, CSV, and JSONL go through [Rugo](https://rugo.dev), Opteryx's native file engine (also published standalone at `pip install rugo`). Rugo is C++ end to end with no PyArrow, NumPy, or other heavy dependency in the decode path, and it is built around reading as little as possible:

- **Column projection** — only columns the query references are decoded.
- **Row-group pruning** — Parquet footer statistics (min/max) rule out row groups that can't match a predicate before they're touched.
- **Bloom-filter pruning** — where a Parquet file carries bloom filters, equality and `IN` predicates use them to rule out row groups that plain min/max ranges can't.
- **Dictionary-aware skipping** — a dictionary-encoded column's predicate can be evaluated against its dictionary before any per-row data is decoded.

This makes Parquet the format with the most optimization available, since it's the only one of the three with page-level statistics and dictionaries to prune against. CSV and JSONL still benefit from column projection and predicate pushdown, applied via SIMD structural scanning, but they carry no footer metadata to skip whole sections of a file the way Parquet can.

Rugo reads from local disk, HTTP(S) range requests, and Google Cloud Storage behind one interface, and writes all three formats back out — including bloom filters on Parquet output.

See [Rugo — the file engine](https://rugo.dev) for the full architecture.

## Supported Data Files

### Parquet

Parquet is the preferred file format for Opteryx. It's the only format with row-group statistics and bloom filters for Rugo to prune against, so it sees the most optimization and is the best choice for data that's hot or has performance requirements. Parquet with zStandard compression is generally the best balance of IO to read and CPU to decompress, though as with all performance guidance, test against your own data.

### ORC & Feather

Opteryx supports ORC and Feather via Arrow, but neither goes through Rugo's pruning path, so treat them as compatibility formats rather than a performance choice — convert to Parquet if either becomes a hot dataset.

ORC files have limited support on Windows and PyPy environments.

### JSONL

[JSONL](https://jsonlines.org/) and zStandard-compressed JSONL files, read and written natively by Rugo with no explicit schema required — types are inferred from the records, and inconsistent types across a partition will fail the read.

Each partition must have the same columns in the same order in every row of every file.

### CSV & TSV

Comma-separated and tab-delimited files are read and written natively by Rugo, with column projection and predicate pushdown applied the same way as JSONL. CSV lacks the schema and per-row-group metadata Parquet carries, so prefer Parquet for anything beyond casual use or data interchange.

### Avro

Avro formatted files are supported via Arrow, however this requires an additional library to be installed (`pip install avro`) and does not go through Rugo — expect it to be slower than the three natively-supported formats.

## Storage Layout

For Blob/File stores, the path of the data is used as the name of the relation in the query. There are currently two built in data schemas, none (or flat) and Mabel.

### Flat

The flat schema is where the data files are stored in the folder which names the relation, such as:

~~~
customer/
    preferences/
        file_1
        file_2
        file_3
~~~

This would be available to query with a query such as:

~~~sql
SELECT *
  FROM customer.preferences;
~~~

Which would read the three files to return the query.

### Mabel

The Mabel schema is where data is structured in date labelled folders

~~~
customer/
    preferences/
        year_2020/
            month_03/
                day_04/
                    file_1
                    file_2
                    file_3
~~~

The date components of the folder structure are part of the temporal processing, and are not directly referenced as part of the query, instead they form part of the temporal clause (`FOR`)

~~~sql
SELECT *
  FROM customer.preferences
   FOR '2020-03-04'
~~~

This approach enables data to be partitioned by date and pruned using temporal filters.

<!---
# Storage Adapters

## Local

### Disk

## Network

### Google Cloud Storage

### AWS S3 (Minio)
--->