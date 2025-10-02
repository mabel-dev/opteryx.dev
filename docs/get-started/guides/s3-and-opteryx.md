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

To query files in S3, you need to register the S3 connector with a prefix that maps to your bucket.

### Basic Setup

~~~python
import opteryx
from opteryx.connectors import AwsS3Connector

# Register S3 connector for your bucket
# Use the bucket name as the prefix
opteryx.register_store("my-bucket", AwsS3Connector)

# Now you can query files using the registered prefix
result = opteryx.query("""
    SELECT * 
    FROM my-bucket.data.planets
    LIMIT 10
""")

# Display results
result.head()
~~~

!!! note
    The dataset path `my-bucket.data.planets` refers to files in the S3 path `s3://my-bucket/data/planets/`. Opteryx uses dot notation instead of S3 URIs.

### Query a Single File

~~~python
import opteryx
from opteryx.connectors import AwsS3Connector

# Register the S3 connector
opteryx.register_store("my-bucket", AwsS3Connector)

# Query a Parquet file in S3
result = opteryx.query("""
    SELECT * 
    FROM my-bucket.data.planets
    LIMIT 10
""")

# Display results
result.head()
~~~

### Query Multiple Files

~~~python
import opteryx
from opteryx.connectors import AwsS3Connector

# Register the S3 connector
opteryx.register_store("my-bucket", AwsS3Connector)

# Query all files in a dataset directory
result = opteryx.query("""
    SELECT * 
    FROM my-bucket.data.planets
    WHERE name LIKE 'M%'
""")

result.head()
~~~

!!! note
    When querying a dataset like `my-bucket.data.planets`, Opteryx reads all compatible files in that directory (e.g., all `.parquet` files in `s3://my-bucket/data/planets/`).

## Supported File Formats

Opteryx can query the following formats directly from S3:

- **Parquet** (`.parquet`)
- **CSV** (`.csv`)
- **JSONL** (`.jsonl`)
- **ORC** (`.orc`)
- **Avro** (`.avro`)

## Performance Tips

- **Use Parquet** for better performance with columnar data
- **Partition your data** by date or category to enable partition pruning
- **Structure data in dataset directories** - Opteryx will automatically read all compatible files in a dataset folder
- **Apply filters** to reduce data transfer from S3

## Example: Joining S3 Data with Local Data

~~~python
import opteryx
from opteryx.connectors import AwsS3Connector

# Register the S3 connector
opteryx.register_store("my-bucket", AwsS3Connector)

# Join data from S3 with a local file
result = opteryx.query("""
    SELECT 
        s3_data.customer_id,
        s3_data.purchase_amount,
        local_data.customer_name
    FROM my-bucket.sales.transactions AS s3_data
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
