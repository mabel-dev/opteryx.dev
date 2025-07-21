# Integrating Pandas with Opteryx

This short guide demonstrates how to integrate Pandas and Opteryx, showing you how to query a Pandas dataframe with Opteryx and how to return Pandas dataframe from Opteryx.

## Installation

Install Opteryx and Pandas.

~~~console
$ pip install opteryx pandas
~~~

## Pandas to Opteryx

Opteryx can natively query Pandas DataFrames by registering the DataFrame as a data source.

~~~python
import opteryx
import pandas

# Create the DataFrame
data = {
    "Name": ["Huey", "Dewey", "Louie"],
    "Age": [12, 12, 12],
    "Favorite Color": ["Red", "Blue", "Green"],
}
df = pandas.DataFrame(data)

# Register as a data source
opteryx.register_df("nephews", df)

results = opteryx.query("SELECT * FROM nephews")
~~~

## Opteryx to Pandas

Opteryx can output results as Pandas DataFrames using the `.pandas()` result-conversion method.

~~~python
import opteryx

dataframe = opteryx.query("SELECT * FROM $planets").pandas()
~~~
