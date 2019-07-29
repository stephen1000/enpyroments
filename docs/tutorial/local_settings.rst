Untracked (local) settings
==========================

So, you've gotten your env.py set up with the settings you want to load. You're
able to read your configuration and use it in your application. Everything is
fine *until* we need to use a setting that we *really* don't want to track in
our source control repository.

For instance, assume we need to add a feature to send an email from our mail
server. We need to tell the mail server what our username and password are, but
we shouldn't keep that in our code (as much as we can help it- more on that
later).

Without making our settings any more complicated, we can solve for this a in a
couple ways-

    1. Use a prompt to take input on the command line whenver we run the app:

.. code-block:: python

    # env.py

    USERNAME = input('Username: ')
    PASSWORD = input('Password: ')

    2. Set an environment variable in your terminal (varies by Operating
    system), then access via :py:attr:`os.environ`:

.. code-block:: python

    # env.py

    import os

    USERNAME = os.environ['USERNAME']
    PASSWORD = os.environ['PASSWORD']

Both of these approaches have some downsides, so enpyronments gives you a third
way to handle it- local files.

Settings files are local settings files if their names end with 'local'. You
should set up a rule in your source control to ignore them (i.e. in .gitignore
add a line "settings/\*_local.py). Since you're not tracking them (or deploying
them to any servers), you can put whatever you want in there. enpyronments
automatically looks for local files and will use settings defined there instead
of settings in env.py.

Here's an example of a local file in action:

.. code-block:: python

    # env_local.py

    USERNAME = 'my_username'
    PASSSWORD = 'my_password'

The settings for USERNAME and PASSWORD will be available in settings-

>>>> print(settings.USERNAME)
'my_username'

>>> print(settings.PASSSWORD)
'my_password'

Masking sensitive information
-----------------------------

So in our last example, when we were checking the values of our settings, we
printed them straight to the console. That works while our script is relatively
small, but as our project grows, we're going to have more settings, some of
which we'll want to show on error pages, or save in logs (even in dev!)

To deal with this, we can use :py:class:`utils.Sensitive`. To use it, wrap your
secret information in :py:class:`utils.Sensitive` when you define a setting.
You'll still be able to access the value as if it were defined without the
wrapper class, but behind the scenes enpyronments is checking to see which
values Sensitive when retrieved:

.. code-block:: python

    # env_local.py
    from enpyronments.utils import Sensisitive

    USERNAME = 'my_username'
    PASSSWORD = Sensisitive('my_password')

When printing settings, invoke the :py:meth:`masked` method to get a dict with
all sensitive values masked:

>>> print(settings.masked())
{'USERNAME': 'my_username', 'PASSWORD': '**********'}

And that's it!

.. note::

    By design, accessing values from a settings object directly will always
    return the underlying value, not a masked value. This is to ensure that
    using the Settings class is just like accessing items in a dictionary or
    namespace. **If you are displaying the values of settings, use masked()!**
    If you print a Settings object directly, the values will be printed as they
    are defined, whether they are marked as Sensitive or not.
