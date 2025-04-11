class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self.MAX_AGE = 120

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        self._age = max(min(new_age, self.MAX_AGE), 0)

user = User("Jan", 30)
print(f"Poczatkowy wiek: {user.get_age()}")

user.set_age(-5)
print(f"Wiek po ustawieniu nieprawidlowej wartosci: {user.get_age()}")

user.set_age(200)
print(f"Wiek po ustawieniu absurdalnie duzej wartosci: {user.get_age()}")