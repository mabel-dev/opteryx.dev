# Debian/Ubuntu

This guide will help you to set up a Debian or Ubuntu workstation to work with the code and develop Opteryx.

Intel/x86 is the recommended environment, however Opteryx does run on ARM (e.g. a Raspberry Pi) and some parts of the guide may require additional steps in order to work correctly.

## Setting Up

### 1. Install Python 

**3.10 recommended** 

We recommend using [pyenv](https://github.com/pyenv/pyenv) to install and manage Python environments, particularly in development and test environments.

> We follow [this guide](https://www.samwestby.com/tutorials/rpi-pyenv) to set up Python on our Raspberry Pi

### 2. Install pip  

~~~console
$ python3 -m ensurepip --upgrade
~~~

### 3. Install Git   

~~~console
$ sudo apt-get update
~~~

~~~console
$ sudo apt-get install git
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
$ sudo apt-get install python3-dev 
~~~

~~~console
$ python3 -m pip install --upgrade -r requirements.txt
~~~

~~~console
$ python3 -m pip install --upgrade setuptools setuptools_rust numpy cython
~~~

### 7. Build Binaries   

~~~console
$ python3 setup.py build_ext --inplace
~~~

## Running Tests

To run the regression and unit tests:

First, install the optional dependencies, on most devices:

~~~console
$ python3 -m pip install --upgrade -r tests/requirements.txt
~~~

On ARM-based devices (like Raspberry Pi):

~~~console
$ python3 -m pip install --upgrade -r tests/requirements_arm.txt
~~~

Then run the regression tests.

~~~console
$ python3 -m pytest
~~~

!!! note
    Some tests require external services like GCS and Memcached and may fail if these have not been configured.