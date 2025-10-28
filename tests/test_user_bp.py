import unittest
from app import create_app  # Імпортуємо фабрику застосунку

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        """Налаштування клієнта тестування перед кожним тестом."""
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_greetings_page(self):
        """Тест маршруту /users/hi/<name>."""
        response = self.client.get("/users/hi/John?age=30")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"JOHN", response.data)
        self.assertIn(b"30", response.data)

    def test_admin_page(self):
        """Тест маршруту /users/admin."""
        response = self.client.get("/users/admin")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"ADMINISTRATOR", response.data)
        self.assertIn(b"45", response.data)

if __name__ == "__main__":
    unittest.main()
