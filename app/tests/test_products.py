import unittest
from app import create_app
from app.models.product import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        """Prepare data for testing before each test"""
        self.app = create_app()
        self.client = self.app.test_client()
        Product.products_db = []
        self.product1 = Product(1, "Product1", 100)
        self.product2 = Product(2, "Product2", 150)

    def test_create_product(self):
        """Test creating a new product"""
        response = self.client.post('/products/', json={
            "name": "Product3",
            "price": 200
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Product created', response.json['message'])
        self.assertEqual(len(Product.products_db), 3)

    def test_get_product_by_id(self):
        """Test retrieving a product by ID"""
        product = self.product1

        response = self.client.get(f'/products/{product.product_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['product_id'], product.product_id)
        self.assertEqual(response.json['name'], product.name)
        self.assertEqual(response.json['price'], product.price)

    def test_get_all_products(self):
        """Test retrieving all products"""
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)

    def test_update_product(self):
        """Test updating a product"""
        product = self.product1

        response = self.client.put(f'/products/{product.product_id}', json={
            "name": "Updated Product1",
            "price": 120
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], "Product updated")

        # Check if product is updated
        updated_product = Product.get_product_by_id(product.product_id)
        self.assertEqual(updated_product.name, "Updated Product1")
        self.assertEqual(updated_product.price, 120)

    def test_delete_product(self):
        """Test deleting a product"""
        product = self.product2

        response = self.client.delete(f'/products/{product.product_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Product deleted', response.json['message'])

        # Verify product is deleted
        deleted_product = Product.get_product_by_id(product.product_id)
        self.assertIsNone(deleted_product)

    def test_get_product_not_found(self):
        """Test trying to get a non-existing product"""
        response = self.client.get('/products/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'Product not found')

    def test_delete_product_not_found(self):
        """Test trying to delete a non-existing product"""
        response = self.client.delete('/products/999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json['message'], 'Product not found')
