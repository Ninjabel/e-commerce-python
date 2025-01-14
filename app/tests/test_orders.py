import unittest
from app import create_app
from app.models.order import Order

class TestOrder(unittest.TestCase):

    def setUp(self):
        """Prepare data for testing before each test"""
        self.app = create_app()
        self.client = self.app.test_client()
        Order.orders_db = []  # Clear the "database"
        self.order1 = Order(1, 1, ["Product1", "Product2"])
        self.order2 = Order(2, 2, ["Product3"])

    def test_create_order(self):
        """Test creating a new order"""
        response = self.client.post('/orders/', json={
            "user_id": 1,
            "products": ["Product1", "Product2"]
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Order created', response.json['message'])

    def test_get_order_by_id(self):
        """Test retrieving an order by ID"""
        order = self.order1

        response = self.client.get(f'/orders/{order.order_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['order_id'], order.order_id)
        self.assertEqual(response.json['user_id'], order.user_id)
        self.assertEqual(response.json['products'], order.products)

    def test_update_order(self):
        """Test updating an order"""
        order = self.order1

        response = self.client.put(f'/orders/{order.order_id}', json={
            "products": ["Product4", "Product5"]
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], "Order updated")
        self.assertEqual(order.products, ["Product4", "Product5"])

    def test_delete_order(self):
        """Test deleting an order"""
        order = self.order1

        response = self.client.delete(f'/orders/{order.order_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], "Order deleted")

    def test_delete_non_existent_order(self):
        """Test attempting to delete a non-existent order"""
        response = self.client.delete('/orders/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], "Order not found")

if __name__ == "__main__":
    unittest.main()
