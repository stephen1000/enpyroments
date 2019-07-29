==========
Quickstart
==========

A brief introduction to enpyronments. For a more in-depth explanation of the
various features, check out the tutorial or Api reference.

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

Using the environment
---------------------

If you want to pull settings from environment variables, you can use
:py:attr:`os.environ` to grab the settings you need:

.. code-block:: python

    import os

    DEBUG = os.environ['DEBUG']

If you want to run a script (say, a flask app) with these settings as
environment variables, it's as easy as calling a function before you
initialize your application:

>>> settings.save_to_envrion()


Hiding sensitive values
-----------------------

When debugging your application, it's often helpful to see the configuration
settings used in a particular run, whether it's on an error screen, log file,
or just the terminal you're running your script in. If you just dump your
current settings, though, you'll run the risk of exposing sensitive information
:

>>> print(settings)
{'APIKEY':'JUC32I3efjihz', 'BANK_PASSWORD':'dollarDollarBills', 'LUNCH_ORDER':'
a disturbingly large number of tacos'}

To avoid this, enpyronments provides you with an easy-to-use wrapper class and
a method to mask your settings:

.. code-block:: python

    # env.py
    from enpyronments.utils import Sensitive

    # hide the secrets
    APIKEY = Sensitive('JUC32I3efjihz')
    BANK_PASSWORD = Sensitive('dollarDollarBills')

    # leave the rest as is
    LUNCH_ORDER = 'a disturbingly large number of tacos'

Now, you can dump your configuration using ``Settings.masked()``:

>>> print(settings.masked())
{'APIKEY':'********** 'BANK_PASSWORD':'**********',', 'LUNCH_ORDER':'a
disturbingly large number of tacos'}

.. note:
    You really shouldn't be storing sensitive information on files tracked by
    your source control- anyone who can see your code can see your data!
    Instead, check out the section on `Local settings <local_settings.html>`

For more on this, see  :py:attr:`enpyronments.utils.Sensitive`.

Next topics
-----------

That should get you started! For more advanced topics, check the tutorial.
