# orso

[orso](https://github.com/mabel-dev/orso) is a DataFrame library.

<dl>
    <dt><h2>class <b>DataFrame</b> (<i>dictionaries</i>)</h2></dt>  
    <dd>

<h3>Constructors</h3>
<dl>
    <dt><h4><b>DataFrame</b> (dictionaries) </h4></dt>
    <dd>
    <p><b>Parameters</b></p>
    <ul>
        <dt><b>dictionaries</b>: iterable of dicts</dt>
        <dd>An Iterable (list, tuple, generator) of Python dicts. Where the dicts have different fields, only the fields from the first dict are used to determine the schema. Missing values are filled with Nones.
        </dd>
    </ul>
    </dd>
    <dt><h4><b>DataFrame.from_arrow</b> (table) </h4></dt>
    <dd>
    <p><b>Parameters</b></p>
    <ul>
        <dt><b>table</b>: pyarrow.Table</dt>
        <dd>Return an orso DataFrame representation of a pyarrow.Table.
        </dd>
    </ul>
    </dd>
</dl>

<h3>Properties</h3>
<dl>
    <dt><b>column_names</b> tuple of strings</dt>
    <dd>The names of the columns in the DataFrame.</dd>
    <dt><b>columncount</b> int</dt>
    <dd>The number of columns in the DataFrame.</dd>
    <dt><b>rowcount</b> int</dt>
    <dd>The number of rows in the DataFrame.</dd>
</dl>

<h3>Functions</h3>
<dl>
    <dt><span class="python-kw">def</span> <b>append</b> (row) -> None</dt>
<dd>
    Appends a row to the DataFrame.
    <p><b>Parameters</b></p>
    <ul>
        <b>row</b>: Tuple<br />
        Tuple containing the data for the new row.
    </ul>
</dd>

<dt><span class="python-kw">def</span> <b>collect</b> (columns) -> list, list of lists</dt>
<dd>
    Collects specified columns from the internal row storage into a tuple of lists.
    <p><b>Parameters</b></p>
    <ul>
        <b>columns</b>: int, str, list of int, list of str<br />
        Integer index, string name, or list of columns to collect.
    </ul>
    <p><b>Returns</b></p>
    <p>list, if a single column has been specified. list of lists, if multiple columns have been specified.</p>
</dd>

<dt><span class="python-kw">def</span> <b>slice</b> (offset, length=None) -> DataFrame</dt>
<dd>
    Returns a sliced DataFrame.
    <p><b>Parameters</b></p>
    <ul>
        <b>offset</b>: int<br />
        Start index for the slice.
        <b>length</b>: int, optional<br />
        Length of the slice.
    </ul>
    <p><b>Returns</b></p>
    <p>A new DataFrame containing the sliced data.</p>
</dd>

<dt><span class="python-kw">def</span> <b>filter</b> (mask) -> DataFrame</dt>
<dd>
    Select rows from the DataFrame based on a boolean array.
    <p><b>Parameters</b></p>
    <ul>
        <b>mask</b>: boolean array<br />
        Boolean array for filtering rows.
    </ul>
    <p><b>Returns</b></p>
    <p>A new DataFrame containing the filtered data.</p>
</dd>

<dt><span class="python-kw">def</span> <b>take</b> (indexes) -> DataFrame</dt>
<dd>
    Select rows from the DataFrame based on their index.
    <p><b>Parameters</b></p>
    <ul>
        <b>indexes</b>: list of int<br />
        List of row indexes to take.
    </ul>
    <p><b>Returns</b></p>
    <p>A new DataFrame containing the specified rows.</p>
</dd>

<dt><span class="python-kw">def</span> <b>row</b> (i) -> Row</dt>
<dd>
    Returns a single row from the DataFrame.
    <p><b>Parameters</b></p>
    <ul>
        <b>i</b>: int<br />
        Index of the row.
    </ul>
    <p><b>Returns</b></p>
    <p>A Row object.</p>
</dd>

<dt><span class="python-kw">def</span> <b>fetchone</b> () -> Row or None</dt>
<dd>
    Fetches a single row from the DataFrame.
    <p><b>Returns</b></p>
    <p>A Row object or None if no more rows are available.</p>
</dd>

<dt><span class="python-kw">def</span> <b>fetchmany</b> (size=None) -> list of Row</dt>
<dd>
    Fetches multiple rows from the DataFrame.
    <p><b>Parameters</b></p>
    <ul>
        <b>size</b>: int, optional<br />
        Number of rows to fetch (defaults to arraysize).
    </ul>
    <p><b>Returns</b></p>
    <p>A list of Row objects.</p>
</dd>

<dt><span class="python-kw">def</span> <b>fetchall</b> () -> list of Row</dt>
<dd>
    Fetches all rows from the DataFrame.
    <p><b>Returns</b></p>
    <p>A list of all Row objects in the DataFrame.</p>
</dd>
