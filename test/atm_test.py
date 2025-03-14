import unittest

from src.atm import ATM, InvalidPinException, InsufficientFundsException


class ATMTest(unittest.TestCase):
    def setUp(self):
        self.atm = ATM()

    def test_check_balance(self):
        self.assertEqual(self.atm.check_balance(1234), 1000)

    def test_check_balance_invalid_pin(self):
        with self.assertRaisesRegex(InvalidPinException, "Nieprawidłowy PIN."):
            self.atm.check_balance(9999)

    def test_deposit_amount_less_than_zero(self):
        with self.assertRaisesRegex(ValueError, "Kwota wpłaty musi być większa od zera."):
            self.atm.deposit(1234, -100)

    def test_deposit_valid_amount(self):
        self.assertEqual(self.atm.deposit(1234, 100), 1100)

    def test_withdraw_amount_less_than_zero(self):
        with self.assertRaisesRegex(ValueError, "Kwota wypłaty musi być większa od zera."):
            self.atm.withdraw(1234, -100)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaisesRegex(InsufficientFundsException, "Niewystarczające środki na koncie."):
            self.atm.withdraw(1234, 10000)

    def test_withdraw_valid_amount(self):
        self.assertEqual(self.atm.withdraw(1234, 100), 900)

if __name__ == '__main__':
    unittest.main()