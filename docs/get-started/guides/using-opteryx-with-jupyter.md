---
title: Using Opteryx with Jupyter Notebooks - SQL Query Engine for Data Science
description: Complete guide to using Opteryx SQL query engine in Jupyter Notebooks. Query data, visualize results with Matplotlib, and integrate with Pandas and Polars.
---

# Using Opteryx with Jupyter Notebooks

This guide demonstrates how to use Opteryx, a high-performance SQL query engine, with Jupyter Notebooks to analyze and visualize data interactively. Opteryx is designed to work seamlessly with large datasets and integrates directly with Python’s most popular data science libraries.

## Installation

For this guide, we assume you have a working Jupyter environment. For assistance on setting up Jupyter, see [Installing Jupyter](https://jupyter.org/install).

> Prebuilt [Binder](https://mybinder.org/v2/gh/mabel-dev/labs/HEAD) notebooks are also available for experimenting with Opteryx without any local setup.

To install Opteryx in your Jupyter environment, run the following command in a notebook cell. This ensures that Opteryx is installed in the same Python environment your notebook is using:

~~~console
# Ensure that Opteryx is installed in the current Jupyter kernel
import sys
!{sys.executable} -m pip install opteryx
~~~

## Getting Started

Here's how to execute a basic SQL query against an internal sample dataset and display the results directly in Jupyter:

~~~python
import opteryx

sql_statement = """
SELECT *
  FROM $planets
"""
results = opteryx.query(sql_statement)

# Display results in a Table
results
~~~

## Integration with Other Libraries

Opteryx supports seamless conversion of query results to formats suitable for further analysis or visualization:

- **Arrow**: Ideal for high-performance data processing.
  `results.arrow()`
- **Pandas**: Best for interactive data manipulation and analysis.
  `results.pandas()`
- **Polars**: Use when working with larger data sets or requiring faster performance.
  `results.polars()`

## Visualizing Data with Matplotlib

After querying data with Opteryx, you can easily visualize it. 

Here's an example of creating a pie chart to show the distribution of missions by company using an internal dataset of missions to space:

~~~python
import matplotlib.pyplot as plt
import opteryx

# Query to count missions per company
sql_statement = """
SELECT COUNT(*) as Missions, Company 
  FROM $missions
 GROUP BY Company
 ORDER BY Missions DESC;
"""
results = opteryx.query(sql_statement)

# Prepare data for the pie chart
missions = list(results["Missions"])
companies = list(results["Company"])
if len(missions) > 9:
    missions = missions[:9] + [sum(missions[9:])]
    companies = companies[:9] + ["Other"]

# Create a pie chart with an 'explode' effect for the largest segment
explode = [0.1 if i == 0 else 0 for i in range(len(missions))]
fig, ax = plt.subplots()
ax.pie(missions, labels=companies, autopct='%1.1f%%', explode=explode, startangle=90, counterclock=False)
ax.set_title('Missions Per Company')
plt.show()
~~~

## Next Steps

This guide has introduced you to the basics of using Opteryx with Jupyter Notebooks.

For a deeper dive into Opteryx, including detailed documentation on advanced features, visit the documentation at [Opteryx.dev](https://opteryx.dev). The site provides extensive resources and documentation to support your data projects.

Happy querying!

## Advanced Examples

### Time Series Analysis

~~~python
import opteryx
import matplotlib.pyplot as plt

# Analyze time series data
sql_statement = """
SELECT 
    DATE(timestamp) as date,
    COUNT(*) as events,
    AVG(value) as avg_value
FROM 'logs/*.jsonl'
WHERE timestamp >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY DATE(timestamp)
ORDER BY date
"""
results = opteryx.query(sql_statement).pandas()

# Plot the time series
plt.figure(figsize=(12, 6))
plt.plot(results['date'], results['events'], marker='o')
plt.title('Daily Event Count')
plt.xlabel('Date')
plt.ylabel('Events')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
~~~

### Working with Multiple Data Sources

~~~python
import opteryx
from opteryx.connectors import SqlConnector
from sqlalchemy import create_engine

# Register a database connection
engine = create_engine("postgresql+psycopg2://user:pass@host/db")
opteryx.register_store("pg", SqlConnector, remove_prefix=True, engine=engine)

# Join database data with files
sql_statement = """
SELECT 
    u.user_name,
    u.email,
    COUNT(e.event_id) as event_count
FROM pg.users AS u
LEFT JOIN 'events/*.parquet' AS e
ON u.user_id = e.user_id
GROUP BY u.user_name, u.email
ORDER BY event_count DESC
LIMIT 10
"""
results = opteryx.query(sql_statement)
results
~~~

### Interactive Data Exploration

~~~python
import opteryx
import ipywidgets as widgets
from IPython.display import display

# Create interactive filters
date_range = widgets.DateRangeSlider(
    description='Date Range:',
    layout={'width': '500px'}
)

def update_results(change):
    start, end = change['new']
    sql = f"""
    SELECT 
        product_category,
        SUM(amount) as total_sales
    FROM 's3://sales/*.parquet'
    WHERE date BETWEEN '{start}' AND '{end}'
    GROUP BY product_category
    ORDER BY total_sales DESC
    """
    results = opteryx.query(sql)
    display(results)

date_range.observe(update_results, names='value')
display(date_range)
~~~

## Related Guides

- [Pandas Integration](pandas-and-opteryx.md) - Work with Pandas DataFrames
- [Polars Integration](polars-and-opteryx.md) - Use Polars for faster processing
- [Query AWS S3](s3-and-opteryx.md) - Access data in cloud storage
- [Connect to PostgreSQL](postgres-and-opteryx.md) - Combine with database queries

