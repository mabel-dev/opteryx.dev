import csv
import random
import opteryx

# Create a CSV file with 1 million rows
num_rows = 10_000_000
categories = ["A", "B", "C", "D", "E"]

with open("large_dataset.csv", "w", newline='') as csvfile:
    fieldnames = ["id", "value", "category"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for i in range(num_rows):
        writer.writerow({
            "id": i,
            "value": random.randint(1, 100),
            "category": random.choice(categories)
        })


import pandas as pd
import time

start_time = time.time()

# Read the entire CSV into Pandas
df = pd.read_csv("large_dataset.csv")

# Filter the DataFrame
filtered_df = df[df['category'] == "A"]

end_time = time.time()
pandas_time = end_time - start_time
print(f"Pandas read and then filter: {pandas_time:.2f} seconds")

del df

start_time = time.time()

# Read and filter the CSV using Opteryx
filtered_df = opteryx.query(
    """
    SELECT * FROM large_dataset.csv 
    WHERE category = 'A';
    """
).arrow().to_pandas()

end_time = time.time()
opteryx_time = end_time - start_time
print(f"Prefilter with Opteryx: {opteryx_time:.2f} seconds")
