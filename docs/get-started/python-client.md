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
<dl><dt><h2>class <b>Connection</b> ()</h2></dt><dd></dd></dl>
<dl><dt><b>cursor</b> ()</dt><dd> 
return a cursor object</dd></dl>
<dl><dt><b>close</b> ()</dt><dd> 
exists for interface compatibility only</dd></dl>
<dl><dt><h2>class <b>Cursor</b> (connection)</h2></dt><dd></dd></dl>
<dl><dt><b>execute</b> (operation, params)</dt><dd></dd></dl>
<dl><dt><b>rowcount</b> ()</dt><dd></dd></dl>
<dl><dt><b>shape</b> ()</dt><dd></dd></dl>
<dl><dt><b>stats</b> ()</dt><dd> 
execution statistics</dd></dl>
<dl><dt><b>has_warnings</b> ()</dt><dd> 
do I have warnings</dd></dl>
<dl><dt><b>warnings</b> ()</dt><dd> 
list of run-time warnings</dd></dl>
<dl><dt><b>fetchone</b> (as_dicts)</dt><dd> 
fetch one record only</dd></dl>
<dl><dt><b>fetchmany</b> (size, as_dicts)</dt><dd> 
fetch a given number of records</dd></dl>
<dl><dt><b>fetchall</b> (as_dicts)</dt><dd> 
fetch all matching records</dd></dl>
<dl><dt><b>as_arrow</b> (size)</dt><dd> 
fetch all matching records as a pyarrow table</dd></dl>
<dl><dt><b>close</b> ()</dt><dd> 
close the connection</dd></dl>
<dl><dt><b>head</b> (size)</dt><dd></dd></dl>

<hr><p>This file has been automatically generated from the source code.</p>