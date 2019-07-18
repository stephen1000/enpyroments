# Enpyroments

**A Django/Node inspired environment settings library for the Python user on the go.**

---

# Overview

Enpyroments is a fully configurable tool for abstracting away the hassle of configuration files.

Here's some use cases:

- Have a separate database & connection string for dev, test, and prod, with your credentials either stored in an untracked \*\_local.py file or pulled from the current environment
-

# Requirements

- Python (3.6, 3.7)

And that's it! No external dependencies!

# Installation

Install using `pip` (eventually.....)

    pip install enpyroments

# Example

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

That's where enpyroments comes in. We'll get started by creating a folder for all of our different settings to go in to. Where you place the folder is up to you, but next to the code, in the same repository is a good idea.

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

MESSAGE =  f'{dt.date.today():%x}: test message please ignore'
```

Or, even better, you can import the default setting and change it for your local environment:

```python
# configuration\env_local.py

import datetime as dt

from . import env

MESSAGE =  f'{dt.datetime.today():%x}: {env.MESSAGE}'
```

We can load those into our app with enpyroments:

```python
# src\main.py

from enpyroments.loader import Loader

loader = Loader('path/to/parent/dir')
settings = Loader.load_settings('configuration')

for _ in range(settings.LINES_TO_PRINT):
    print(MESSAGE)
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
    MESSAGE = f"Sorry, we couldn't load the comic :("
```

And lastly (or more likely beforehand), you'll probably want to make sure you don't track the localized settings in your repository, so add them to your .gitignore:

```
# .gitignore

configuration\*_local.py
```

# Further reading

I'm working on it! Check back here for a link to wherever the full documentation lands.
