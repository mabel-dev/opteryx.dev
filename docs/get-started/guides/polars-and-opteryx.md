# Polars and Opteryx Integration

This short guide demonstrates how to integrate Polars and Opteryx, showing you how to query a Polars dataframe with Opteryx and how to return Polars dataframe from Opteryx.

## Installation

Install Opteryx and Polars.

~~~console
$ pip install opteryx
$ pip install polars
~~~

## Polars to Opteryx

Opteryx can natively query Polars DataFrames by registering the DataFrame as a data source.

~~~python
import opteryx
import polars

# Create the DataFrame
data = {
    "Name": ["Huey", "Dewey", "Louie"],
    "Age": [12, 12, 12],
    "Favorite Color": ["Red", "Blue", "Green"],
}
df = polars.DataFrame(data)

# Register as a data source
opteryx.register_df("nephews", df)

results = opteryx.query("SELECT * FROM nephews")
~~~

## Opteryx to Polars

Opteryx can output results as Polars DataFrames using the `.polars()` result-conversion method.

~~~python
import opteryx

dataframe = opteryx.query("SELECT * FROM $planets").polars()
~~~
