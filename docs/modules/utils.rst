.. module:: utils
    :synopsis: Helper functions

.. **Source code:** :source:`enpyronments/utils.py`


The utils module
================

The utils module contains some classes that aren't complex enough to warrent
their own module, and aren't tightly coupled with another class. There are
currently 2 classes:

    * `UsePath`_: A context manager for temporarilly adding a path to sys.path

    * `Sensitive`_: A wrapper class used to provide masking to individual
        settings

UsePath
-------

``UsePath`` is a Context Manager that temporarilly places a path at the start
of ``sys.path``. For example:

.. code-block:: python

    from enpyronments.utils import UsePath

    # Let's pick a path to a module that isn't already on sys.path
    module_path = 'path/to/some/module'


    # Right now, module_path isn't on sys.path

    with UsePath(module_path):
        # Here, module_path is the first item on sys.path
        import module_name as cool_module

    # And now, module_path is no long on sys.path

Used to import settings modules without affecting anything that runs after.

Methods
```````

.. autoclass:: enpyronments.utils.UsePath
    :members: __init__, __enter__, __exit__

Sensitive
---------

``Sensitive`` is a wrapper class that can be used to flag a setting in a python
settings file as a sensitive value. Accessing the value from the Settings dict
normally will retrieve the underlying value, but invoking Settings.masked()
will replace the value of the setting with asterisks, allowing easy dumping of
masked data to logs.

For example, let's say we have an env_local.py file with the following
settings provided:

.. code-block:: python

    # env_local.py

    MODE = 'dev'
    APIKEY = 'abc123pleasedonttrackme'

If we wanted our application to print a readout of all of our settings, by say
calling ``json.dumps``, we'd be exposing our Api key in the dump:

>>> json.dumps(settings)
{'MODE': 'dev', 'APIKEY': 'abc123pleasedonttrackme'}

To avoid this, while still being able to easily print out the current settings,
we can use Sensitive:

.. code-block:: python

    # env_local.py

    from enpyronments.utils import Sensitive

    MODE = 'dev'
    APIKEY = Sensitive('abc123pleasedonttrackme')

And now, we can safely print our settings via settings.masked():

>>> json.dumps(settings.masked())
{'MODE': 'dev', 'APIKEY': '**********'}

Methods
```````

.. autoclass:: enpyronments.utils.Sensitive
    :members: mask, __init__, __str__, __repr__

