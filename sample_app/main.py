import os
import sys

try:
    from enpyronments.loader import Loader
except ImportError:
    sys.path.append(
        os.path.dirname(os.path.dirname(__file__))
    )
    from enpyronments.loader import Loader


root = os.path.dirname(os.path.abspath(__file__))
settings_dir = 'sample_settings'

settings = Loader(root).load_settings(settings_dir)

if settings.DEBUG:
    print('---DEBUG MODE---')
    print(settings.WELCOME_MESSAGE)
else:
    print(settings.WELCOME_MESSAGE)
