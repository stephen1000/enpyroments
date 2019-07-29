from enpyronments.utils import Sensitive

# Override a default setting
LINES_TO_PRINT = 5
# Enable masking on welcome message
WELCOME_MESSAGE = Sensitive('secret message!')
