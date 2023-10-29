import opteryx
import time
import pandas


df = opteryx.query("SELECT * FROM $astronauts CROSS JOIN $satellites")

ts = time.monotonic()
p = df.pandas()
print(time.monotonic() - ts)
print(p.head())


ts = time.monotonic()
p = df.arrow().to_pandas()
print(time.monotonic() - ts)
print(p.head())