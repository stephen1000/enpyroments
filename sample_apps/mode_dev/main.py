import json
import logging
import os
import sys

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
logger.addHandler(logging.StreamHandler())

# fix to have app work w/o enpyronments installed
try:
    from enpyronments.loader import Loader
except ImportError:
    sys.path.append(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    )
    from enpyronments.loader import Loader


def get_settings():
    root = os.path.dirname(os.path.abspath(__file__))
    settings_dir = "sample_settings"

    settings = Loader(root).load_settings(settings_dir)

    return settings


def main():
    settings = get_settings()
    logger.info('Running app "%s"', settings.app_name)
    if settings.debug:
        logger.info("---DEBUG MODE---")
    
    for _ in range(settings.lines_to_print):
        logger.info(settings.welcome_message)

    logger.debug('Settings (masked): %s', json.dumps(settings.masked()))


if __name__ == "__main__":
    main()
