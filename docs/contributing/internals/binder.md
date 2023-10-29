


LITERAL COLUMNS
- node_type is LITERAL
- schema_column is a ConstantColumn
- type is the data type of the ConstantColumn

get the value from the schema_column.value


IDENTIFIER
- node_tpye is IDENTIFIER
- schema_column is a FlatColumn
- source is the relation (remote dataset, subquery)
- source_column is the name of the column at the source

        alias=alias,  # AS alias, if provided
        source_column=branch[-1]["value"],  # the source column
        source=".".join(p["value"] for p in branch[:-1]),  # the source relation
