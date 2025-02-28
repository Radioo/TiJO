import unittest

from src.shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_product(self):
        result = self.cart.add_product("apple", 100, 2)
        self.assertTrue(result)
        self.assertIn("apple", self.cart.get_products())

    def test_remove_product(self):
        self.cart.add_product("apple", 100, 2)
        result = self.cart.remove_product("apple")
        self.assertTrue(result)
        self.assertNotIn("apple", self.cart.get_products())

    def test_remove_nonexistent_product(self):
        result = self.cart.remove_product("banana")
        self.assertFalse(result)

    def test_update_quantity(self):
        self.cart.add_product("apple", 100, 2)
        result = self.cart.update_quantity("apple", 5)
        self.assertTrue(result)
        self.assertEqual(self.cart.products["apple"]["quantity"], 5)

    def test_update_nonexistent_product(self):
        result = self.cart.update_quantity("banana", 3)
        self.assertFalse(result)

    def test_get_products(self):
        self.cart.add_product("apple", 100, 2)
        self.cart.add_product("banana", 50, 3)
        products = self.cart.get_products()
        self.assertEqual(len(products), 2)
        self.assertIn("apple", products)
        self.assertIn("banana", products)

    def test_count_products(self):
        self.cart.add_product("apple", 100, 2)
        self.cart.add_product("banana", 50, 3)
        self.assertEqual(self.cart.count_products(), 2)

    def test_get_total_price(self):
        self.cart.add_product("apple", 100, 2)
        self.cart.add_product("banana", 50, 3)
        self.assertEqual(self.cart.get_total_price(), 350)

    def test_apply_valid_discount_code(self):
        self.cart.add_product("apple", 100, 2)
        result = self.cart.apply_discount_code("DISCOUNT10")
        self.assertTrue(result)
        self.assertEqual(self.cart.get_total_price(), 180)

    def test_apply_invalid_discount_code(self):
        self.cart.add_product("apple", 100, 2)
        result = self.cart.apply_discount_code("INVALID")
        self.assertFalse(result)
        self.assertEqual(self.cart.get_total_price(), 200)

    def test_checkout_with_products(self):
        self.cart.add_product("apple", 100, 2)
        result = self.cart.checkout()
        self.assertTrue(result)
        self.assertEqual(len(self.cart.products), 0)

    def test_checkout_without_products(self):
        result = self.cart.checkout()
        self.assertFalse(result)

    def tearDown(self):
        self.cart = None