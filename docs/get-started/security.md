# Security

## Statement Execution

Opteryx allows you to prevent users from executing classes of query, for example you may limit a population of users to just being able to run `SELECT` statements, and prevent them from running other types of query.

This can be used to limit user's ability to perform certain actions on the engine; for example limiting users to only perform `EXECUTE` queries.

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
    - `Analyze` and `Execute` and not fully supported statements.
    - `ShowVariable` only applies to queries that are not one of the more specific `SHOW` query types.

Permissions are applied to connections using the `permissions` parameter, the default permissions are to allow all queries to be executed.

~~~python
import opteryx

conn = opteryx.connect(permissions={"Query"})
curr = conn.cursor()
# The user does not have permissions to execute a SHOW COLUMNS statement
# and this will return a PermissionsError
try:
    curr.execute("SHOW COLUMNS FROM $planets")
    print(curr.head())
except opteryx.exceptions.PermissionsError:
    print("User does not have permission to execute this query")
~~~

Opteryx does not have any defined roles, however we can implement Role-Based access model using code similar to the below.

~~~python
import opteryx

role_permissions = {
    "admin": opteryx.permissions,
    "user": {"Query"}
}

def get_user_permissions(user_roles):
    permissions = set()
    for role in user_roles:
        if role in role_permissions:
            permissions |= role_permissions[role]
    return permissions

user_permissions = get_user_permissions(["user"])
~~~

In this code we have a variable `user_roles` which contains the roles a user has, and a dictionary `role_permissions` which contains the permissions each role has. When the code executes it sets the `permissons` variable with the all of the permissions which the user has.
