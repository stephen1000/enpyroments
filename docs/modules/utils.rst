================
The utils module
================


The utils module contains some classes that aren't complex enough to warrent
their own module, and aren't tightly coupled with another class. There are
currently 2 classes:

    * [UsePath]_: A context manager for temporarilly adding a path to sys.path
    .. [UsePath] utils.UsePath
    * [Sensitive]_: A wrapper class used to provide masking to individual settings
    .. [Sensitive] utils.Sensitive

-------
UsePath
-------

UsePath is a Context Manager that 