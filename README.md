# enpyronments

**A Django/Node inspired environment settings library for the Python user on the go.**

---

# <In Development>

Please note that this project is still very much in alpha, so a lot of things will be broken / untested until a more stable build exists.

# Overview

enpyronments is a fully configurable tool for abstracting away the hassle of configuration files.

Here's some use cases:

- Have a separate database address & connection string for dev, test, and prod, with your credentials either stored in an untracked \*\_local.py in settings.DATABASE_ADDRESS and settings.DATABASE_CONNECTION_STRING
- Configure environment variables for both dev and prod servers at startup by calling settings.save_to_environ()
- Have emails deferred or saved as drafts instead of sent while developing and testing based on settings.SEND_MAIL

# Requirements

- Python (3.6, 3.7)

And that's it! No external dependencies!

# Installation

Install using `pip`

    pip install enpyronments

# Example Application

Here is a walkthrough of the provided sample setup for an app with two modes, "dev" and "prod":

    sample_app\
        main.py
        sample_settings\
            env_dev_local.py
            env_dev.py
            env_local.py
            env_prod_local.py
            env_prod.py
            env.py

You'll notice there's 6 different settings files. Here's what each is doing:

- env.py: Default application settings that you track in your repository. Could contain settings like APP_NAME, TARGET_URL, JSON_PAYLOAD, LOGGING_CONFIG, etc.

- env_local.py: Primarily used to determine the local environment's MODE (i.e. if we're running in development, we'd have MODE="dev"). Can be used for sensitive information in apps that don't need different modes, as well. These will override any settings found in env.py

- env_dev.py: Settings for when we're in development mode. We can do things like set SEND_MAIL=False, to indicate that we won't be sending out emails while we're working on the app. These override any settings found in env.py.

- env_dev_local.py: Settings for our local development machine. Things like database connection strings or account credentials can be set here (make sure you don't track these in source control!!!!). If you want to use those settings, but don't want them stored in a file, you can use os.environ to pull them from the operating system's environment variables.

- env_prod.py: Same as env_dev.py, but for production.

- env_prod_local.py: Same as env_dev_local.py, but for production.

In development, our settings will look like:

    {
        "APP_NAME": "enpyronments",
        "LINES_TO_PRINT": 5,
        "MODE": "dev",
        "DEBUG": true,
        "DEBUG_EMAIL_ADDRESS": "foo@bar.baz",
        "WELCOME_MESSAGE": "ayyy whattup",
        "SECRET_KEY": "hey man dont steal my secret key",
        "EMAIL_SERVER_LOGIN": "my_username",
        "EMAIL_SERVER_PASSWORD": "my_password",
        "SECRET_NUMBER": 3
    }

In production, we'd have:

    {
        "APP_NAME": "enpyronments",
        "LINES_TO_PRINT": 20,
        "MODE": "prod",
        "WELCOME_MESSAGE": "Welcome to Jurrasic Park!",
        "SECRET_KEY": "SUPREMELY SECRET- DO NOT SHARE!!!",
        "EMAIL_SERVER_LOGIN": "resource_account_user",
        "EMAIL_SERVER_PASSWORD": "resource_account_password"
    }

And we can access those in the code in just a few lines:

```python
app_dir = "sample_app"
settings_dir = "sample_settings"
root = os.path.join(os.path.dirname(__file__), app_dir)

loader = Loader(root)
settings = loader.load_settings(settings_dir)
```

# Usage Explanation

Let's say we're making an ultra-complex application that needs to print a message a certain number of times, depending on who / where our app is running. Let's say it looks something like this:

```python
# main.py

from . import settings

def main():
    for _ in range settings.LINES_TO_PRINT:
        print(settings.MESSAGE)


if __name__ == '__main__':
    main()
```

And next to it, the configuration:

```python
# settings.py

LINES_TO_PRINT = 10
MESSAGE = 'test message please ignore'
```

Seems straightforward enough, right? We can just have our app import those settings from a .py file right next to it, and poof, problem solved!

Now, let's say that we've deployed this code to our production machine, and it's running just great. Our customers are happy*ish*, but a few of them would happier if the message had a date attached to it.

We can instruct them to change their settings file like so:

```python
# settings.py

import datetime as dt

LINES_TO_PRINT = 10
MESSAGE =  f'{dt.date.today():%x}: test message please ignore'
```

Ok, that's easy enough, but now we've got two different versions of our settings.py file. How do we choose which one should be in our repository?

That's where enpyronments comes in. We'll get started by creating a folder for all of our different settings to go in to. Where you place the folder is up to you, but next to the code, in the same repository is a good idea.

So our new setup looks like this:

    src\
        main.py
    configuration\
        env.py
        env_local.py

Our default settings would go into env.py:

```python
# configuration\env.py

LINES_TO_PRINT = 10
MESSAGE = 'test message please ignore'
```

And our users would just have to modify the env_local.py file to change the settings they want to override:

```python
# configuration\env_local.py

import datetime as dt

MESSAGE =  f'{dt.date.today():%x}: test message please ignore'
```

Or, even better, you can import the default setting and change it for your local environment:

```python
# configuration\env_local.py

import datetime as dt

from . import env

MESSAGE =  f'{dt.datetime.today():%x}: {env.MESSAGE}'
```

We can load those into our app with enpyronments:

```python
# src\main.py

from enpyronments.loader import Loader

loader = Loader('path/to/parent/dir')
settings = Loader.load_settings('configuration')

for _ in range(settings.LINES_TO_PRINT):
    print(settings.MESSAGE)
```

That's all fine and dandy, but maybe you want to pull a message from an external source using something like requests. That's pretty easily done:

```python
# configuration\env.py

import requests

response = requests.get('https://xkcd.com/info.0.json')
data = response.content
comic_title = data.get('title')

if comic_title:
    MESSAGE = f"Today's xkcd is called '{comic_title}'"
else:
    MESSAGE = f"Sorry, we couldn't load the title of today's xkcd :("
```

And lastly (or more likely beforehand), you'll probably want to make sure you don't track the localized settings in your repository, so add them to your .gitignore:

```
# .gitignore

configuration\*_local.py
```

# Further reading

I'm working on it! Check back here for a link to wherever the full documentation lands.
