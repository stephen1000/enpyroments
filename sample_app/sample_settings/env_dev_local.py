from enpyronments.utils import Sensitive

SECRET_KEY = Sensitive("hey man dont steal my secret key")

EMAIL_SERVER_LOGIN = "my_username"
EMAIL_SERVER_PASSWORD = Sensitive("my_password")

SECRET_NUMBER = Sensitive(3)
