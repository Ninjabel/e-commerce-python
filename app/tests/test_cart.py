import unittest
from app.models.cart import Cart


class TestCartRoutes(unittest.TestCase):

    def setUp(self):
        """Runs before each test"""
        self.cart = Cart(user_id=1)
        self.cart.clear_cart()

    def test_add_product(self):
        """Test adding a product to the cart"""
        self.cart.add_product(101, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]['quantity'], 2)

    def test_remove_product(self):
        """Test removing a product from the cart"""
        self.cart.add_product(101, 2)
        self.cart.remove_product(101)
        self.assertEqual(len(self.cart.items), 0)

    def test_clear_cart(self):
        """Test clearing the cart"""
        self.cart.add_product(101, 2)
        self.cart.clear_cart()
        self.assertEqual(len(self.cart.items), 0)

    def test_get_cart_details(self):
        """Test retrieving the cart details"""
        self.cart.add_product(101, 2)
        details = self.cart.get_cart_details()
        self.assertEqual(details['user_id'], 1)
        self.assertEqual(len(details['items']), 1)


if __name__ == '__main__':
    unittest.main()
