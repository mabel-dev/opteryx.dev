# Windows

This guide will help you to set up a Windows workstation to work with the code and develop Opteryx.

If using WSL, refer to the Debian/Ubuntu set up guide. Initial set up of the WSL component is not covered in these guides.

Intel/x86 is the recommended environment, it has not been confirmed that Opteryx operates as expected on ARM Windows - it does operate on Linux and Mac ARM.

## Setting Up

### 1. Install Python 

**3.11 recommended**

We recommend using [pyenv](https://github.com/pyenv/pyenv) to install and manage Python environments, particularly in development and test environments.

### 2. Install pip   

~~~console
> python -m ensurepip --upgrade
~~~

### 3. Install Git   

Follow the instructions at https://git-scm.com/download/win

### 4. Install Rust

Follow the instructions at https://rustup.rs/

### 5. Clone the Repository   

~~~console
> clone https://github.com/mabel-dev/opteryx
~~~

### 5. Install Dependencies   

~~~console
> python -m pip install --upgrade -r requirements.txt
~~~

~~~console
> python -m pip install --upgrade setuptools setuptools_rust numpy cython
~~~

### 6. Build Binaries   

~~~console
> python setup.py build_ext --inplace
~~~

## Running Tests

To run the regression and unit tests:

First, install the optional dependencies:

~~~console
> python -m pip install --upgrade -r tests/requirements.txt
~~~

Then run the regression tests.

~~~console
> python -m pytest
~~~

!!! note
    Some tests require external services like GCS and Memcached and may fail if these have not been configured.