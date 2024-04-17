

Key                    | Description
---------------------- | ----------------------------------------------
blobs_read             | The number of blobs read
bytes_processed        | Sum of the datasets processed by the engine
bytes_read             | Sum of the size of all blobs read
cache_evictions        | Count of blobs removed from cache
cache_hits             | Count of blobs read from cache
cache_misses           | Count of blobs read from source
cache_oversize         | Count of blobs not cached due to size
columns_read           | Count of columns read following projection pushdown
morsel_merges          | Count of internal defragmentations
morsel_splits          | Count of internal forced fragmentation
rows_read              | Count of rows read following selection pushdown
rows_seen              | Count of all rows seen by the reader
unreadable_data_blobs  | Count of blobs which failed decoding
time_aggregating       | Seconds taken aggregating
time_cross_join_unnest | Seconds taken performing CROSS JOIN UNNEST
time_defragmenting     | Seconds taken performing internal data defragmentation
time_distincting       | Seconds taken performing DISTINCT
time_evaluate_dataset  | Seconds taken creating function defined datasets
time_evaluating        | Seconds taken in executing functions and expressions
time_exiting           | Seconds taken preparing the final record set
time_grouping          | Seconds taken performing GROUP BY
time_inner_join        | Seconds taken performing INNER JOIN
time_limiting          | Seconds taken performing LIMIT
time_outer_join        | Seconds taken performing OUTER JOINs
time_planning          | Seconds taken in query planning
time_ordering          | Seconds taken to ordering results
time_reading_blobs     | Seconds taken reading blobs
time_waiting_sql       | Seconds waiting for remote SQL server
