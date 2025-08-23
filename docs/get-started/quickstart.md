# Quickstart Guide

Get Opteryx running in minutes.

## Requirements

- OS: Linux, macOS, or Windows _(Windows is supported but not recommended for production use)_
- Python: 3.10 or later

### Install from PyPI (recommended)

We recommend using a virtual environment:

~~~console
$ python -m venv myenv
$ source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
$ pip install --upgrade opteryx
~~~

This installs the latest stable release.

## Install from Source (Bleeding-edge)

If you want the latest features or are contributing to Opteryx, install directly from GitHub:

~~~console
$ pip install git+https://github.com/mabel-dev/opteryx
~~~

!!! Note  
    Source builds may include unstable or experimental features and can have additional dependencies. Not recommended for production.

## Verify Installation

Run in Python:

~~~python
import opteryx
print(opteryx.query("SELECT 'Hello, Opteryx!'"))
~~~

## Resources

- [API Documentation](../python-client/)
- [Usage Examples](https://github.com/mabel-dev/opteryx#examples)
- [Discord Server](https://discord.gg/qpv2tr989x)

---

Ready to use it in Python? See the [Python Integration Guide](../python-client/)