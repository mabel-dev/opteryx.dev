import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "../../opteryx"))

import opteryx
import time
import pandas


df = opteryx.query("SELECT * FROM $astronauts CROSS JOIN $satellites")

ts = time.monotonic()
p = df.pandas()
print(time.monotonic() - ts)
print(p.head(), len(p))


ts = time.monotonic()
p = df.arrow().to_pandas()
print(time.monotonic() - ts)
print(p.head(), len(p))


ts = time.monotonic()
p = df.pandas()
print(time.monotonic() - ts)
print(p.head(), len(p))


ts = time.monotonic()
p = df.arrow().to_pandas()
print(time.monotonic() - ts)
print(p.head(), len(p))