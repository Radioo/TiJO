from register_form_fields import RegisterFormFields
from validator import Validator


class PeselValidator(Validator):
    def __init__(self, pesel):
        self.pesel = pesel

    def is_valid(self):
        if self.pesel is None or self.pesel.strip() == "":
            return False

        if len(self.pesel) != 11 or not self.pesel.isdigit():
            return False

        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
        check_sum = sum(int(self.pesel[i]) * weights[i] for i in range(11))

        return check_sum % 10 == 0

    def field_name(self):
        return RegisterFormFields.PESEL