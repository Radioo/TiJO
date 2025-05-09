from register_form_fields import RegisterFormFields
from validator import Validator

class PasswordValidator(Validator):
    def __init__(self, password):
        self.password = password
        self.special_chars = "!@#$%^&*()_+-="
        self.min_length = 4

    def is_valid(self):
        if self.password is None or self.password == "":
            return False

        if len(self.password) < self.min_length:
            return False

        if not any(char.isdigit() for char in self.password):
            return False

        if not any(char.isupper() for char in self.password):
            return False

        if not any(char.islower() for char in self.password):
            return False

        if not any(char in self.special_chars for char in self.password):
            return False

        return True

    def field_name(self):
        return RegisterFormFields.PASSWORD