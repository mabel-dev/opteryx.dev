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

You can query files in GCS by using the GCS URI in your SQL query.

### Query a Single File

~~~python
import opteryx

# Query a Parquet file in GCS
result = opteryx.query("""
    SELECT * 
    FROM 'gs://my-bucket/data/planets.parquet'
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
    FROM 'gs://my-bucket/data/*.parquet'
    WHERE name LIKE 'M%'
""")

result.head()
~~~

## Supported File Formats

Opteryx can query the following formats directly from GCS:

- **Parquet** (`.parquet`)
- **CSV** (`.csv`)
- **JSONL** (`.jsonl`)
- **ORC** (`.orc`)
- **Avro** (`.avro`)

## Performance Tips

- **Use Parquet** for better performance with columnar data
- **Partition your data** to enable partition pruning
- **Use wildcards strategically** to limit the number of files scanned
- **Apply filters** to reduce data transfer from GCS

## Example: Joining GCS Data with Local Data

~~~python
import opteryx

# Join data from GCS with a local file
result = opteryx.query("""
    SELECT 
        gcs_data.customer_id,
        gcs_data.purchase_amount,
        local_data.customer_name
    FROM 'gs://my-bucket/sales/2024/*.parquet' AS gcs_data
    JOIN 'local_customers.csv' AS local_data
    ON gcs_data.customer_id = local_data.id
""")

result.head()
~~~

## Example: Combining GCS and BigQuery

~~~python
import opteryx
from opteryx.connectors import SqlConnector
from sqlalchemy import create_engine

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
    FROM 'gs://my-bucket/transactions/*.parquet' AS gcs
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
- Ensure the GCS path is correct (use `gs://` prefix)
- Verify the bucket name and object path exist
- Check bucket permissions

**Slow Queries**
- Consider using Parquet instead of CSV for better performance
- Apply WHERE clauses to filter data early
- Check your network connection to Google Cloud
