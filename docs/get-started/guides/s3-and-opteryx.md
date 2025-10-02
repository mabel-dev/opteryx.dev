---
title: Query AWS S3 with Opteryx - SQL Engine for S3 Data
description: Query Parquet, CSV, JSONL files in AWS S3 directly with Opteryx SQL engine. No ETL required - run federated queries across S3 and other data sources.
---

# Querying AWS S3 with Opteryx

This guide demonstrates how to query data stored in Amazon S3 buckets using Opteryx. Opteryx can directly read various file formats (Parquet, CSV, JSONL, ORC, Avro) from S3 without needing to download them first.

## Installation

Install Opteryx with S3 support.

~~~console
$ pip install opteryx
~~~

## Authentication

Opteryx uses standard AWS credential mechanisms. Ensure you have AWS credentials configured through one of:

- Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
- AWS credentials file (`~/.aws/credentials`)
- IAM role (when running on AWS infrastructure)

## Querying S3 Files

You can query files in S3 by using the S3 URI in your SQL query.

### Query a Single File

~~~python
import opteryx

# Query a Parquet file in S3
result = opteryx.query("""
    SELECT * 
    FROM 's3://my-bucket/data/planets.parquet'
    LIMIT 10
""")

# Display results
result.head()
~~~

### Query Multiple Files with Wildcards

~~~python
import opteryx

# Query all Parquet files in a directory
result = opteryx.query("""
    SELECT * 
    FROM 's3://my-bucket/data/*.parquet'
    WHERE name LIKE 'M%'
""")

result.head()
~~~

## Supported File Formats

Opteryx can query the following formats directly from S3:

- **Parquet** (`.parquet`)
- **CSV** (`.csv`)
- **JSONL** (`.jsonl`)
- **ORC** (`.orc`)
- **Avro** (`.avro`)

## Performance Tips

- **Use Parquet** for better performance with columnar data
- **Partition your data** to enable partition pruning
- **Use wildcards strategically** to limit the number of files scanned
- **Apply filters** to reduce data transfer from S3

## Example: Joining S3 Data with Local Data

~~~python
import opteryx

# Join data from S3 with a local file
result = opteryx.query("""
    SELECT 
        s3_data.customer_id,
        s3_data.purchase_amount,
        local_data.customer_name
    FROM 's3://my-bucket/sales/2024/*.parquet' AS s3_data
    JOIN 'local_customers.csv' AS local_data
    ON s3_data.customer_id = local_data.id
""")

result.head()
~~~

## Troubleshooting

**Permission Denied Errors**
- Verify your AWS credentials are configured correctly
- Check that your IAM user/role has `s3:GetObject` permission for the bucket

**File Not Found**
- Ensure the S3 path is correct
- Verify the bucket name and object key exist

**Slow Queries**
- Consider using Parquet instead of CSV for better performance
- Apply WHERE clauses to filter data early
- Check your network connection to AWS
