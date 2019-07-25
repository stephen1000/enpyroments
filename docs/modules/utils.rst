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
of ``sys.path``.


::autoclass:utils.UsePath


Methods
```````

.. method:: UsePath.__init__(path)

    Saves ``path`` to the UsePath instance

.. method:: UsePath.__enter__()

    Appends ``path`` to ``sys.path``, at index 0.

.. method:: UsePath.__exit__()

    Removes the item at ``sys.path``'s index 0 (should be ``path``).


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

.. method:: Sensitive.__init__(obj, stars=10)

    Create a new ``Sensitive`` instance around ``obj``. You may optionally
    pass stars = <int > 0> the number of asterisks to display when
    Settings.masked is invoked (default 10).

.. method:: Sensitive.__str__()

    Returns the wrapped object's ``__str__()``.

.. method:: Sensitive.__repr__()

    Returns "Sensitive :" and the ``__repr__()`` of the wrapped object.

.. method:: Sensitive.mask()

    Returns a string containing a number of asterisks equal to ``stars``
