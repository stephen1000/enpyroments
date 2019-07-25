.. enpyronments documentation master file, created by
   sphinx-quickstart on Wed Jul 24 13:49:53 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to enpyronments's documentation!
========================================

.. toctree::
    :maxdepth: 2

    About <about>
    Quickstart <quickstart>
    Tutorial <tutorial>
    Api reference (modules) <modules>

Overview
========

enpyronments is a settings configuration library that seeks to provide a
simple way to configure your application for whatever environment you're in.

To get started ASAP, check out `Quickstart`. To get a more detailed overview
of enpyronments' features, start at the `Tutorial`.


Features
========

enpyronments currently provides the following features for loading from a
configuration folder:

    * `Untracked (local) settings`
    * `Mode based settings`
    * `Dot accessors`
    * `Sensitive setting masking`
    * `Load to environment variables`


Roadmap
=======

Roughly in order-

    * More and better tests
    * LocalOnly object (for indicating that a setting must be provided locally)
    * Tox testing
    * CLI configuration interface (add/change/remove settings/files)
    * More settings destinations (JSON, new .py file, etc.)
    * More source options (JSON, python dict's)
    * Namespace unpacking object (for more modular .py files)
    * Django Plugin + Management commands (wrapping the above CLI)


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
