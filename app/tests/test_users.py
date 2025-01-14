import unittest
from app import create_app
from app.models.user import User


class TestUserRoutes(unittest.TestCase):

    def setUp(self):
        """Runs before each test"""
        self.app = create_app()
        self.client = self.app.test_client()
        User.users_db.clear()

    def test_create_user(self):
        """Test creating a new user"""
        response = self.client.post('/users/', json={
            "username": "JohnDoe",
            "email": "john@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('User created', response.json['message'])

    def test_get_user_by_id(self):
        """Test retrieving a user by ID"""
        user = User(1, "JohnDoe", "john@example.com")

        response = self.client.get(f'/users/{user.user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['username'], user.username)

    def test_update_user(self):
        """Test updating a user"""
        user = User(1, "JohnDoe", "john@example.com")

        response = self.client.put(f'/users/{user.user_id}', json={
            "username": "JohnUpdated",
            "email": "john_updated@example.com"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], "User updated")
        self.assertEqual(user.username, "JohnUpdated")
        self.assertEqual(user.email, "john_updated@example.com")

    def test_delete_user(self):
        """Test deleting a user"""
        user = User(1, "JohnDoe", "john@example.com")

        response = self.client.delete(f'/users/{user.user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], "User deleted")


if __name__ == '__main__':
    unittest.main()
