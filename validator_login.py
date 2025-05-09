from re import *
from validator import Validator
from register_form_fields import RegisterFormFields

class LoginValidator(Validator):
    def __init__(self, login):
        self.login = login
        self.LOGIN_MIN_LENGTH = 4

    def is_valid(self):
        if self.login is None or self.login.strip() == "":
            return False

        if len(self.login) < self.LOGIN_MIN_LENGTH:
            return False

        if not match(r"^[a-zA-Z0-9_.-]+$", self.login):
            return False

        return True

    def field_name(self):
        return RegisterFormFields.LOGIN