# Debug Logging

## Overview

This feature automatically transforms specific comment lines into debugging print statements during development. Comments in the form `# DEBUG: log(<string>)` will be converted to `print(<string>)`. The goal is to facilitate debugging without permanently altering the codebase.

The `# DEBUG: log` function supports `print` functionality such as formatting with f-strings and printing comma separated values.

## Activation

To enable this feature, set an environment variable `OPTERYX_DEBUG`.

Via the terminal:
~~~console
export OPTERYX_DEBUG=1
~~~

or via code:
~~~python
import os
os.environ["OPTERYX_DEBUG"] = "1"
~~~

or via a .env file
~~~ini
OPTERYX_DEBUG=1
~~~
!!! note
    using a .env file requiores [dotenv](https://pypi.org/project/python-dotenv/) to be installed

## Usage
Insert comments in your code following this template:

~~~python
# DEBUG: log "Debug message."
~~~

When this feature is active, this will become:

~~~python
print("Debug message.")
~~~

When this is not active, it will remain a comment.

## Rationale

**Debugging**: Facilitates the addition of debugging log points without requiring code changes.   
**Code Cleanliness**: Avoids cluttering the codebase with `if`s for debugging statements.   
**Convenience**: Controlled through an environment variable, allowing for easy toggling.

## Caveats

**Performance**: There may be a slight performance impact during the import stage.   
**Complexity**: The feature performs dynamic code modification, so developers should understand its implications.

## Contribution

Contributions to this feature should align with the standard Opteryx development guidelines.