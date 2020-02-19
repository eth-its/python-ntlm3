python-ntlm3
============

This is a Python 3 compatible fork of the [python-ntlm](https://code.google.com/p/python-ntlm) project. 

About this library
------------------

This library handles the low-level details of NTLM authentication. Almost all users should use [requests-ntlm](https://github.com/requests/requests-ntlm) instead, which is a plugin to requests that uses this library under the hood and is way easier to use and understand. 

Installation
------------

python-ntlm3 supports Python 2.6, 2.7 and 3.3+ 

To install, use pip:

    pip install python-ntlm3

To install from source, download the source code, then run:

    python setup.py install
    
Usage
------------

This library has an identical API as python-ntlm and is a drop-in replacement. To use, include this:

    import ntlm3 as ntlm

API
----------

TODO
