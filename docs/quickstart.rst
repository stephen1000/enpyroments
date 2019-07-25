==========
Quickstart
==========




------------
Requirements
------------
Python 3.6, 3.7+

-------
Install
-------
> pip install enpyronments

-----
Usage
-----

Within your application, create a folder to hold your settings files (for this
example, let's call it "settings").

In settings, create a file for your default settings (these are the values
that will be used unless you explicitly overwrite them in another file).

    settings/env.py

    DEBUG = False
    SEND_TO = ['myemail@mydomain.com']