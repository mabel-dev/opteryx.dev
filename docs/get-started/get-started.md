# Get Started

## Installation

### Requirements

- Operating System: MacOS, Linux or Windows
- Python:
    - 3.9 or later
    - **Note**: Windows is not recommented

### Install from PyPI (recommended)

We recommend installing Opteryx within a virtual environment. This will install the latest release version.

~~~console
$ python -m venv myenv
$ source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
$ pip install --upgrade opteryx
~~~

## Build from Source

To get the latest version, including pre-release and beta versions, you can build from the source code on GitHub.

~~~console
$ pip install git+https://github.com/mabel-dev/opteryx
~~~

!!! Note  
    This is not recommended for production use and involves additional steps and requirements dependant on the operating system and environment.

## Additional Resources

- [API Documentation](../python-client/)
- [Usage Examples](https://github.com/mabel-dev/opteryx#examples)
- [Discord Server](https://discord.gg/qpv2tr989x)

## Troubleshooting

### FAQ

**Q**: What is the most common cause of installation problems?   
**A**: Often, the issue is related to the Python version. Ensure you have Python 3.9 or later, and for Apple Silicon Mac, Python 3.11 or later is required.