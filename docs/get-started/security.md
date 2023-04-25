# Security

## Statement Execution

Opteryx allows you to prevent users from executing classes of queries, for example, you may limit a population of users to just being able to run `SELECT` statements and prevent them from running other types of queries.

This can be used to limit user's ability to perform certain actions on the engine; for example, limiting users to only perform `EXECUTE` queries.

Below is the complete list of permissions and the SQL query keyword which indicates that query type:

Permission    | Query Keyword
------------- | -------------------
Analyze       | `ANALYZE` :octicons-beaker-24: 
Execute       | `EXECUTE` :octicons-beaker-24: 
Explain       | `EXPLAIN`
Query         | `SELECT`
SetVariable   | `SET`
ShowColumns   | `SHOW COLUMNS`
ShowCreate    | `SHOW CREATE`
ShowFunctions | `SHOW FUNCTIONS`
ShowVariables | `SHOW VARIABLES`
ShowVariable  | `SHOW`

!!! Note
    - `Analyze` and `Execute` are not fully supported statements.
    - `ShowVariable` only applies to queries that are not one of the more specific `SHOW` query types.
    - Permissions exist for query types supported by the parser library but not supported by Opteryx.

Permissions are applied to connections using the `permissions` parameter. The default permissions allow all queries to be executed.

~~~python
import opteryx

conn = opteryx.connect(permissions={"Query"})
curr = conn.cursor()
# The user does not have permissions to execute a SHOW COLUMNS statement
# and this will raise a PermissionsError
try:
    curr.execute("SHOW COLUMNS FROM $planets")
    print(curr.head())
except opteryx.exceptions.PermissionsError:
    print("User does not have permission to execute this query")
~~~

Opteryx does not have any defined roles; however, we can implement a Role-Based access model using code similar to the below.

~~~python
import opteryx

# Define which roles exist and the permissions each role has,
# `opteryx.constants.PERMISSIONS` is all available permissions.
role_permissions = {
    "admin": opteryx.constants.PERMISSIONS,
    "user": {"Query"}
}

def get_user_permissions(user_roles:list):
    # return the accumulated permissions for a user by appending
    # the permissions for each of the roles for that user
    permissions = set()
    for role in user_roles:
        if role in role_permissions:
            permissions |= role_permissions[role]
    return permissions

user_permissions = get_user_permissions(["user"])

# this can now be passed when creating a connection
conn = opteryx.connect(permissions=user_permissions)
~~~

In this code, we have a variable `user_roles` that contains the roles a user has and a dictionary `role_permissions` that contains the permissions each role has. When the code executes, it sets the `permissions` variable with all the permissions the user has.
