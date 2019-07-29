import os

eviron_debug = os.environ.get('DEBUG')
if eviron_debug is not None:
    DEBUG = eviron_debug
else:
    DEBUG = True

APP_NAME = "enpyronments"

WELCOME_MESSAGE = 'Welcome to enpyronments!'
LINES_TO_PRINT = 10

shouldnt_load_as_setting = "hey im just here for the show!"
