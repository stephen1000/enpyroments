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

    2. Set an environment variable in your terminal (varies by Operating system
    ), then access via :py:attr:`os.environ`:

..code-block:: python

    # env.py
    
    import os

    USERNAME = os.environ['USERNAME']
    PASSWORD = os.environ['PASSWORD']
    
Both of these approaches have some downsides, so enpyronments gives you a third
way to handle it- local files.

Local settings files are settings files whose names end with '_local'. You
should set up a rule in your source control to ignore them (i.e. in .gitignore
add a line "settings/*_local.py). Since you're not tracking them (or deploying
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
which we'll want to showing on error pages, or saving in logs (even in dev!)

To deal with this, we can use :py:class:`utils.Sensitive`. To use in code,
simply wrap your secret information in the 
