# Orso

> IN DEVELOPMENT

Orso is a DataFrame library implemented for Opteryx and HadroDB.

<dl>
    <dt><h2>class <b>DataFrame</b> (<i>dictionaries</i>)</h2></dt>  
    <dd>
 
<h3>Constructor Parameters</h3>
<dl>
    <dt><b>dictionaries</b> iterable of dicts</dt>
    <dd>An Iterable (list, tuple, generator) of Python dicts. Where the dicts have different fields, only the fields from the first dict are used to determine the schema. Missing values are filled with Nones.
    </dd>
</dl>

<h3>Properties</h3>
<dl>
    <dt><b>column_names</b> tuple of strings</dt>
    <dd>The names of the columns in the DataFrame.</dd>
    <dt><b>num_columns</b> int</dt>
    <dd>The number of columns in the DataFrame.</dd>
    <dt><b>num_rows</b> int</dt>
    <dd>The number of rows in the DataFrame.</dd>
</dl>

<h3>Functions</h3>
<dl>
    <dt><h4>def <b>collect</b> (columns) -> list, list of lists</h4></dt>
    <dd>
        Fetch all of the values in specified columns.
        <p><b>Parameters</b></p>
        <ul>
            <li>
                columns: int, str, list of int, list of str<br />
                If an int, fetch the column with that offset. If a str, fetch the column with that name, if a list of ints, fetch the columns at the given offsets, if a list of strings, fetch the columns with those names.
            </li>
        </ul>
        <p><b>Returns</b></p>
        <p>list, if a single column has been specified. list of lists, if multiple columns have been specified.</p>
    </dd>
</dl>
<dl>
<dt><h4>def <b>distinct</b> () -> orso.DataFrame</h4></dt>
<dt><h4>def <b>query</b> () -> orso.DataFrame</h4></dt>
</dl>
<dl>
    <dt><h4>def <b>row</b> (i) -> orso.Row</h4></dt>
    <dd>
        Fetch a row from the DataFrame.
        <p><b>Parameters</b></p>
        <ul>
            <li>
                i: int<br />
                The offset of the Row to fetch.
            </li>
        </ul>
        <p><b>Returns</b></p>
        <p>orso.Row</p>
        <p><b>Raises</b></p>
        <p>ValidationError</p>
    </dd>
</dl>
<dt><h4>def <b>select</b> () -> orso.DataFrame</h4></dt>
<dl>
    <dt><h4>def <b>slice</b> (offset:int, length:int) -> orso.DataFrame</h4></dt>
    <dd>
        Slices a DataFrame.
        <p><b>Parameters</b></p>
        <ul>
            <li>
                offset: int (optional)<br />
                The starting row of the slice, if not provided the slice starts from the first row. Negative values are offsets from the last record.
            </li>
            <li>
                length: int (optional)<br />
                The number of records to include in the slice.
            </li>
        </ul>
        <p><b>Returns</b></p>
        <p>orso.DataFrame</p>
    </dd>
</dl>
<dt><h4>def <b>to_arrow</b> () -> orso.DataFrame</h4></dt>

</dd>
</dl>