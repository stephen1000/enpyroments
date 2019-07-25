==========
Quickstart
==========

<ref here>

Requirements
------------

Python 3.6, 3.7+

Install
-------

Install using pip:

.. code-block::

    pip install enpyronments

.. note::

    enpyronments is still very much in alpha, so be sure you're getting the
    most recent version when upgrading (pip won't grab the most recent alpha
    unless you specifiy the version number).

Usage
-----

Within your application, create a folder to hold your settings files (for this
example, let's call it "settings").

In settings, create a file for your default settings (these are the values
that will be used unless you explicitly overwrite them in another file).

.. code-block:: python

    # settings/env.py

    DEBUG = False
    TARGET_URL = 'https://xkcd.com/info.0.json'

Now, in your main script:

.. code-block:: python

    # main.py

    from enpyronments.loader import Loader

    # if your project has a static root folder:
    root = 'path/to/project/folder/'

    # you can also determine this programatically in script files by using the
    # python builtin variable "__file__" (see the python docs for more on this)
    #
    # import os
    #
    # root = os.path.dirname(os.path.abspath(__file__))

    loader = Loader(root)
    settings = Loader.load_settings('settings')


All the settings defined in env.py that look like constants (UPPER_CASE) are
available as attributes of ``settings``:

>>> settings.DEBUG
False

You can also use the lower case equivalent to access a setting:

>>> settings.target_url
'https://xkcd.com/info.0.json'

That should get you started! For more advanced topics, check the tutorial.
