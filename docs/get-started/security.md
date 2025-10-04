---
title: Security in Opteryx - Access Control and Permissions
description: Implement security in Opteryx with statement execution controls, user membership restrictions, and role-based access control (RBAC).
---

# Security

Opteryx provides two primary security features designed to restrict user actions and control data access. Since Opteryx does not maintain a traditional user model, access control is managed through contextual information, such as AD Groups, rather than predefined user accounts. This framework supports implementing a traditional Role-Based Access Control (RBAC) system if desired.

The two security features are:

1. **Statement Execution Control** - Limits the types of queries users can execute (e.g., restricting users to only `SELECT` or `EXECUTE` statements)
2. **User Membership Restrictions** - Provides a mechanism for fine-grained, row-level access control

## Statement Execution Controls

Opteryx provides mechanisms to restrict the types of SQL statements that users can execute.

This feature limits a user's ability to perform certain actions on the engine. For example, you can restrict users to only execute `EXECUTE` queries, or allow only `SELECT` statements.

### Permissions Overview

Below is a table of permissions associated with their respective SQL commands:

| Permission    | Query Keyword    |
|---------------|------------------|
| Analyze       | `ANALYZE` :octicons-beaker-24: |
| Execute       | `EXECUTE` :octicons-beaker-24: |
| Explain       | `EXPLAIN`        |
| Query         | `SELECT`         |
| SetVariable   | `SET`            |
| ShowColumns   | `SHOW COLUMNS`   |
| ShowCreate    | `SHOW CREATE`    |
| ShowFunctions | `SHOW FUNCTIONS` |
| ShowVariables | `SHOW VARIABLES` |
| ShowVariable  | `SHOW`           |

!!! Note
    - `Analyze` and `Execute` are not fully supported statements.
    - `ShowVariable` only applies to queries that are not one of the more specific `SHOW` query types.
    - Permissions exist for query types supported by the parser library but not supported by Opteryx.

Permissions are applied at the connection level using the `permissions` parameter, with the default setting allowing all queries.

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

Opteryx does not have predefined roles; however, you can implement a Role-Based Access Control (RBAC) model using code similar to the example below.

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

In this code, we define a `user_roles` variable containing the roles assigned to a user and a `role_permissions` dictionary mapping each role to its permissions. The accumulated permissions for a user are computed and stored in the `user_permissions` variable.

Permissions can also be set using the short-form query API:

~~~python
data = opteryx.query("SELECT * FROM $planets", permissions=user_permissions)
~~~

## User Membership Restrictions

Opteryx supports user-specific data access by embedding user attributes directly into queries, enabling fine-grained access control. This functionality isn't automatic; it requires explicit query formulation to incorporate data filtering based on user attributes.

Memberships are specified via the `memberships` parameter during connection setup, making them accessible within queries through the `@@user_memberships` variable and the `$user` virtual table. By default, no memberships are configured (`memberships=[]`).

The following example demonstrates how to use array-type memberships to restrict data access:

~~~python
import opteryx

conn = opteryx.connect(memberships=["Apollo 11"])
curr = conn.cursor()

# the missions field is an ARRAY
curr.execute("SELECT * FROM $astronauts WHERE ARRAY_CONTAINS_ANY(missions, @@user_memberships)")
print(curr.head())
~~~

Here is how you might test memberships where the attribute is a VARCHAR:

~~~python
import opteryx

conn = opteryx.connect(memberships=["Apollo 11"])
curr = conn.cursor()

# the Missions field is a VARCHAR
curr.execute("SELECT $missions.* FROM $missions INNER JOIN $user ON Mission = value WHERE attribute = 'membership'")
print(curr.head())
~~~

Memberships can also be provided using the short-form query API:

~~~python
data = opteryx.query("SELECT * FROM $planets", memberships=["Apollo 11"])
~~~

Memberships and permissions can be defined simultaneously and utilized in queries through both explicit SQL and the short-form query API.