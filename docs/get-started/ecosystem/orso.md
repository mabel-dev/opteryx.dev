# orso

> IN DEVELOPMENT

orso is a DataFrame library implemented for Opteryx and HadroDB.

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
    <dt><span class="python-kw">def</span> <b>collect</b> (columns) -> list, list of lists</dt>
    <dd>
        Fetch all of the values in specified columns.
        <p><b>Parameters</b></p>
        <ul>
            <b>columns</b>: int, str, list of int, list of str<br />
            If an int, fetch the column with that offset. If a str, fetch the column with that name, if a list of ints, fetch the columns at the given offsets, if a list of strings, fetch the columns with those names.
        </ul>
        <p><b>Returns</b></p>
        <p>list, if a single column has been specified. list of lists, if multiple columns have been specified.</p>
    </dd>
</dl>
<dl>
<dt><span class="python-kw">def</span> <b>distinct</b> () -> orso.DataFrame</dt>
</dl>
<dl>
<dt><span class="python-kw">def</span> <b>filter</b> (mask) -> orso.DataFrame</dt>
</dl>
<dl>
<dt><span class="python-kw">def</span> <b>query</b> () -> orso.DataFrame</dt>
</dl>
<dl>
    <dt><span class="python-kw">def</span> <b>row</b> (i) -> orso.Row</dt>
    <dd>
        Fetch a row from the DataFrame.
        <p><b>Parameters</b></p>
        <ul>
            <b>i</b>: int<br />
            The offset of the Row to fetch.
        </ul>
        <p><b>Returns</b></p>
        <p>orso.Row</p>
        <p><b>Raises</b></p>
        <p>ValidationError</p>
    </dd>
</dl>
<dl>
<dt><span class="python-kw">def</span> <b>select</b> () -> orso.DataFrame</dt>
</dl>
<dl>
    <dt><span class="python-kw">def</span> <b>slice</b> (offset:int, length:int) -> orso.DataFrame</dt>
    <dd>
        Slices a DataFrame.
        <p><b>Parameters</b></p>
        <ul>
            <b>offset</b>: int (optional)<br />
            The starting row of the slice, if not provided the slice starts from the first row. Negative values are offsets from the last record.<br />
            <b>length</b>: int (optional)<br />
            The number of records to include in the slice.
        </ul>
        <p><b>Returns</b></p>
        <p>orso.DataFrame</p>
    </dd>
</dl>
<dl>
<dt><span class="python-kw">def</span> <b>to_arrow</b> () -> orso.DataFrame</dt>
</dl>
</dd>
</dl>

<dl>
    <dt><h2>class <b>Row</b> ()</h2></dt>  
</dl>