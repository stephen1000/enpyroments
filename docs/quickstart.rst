==========
Quickstart
==========

<ref here>

Requirements
------------

Python 3.6, 3.7+

Install
-------

> pip install enpyronments

Usage
-----

Within your application, create a folder to hold your settings files (for this
example, let's call it "settings").

In settings, create a file for your default settings (these are the values
that will be used unless you explicitly overwrite them in another file).

-- code-block:: python

    # settings/env.py

    DEBUG = False
    TARGET_URL = 'https://xkcd.com/info.0.json'

Next, add settings\*_local.py to your .gitignore. In settings, create a
env_local.py file:

-- code-block:: python

    # settings/env_local.py

    MODE = 'dev'

Now,

