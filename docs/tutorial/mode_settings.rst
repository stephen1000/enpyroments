Mode based settings
===================


When working on an application, it's often useful to change some behavior
depending on what environment you're working in. For example, you might have
a Django app with a separate database for development and production:

.. code-block:: python

    # settings.py

    if DEBUG:
        DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
    else:
        DATABASES = {
            # ... some other database ...
        }

This pattern gets out of hand rather quickly, especially as you begin to add
more settings / modes:

.. code-block:: python

    # settings.py

    DEBUG = True # !~Important- change this in prod!!!!
    SEND_MAIL = not (DEBUG or TEST_MODE)
    USE_HTTPS = not DEBUG

    if DEBUG:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
    elif TEST_MODE:
        DATABASES = {
            # ... some other database ...
        }
    else:
        DATABASES = {
            # ... some other database ...
        }


Creating modes
--------------

enpyronments comes with strong support for choosing between any number of modes
. To create a new mode, just create a file named env_modename.py.

Let's modify the above to use enpyronments to manage mode state.

In env.py, we'll leave a placeholder value that we'll overwrite (Not necessary,
but it makes your configuration a bit easier to read):

.. code-block:: python

    # settings/env.py

    DEBUG = None
    SEND_MAIL = None
    USE_HTTPS = None
    DATABASES = None

In env_dev.py, we just need to define the database for dev mode:

.. code-block:: python

    # settings/env_dev.py

    DEBUG = True
    SEND_MAIL = False
    USE_HTTPS = False

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

In env_test.py, we do the same, but for test:

.. code-block:: python

    # settings/env_test.py

    DEBUG = True
    SEND_MAIL = False
    USE_HTTPS = True

    DATABASES = {
        # ... settings for test database ...
    }

And in env_prod.py, the same:

.. code-block:: python

    # settings/env_prod.py

    DEBUG = False
    SEND_MAIL = True
    USE_HTTPS = True

    DATABASES = {
        # ... settings for test database ...
    }

And lastly, we'll add a local file to indicate what mode we're actually in (
we're using a local file so we don't track it in our source control):

.. code-block:: python

    # settings/env_local.py

    MODE = 'dev'

Now when we load our settings, we get:

>>> print(settings)
{'DEBUG': True, 'SEND_MAIL': False, 'USE_HTTPS': False, ...}


Overriding mode-specific settings
---------------------------------

When loading a particular mode configuration, it may become necessary to pull
in some settings we don't want to track, but also need to change based on mode.
enpyronments supports this, too, by using mode_local files:

.. code-blocK:: python

    # settings/env_dev_local.py

    USERNAME = 'my_username'
    PASSWORD = 'my_password'

    # settings/env_prod_local.py

    USERNAME = 'my_other_username'
    PASSWORD = 'my_other_password'

.. note::
    Be sure not to print or log your settings directly if you're doing this-
    see ``Masking sensitive information``.

You can have any number of modes, but only one mode can be active at a given
time. enpyronments will load settings with the following priority:

    1. Mode local settings (env_dev_local.py, env_prod_local.py, etc.)
    2. Mode settings (env_dev.py, env_prod.py, etc.)
    3. Local settings (env_local.py)
    4. Default settings (env.py)
