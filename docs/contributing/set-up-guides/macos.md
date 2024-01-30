# MacOS Setup Guide

This guide will help you set up a macOS workstation to work with the code and develop Opteryx.

Both Intel/x86 and ARM environments are supported, but some parts of the guide may require additional steps for ARM.

## Setting Up

### 1. Install Python

**Python 3.11 recommended**

We recommend using [pyenv](https://github.com/pyenv/pyenv) to install and manage Python environments. Follow the pyenv installation instructions for macOS.

### 2. Install pip

~~~console
$ python -m ensurepip --upgrade
~~~

### 3. Install Git   

First, update Homebrew:

~~~console
$ brew update
~~~

Then, install Git:

~~~console
$ brew install git
~~~

### 4. Install Rust

~~~console
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
~~~

### 5. Clone the Repository    

~~~console
$ git clone https://github.com/mabel-dev/opteryx
~~~

### 6. Install Dependencies   

~~~console
$ python -m pip install --upgrade -r requirements.txt
~~~

~~~console
$ python -m pip install --upgrade setuptools setuptools_rust numpy cython
~~~

### 7. Build Binaries   

~~~console
$ python setup.py build_ext --inplace
~~~

## Running Tests

To run the regression and unit tests:

First, install the optional dependencies, on intel-based Macs:

~~~console
$ python -m pip install --upgrade -r tests/requirements.txt
~~~

On M-series (ARM) CPU Macs:

~~~console
$ python -m pip install --upgrade -r tests/requirements_arm.txt
~~~

Then run the regression tests.

~~~console
$ python -m pytest
~~~

!!! note
    Some tests require external services like GCS and Memcached and may fail if these have not been configured.