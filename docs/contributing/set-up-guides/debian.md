# Debian/Ubuntu

This guide will help you to set up a Debian or Ubuntu workstation to work with the code and develop Opteryx.

Intel/x86 is the recommended environment, however Opteryx does run on ARM and some parts of the guide may require additional steps in order to work correctly.

## Setting Up

### 1. Install Python 

**3.10 recommended** 

We recommmend using [pyenv](https://github.com/pyenv/pyenv) to install and manage Python environments, particularly in development and test environments.

### 2. Install pip   

~~~bash
python3 -m ensurepip --upgrade
~~~

### 3. Install Git   

~~~bash
sudo apt-get update
~~~

~~~bash
sudo apt-get install git
~~~

### 4. Install Rust

~~~bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
~~~

### 5. Clone the Repository   

~~~bash
git clone https://github.com/mabel-dev/opteryx
~~~

### 6. Install Dependencies   

~~~bash
python -m pip install --upgrade -r requirements.txt
~~~

~~~bash
python3 -m pip install --upgrade setuptools setuptools_rust
~~~

### 7. Build Binaries   

~~~bash
python3 setup.py build_ext --inplace
~~~

## Running Tests

To run the regression and unit tests:

First, install the optional dependencies, on most devices:

~~~bash
python3 -m pip install --upgrade -r tests/requirements.txt
~~~

On ARM-based devices (like Raspberry Pi):

~~~bash
python3 -m pip install --upgrade -r tests/requirements_arm.txt
~~~

Then run the regression tests.

~~~
python3 -m pytest
~~~

!!! note
    Some tests require external services like GCS and Memcached and may fail if these have not been configured.