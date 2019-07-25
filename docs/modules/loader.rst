.. module:: loader
    :synopsis: The settings loader

The loader module
=================

The module for holding the :class:`Loader` class.

Loader
------

The settings loader class. Responsible for importing settings files and
the module resolution order.

Methods
```````

The following settings are provided at the module level as defaults, and can
be overridden on initilization of :class:`Loader`.

.. code-block:: python

    default_prefix = "env"
    default_ext = ".py"
    default_sep = "_"
    default_builtin_pattern = r"^__(.+)__$"
    default_attribute_pattern = r"^[A-Z_0-9]+$"

.. autoclass:: enpyronments.loader.Loader
    :members:
