class InvalidPinException(Exception):
    pass


class InsufficientFundsException(Exception):
    pass


class ATM:
    def __init__(self):
        self.accounts = {
            1234: 1000.0,
            5678: 2500.0,
        }

    def _validate_pin(self, pin: int) -> None:
        if pin not in self.accounts:
            raise InvalidPinException("Nieprawidłowy PIN.")

    def check_balance(self, pin: int) -> float:
        self._validate_pin(pin)
        return self.accounts[pin]

    def deposit(self, pin: int, amount: float) -> float:
        self._validate_pin(pin)

        if amount <= 0:
            raise ValueError("Kwota wpłaty musi być większa od zera.")

        self.accounts[pin] += amount
        return self.accounts[pin]

    def withdraw(self, pin: int, amount: float) -> float:
        self._validate_pin(pin)

        if amount <= 0:
            raise ValueError("Kwota wypłaty musi być większa od zera.")

        if self.accounts[pin] < amount:
            raise InsufficientFundsException("Niewystarczające środki na koncie.")

        self.accounts[pin] -= amount
        return self.accounts[pin]