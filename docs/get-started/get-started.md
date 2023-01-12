# Get Started



## Installation

**Install from PyPI (recommended)**

This will install the latest release version.

~~~bash
pip install --upgrade opteryx
~~~

**Install from GitHub**

The lastest version, including pre-release and beta versions can be installed, this is not recommended for production environments.

~~~bash
pip install git+https://github.com/mabel-dev/opteryx
~~~

## Your First Query

You can quickly test your installation is working as expected by querying one of the internal sample datasets.

~~~python
import opteryx

result = opteryx.query("SELECT * FROM $planets;").arrow()
print(result)
~~~