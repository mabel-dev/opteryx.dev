# Python Client

<!--- this page is automatically build from connection.py --->

<!--- target format
<dl>
    <dt><h2>class <b>Schema</b> (definition)</h2></dt>  
    <dd>
    Tests a dictionary against a schema to test for conformity. Schema definition is similar to - but not the same as - avro schemas
 
    <h3>Parameters</h3>
    <dl>
        <dt><b>definition:</b> dictionary or string</dt>
        <dd>A dictionary, a JSON string of a dictionary or the name of a JSON file containing a schema definition
        </dd>
    </dl>

    <h3>Properties</h3>
    <dl>
        <dt><b>definition</b> dictionary or string</dt>
        <dd>A dictionary, a JSON string of a dictionary or the name of a JSON file containing a schema definition
        </dd>
    </dl>

    <h3>Functions</h3>
    <dl>
        <dt><h4>def <b>validate</b> (subject, raise_exception) -> dictionary or string</h4></dt>
        <dd>
            Test a dictionary against the Schema.

            <p><b>Parameters</b></p>
            <ul>
                <li>
                    subject: dictionary<br />
                    The dictionary to test for conformity
                </li>
                <li>
                    raise_exception: boolean<br />
                    If True, when the subject doesn't conform to the schema a ValidationError is raised
                </li>
            </ul>

            <p><b>Returns</b></p>
            <p>boolean, True is subject conforms</p>

            <p><b>Raises</b></p>
            <p>ValidationError</p>
        </dd>
    </dl>

</dd>
</dl>
--->

<!--- start --->
<dl><dt><h2>class <b>Connection</b> ()</h2></ul></dd></dl><dl><dt><b>cursor</b> ()</dt><dd>
</br>return a cursor object</li></ul></dd></dl>
<dl><dt><b>close</b> ()</dt><dd>
</br>exists for interface compatibility only</li></ul></dd></dl>
<dl><dt><b>commit</b> ()</dt><dd>
</br>exists for interface compatibility only</li></ul></dd></dl>
<dl><dt><b>rollback</b> ()</dt><dd>
</br>exists for interface compatibility only</li></ul></dd></dl>
<dl><dt><h2>class <b>Cursor</b> (connection)</h2></ul></dd></dl><dl><dt><b>id</b> ()</dt><dd>
</br>The unique internal reference for this query</li></ul></dd></dl>
<dl><dt><b>execute</b> (operation, params)</dt><dd></ul></dd></dl>
<dl><dt><b>rowcount</b> ()</dt><dd></ul></dd></dl>
<dl><dt><b>shape</b> ()</dt><dd></ul></dd></dl>
<dl><dt><b>stats</b> ()</dt><dd>
</br>execution statistics</li></ul></dd></dl>
<dl><dt><b>messages</b> ()</dt><dd>
</br>list of run-time warnings</li></ul></dd></dl>
<dl><dt><b>fetchone</b> (as_dicts)</dt><dd>
</br>Fetch one record only.</li>

<p><b>Parameters</b></p><ul><li>as_dicts:  boolean (optional)
</br>Return a dictionary, default is False, return a tuple</li></ul></dd></dl>
<dl><dt><b>fetchmany</b> (size, as_dicts)</dt><dd>
</br>fetch a given number of records</li></ul></dd></dl>
<dl><dt><b>fetchall</b> (as_dicts)</dt><dd>
</br>fetch all matching records</li></ul></dd></dl>
<dl><dt><b>arrow</b> (size)</dt><dd>
</br>Fetch the resultset as a pyarrow table, this is generally the fastest way to</li> get the entire set of results.

<p><b>Parameters</b></p><ul><li>size:  int (optional)
</br>Return the head 'size' number of records.</li>

<p><b>Returns</b></p><ul><li>pyarrow.Table</ul></dd></dl>

<dl><dt><b>to_df</b> (size)</dt><dd>
</br>Fetch the resultset as a pandas DataFrame.

<p><b>Parameters</b></p><ul><li>size:  int (optional)
</br>Return the head 'size' number of records.</li>

<p><b>Returns</b></p><ul><li>pandas.DataFrame</ul></dd></dl>

<dl><dt><b>close</b> ()</dt><dd>
</br>close the connection</li></ul></dd></dl>
<dl><dt><b>head</b> (size)</dt><dd></ul></dd></dl>

<hr><p>This file has been automatically generated from the source code.</p>