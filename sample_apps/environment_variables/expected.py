import os

eviron_debug = os.environ.get("DEBUG")
if eviron_debug is not None:
    DEBUG = eviron_debug
else:
    DEBUG = True

settings = {
    "DEBUG": DEBUG,
    "APP_NAME": "enpyronments",
    "WELCOME_MESSAGE": "Welcome to enpyronments!",
    "LINES_TO_PRINT": 10,
}
