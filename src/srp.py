class Order:
    def __init__(self, id, items, customer):
        self.id = id
        self.items = items
        self.customer = customer


class OrderValidator:
    def validate(self, order):
        print("Walidacja zamowienia.")


class OrderRepository:
    def save(self, order):
        print("Zapisywanie zamowienia do bazy danych.")


class OrderNotifier:
    def send_confirmation(self, order):
        print("Wysylanie e-maila potwierdzajacego.")


class OrderProcessor:
    def __init__(self, order, validator, repository, notifier):
        self.order = order
        self.validator = validator
        self.repository = repository
        self.notifier = notifier

    def process_order(self):
        self.validator.validate(self.order)
        self.repository.save(self.order)
        self.notifier.send_confirmation(self.order)


order = Order("123", ["Produkt A", "Produkt B"], "Jan Kowalski")
validator = OrderValidator()
repository = OrderRepository()
notifier = OrderNotifier()
processor = OrderProcessor(order, validator, repository, notifier)
processor.process_order()