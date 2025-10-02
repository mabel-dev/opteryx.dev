---
title: Query Google Cloud Storage with Opteryx - SQL for GCS Data
description: Query Parquet, CSV, JSONL files in Google Cloud Storage with Opteryx SQL engine. Run federated queries across GCS, BigQuery, and other sources.
---

# Querying Google Cloud Storage with Opteryx

This guide demonstrates how to query data stored in Google Cloud Storage (GCS) buckets using Opteryx. Opteryx can directly read various file formats (Parquet, CSV, JSONL, ORC, Avro) from GCS without needing to download them first.

## Installation

Install Opteryx with GCS support.

~~~console
$ pip install opteryx
~~~

## Authentication

Opteryx uses standard Google Cloud credential mechanisms. Ensure you have GCP credentials configured through one of:

- Application Default Credentials (ADC)
- Service account key file (set `GOOGLE_APPLICATION_CREDENTIALS` environment variable)
- OAuth 2.0 token (when running on Google Cloud infrastructure)

For local development, authenticate using:

~~~console
$ gcloud auth application-default login
~~~

## Querying GCS Files

To query files in GCS, you need to register the GCS connector with a prefix that maps to your bucket.

### Basic Setup

~~~python
import opteryx
from opteryx.connectors import GcpCloudStorageConnector

# Register GCS connector for your bucket
# Use the bucket name as the prefix
opteryx.register_store("my-bucket", GcpCloudStorageConnector)

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
    The dataset path `my-bucket.data.planets` refers to files in the GCS path `gs://my-bucket/data/planets/`. Opteryx uses dot notation instead of GCS URIs.

### Query a Single File

~~~python
import opteryx
from opteryx.connectors import GcpCloudStorageConnector

# Register the GCS connector
opteryx.register_store("my-bucket", GcpCloudStorageConnector)

# Query a Parquet file in GCS
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
from opteryx.connectors import GcpCloudStorageConnector

# Register the GCS connector
opteryx.register_store("my-bucket", GcpCloudStorageConnector)

# Query all files in a dataset directory
result = opteryx.query("""
    SELECT * 
    FROM my-bucket.data.planets
    WHERE name LIKE 'M%'
""")

result.head()
~~~

!!! note
    When querying a dataset like `my-bucket.data.planets`, Opteryx reads all compatible files in that directory (e.g., all `.parquet` files in `gs://my-bucket/data/planets/`).

## Supported File Formats

Opteryx can query the following formats directly from GCS:

- **Parquet** (`.parquet`)
- **CSV** (`.csv`)
- **JSONL** (`.jsonl`)
- **ORC** (`.orc`)
- **Avro** (`.avro`)

## Performance Tips

- **Use Parquet** for better performance with columnar data
- **Partition your data** by date or category to enable partition pruning
- **Structure data in dataset directories** - Opteryx will automatically read all compatible files in a dataset folder
- **Apply filters** to reduce data transfer from GCS

## Example: Joining GCS Data with Local Data

~~~python
import opteryx
from opteryx.connectors import GcpCloudStorageConnector

# Register the GCS connector
opteryx.register_store("my-bucket", GcpCloudStorageConnector)

# Join data from GCS with a local file
result = opteryx.query("""
    SELECT 
        gcs_data.customer_id,
        gcs_data.purchase_amount,
        local_data.customer_name
    FROM my-bucket.sales.transactions AS gcs_data
    JOIN 'local_customers.csv' AS local_data
    ON gcs_data.customer_id = local_data.id
""")

result.head()
~~~

## Example: Combining GCS and BigQuery

~~~python
import opteryx
from opteryx.connectors import SqlConnector, GcpCloudStorageConnector
from sqlalchemy import create_engine

# Register GCS
opteryx.register_store("my-bucket", GcpCloudStorageConnector)

# Register BigQuery
GCP_PROJECT = "your-gcp-project"
bq_engine = create_engine(f"bigquery://{GCP_PROJECT}")
opteryx.register_store(
    prefix="bq",
    connector=SqlConnector,
    remove_prefix=True,
    engine=bq_engine
)

# Query joining GCS files with BigQuery tables
result = opteryx.query("""
    SELECT 
        gcs.transaction_id,
        gcs.amount,
        bq.customer_name
    FROM my-bucket.transactions AS gcs
    JOIN bq.customers AS bq
    ON gcs.customer_id = bq.id
""")

result.head()
~~~

## Troubleshooting

**Permission Denied Errors**
- Verify your GCP credentials are configured correctly
- Check that your service account has `storage.objects.get` permission for the bucket
- Run `gcloud auth application-default login` for local development

**File Not Found**
- Ensure the GCS path is correct
- Verify the bucket name and object path exist
- Check bucket permissions

**Slow Queries**
- Consider using Parquet instead of CSV for better performance
- Apply WHERE clauses to filter data early
- Check your network connection to Google Cloud
