    # Register the store, so we know queries for this store should be handled by
    # the SQL Connector
    opteryx.register_store(
        prefix="sql",
        connector=SqlConnector,
        remove_prefix=True,  # the prefix isn't part of the SQLite table name
        connection="sqlite:///database.db",  # SQLAlchemy connection string
    )
    result = opteryx.query("SELECT * FROM sql.planets LIMIT 5;")
    result.head()