import os

from enpyronments.loader import Loader

root = os.path.dirname(os.path.abspath(__file__))
settings_dir = 'sample_settings'

settings = Loader(root).load_settings(settings_dir)

if settings.DEBUG:
    print('---DEBUG MODE---')
    print(settings.MESSAGE)
else:
    print(settings.MESSAGE)
