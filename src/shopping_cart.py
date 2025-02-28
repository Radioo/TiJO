class ShoppingCart:
    def __init__(self):
        self.products = {}

    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
        if not hasattr(self, 'products'):
            self.products = {}
        self.products[product_name] = {'price': price, 'quantity': quantity}
        return True

    def remove_product(self, product_name: str) -> bool:
        if product_name in self.products:
            del self.products[product_name]
            return True
        return False

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        if product_name in self.products:
            self.products[product_name]['quantity'] = new_quantity
            return True
        return False

    def get_products(self):
        return list(self.products.keys())

    def count_products(self) -> int:
        return len(self.products)

    def get_total_price(self) -> int:
        return sum(item['price'] * item['quantity'] for item in self.products.values())

    def apply_discount_code(self, discount_code: str) -> bool:
        if discount_code == "DISCOUNT10":
            for item in self.products.values():
                item['price'] *= 0.9
            return True
        return False

    def checkout(self) -> bool:
        if not self.products:
            return False
        self.products.clear()
        return True