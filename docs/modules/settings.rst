.. module:: settings
    :synopsis: Settings holder class

.. **Source code:** :source:`enpyronments/settings.py`


The settings module
===================

The settings module serves one purpose- defining :class:`Settings`. Settings
isn't meant to be constructed outside of `The loader module <loader.html>`_,
but its members are documented here anyways.

Settings
--------

A dict-like class (inherits from :py:class:`collections.abc.MutableMapping`)
for storage of configuration settings.

.. autoclass:: enpyronments.settings.Settings
    :members:
