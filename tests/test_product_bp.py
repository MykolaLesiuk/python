import unittest
from app import create_app

class ProductBlueprintTestCase(unittest.TestCase):
    def setUp(self):
        """Налаштування клієнта тестування."""
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_product_list_page(self):
        """Перевірка сторінки /products/."""
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)

        # декодуємо відповідь у текст (UTF-8)
        html = response.data.decode('utf-8')

        # перевіримо наявність назв товарів у HTML
        self.assertIn("Ноутбук", html)
        self.assertIn("Мишка", html)
        self.assertIn("Клавіатура", html)

    def test_product_template_title(self):
        """Перевірка заголовку сторінки."""
        response = self.client.get("/products/")
        html = response.data.decode('utf-8')
        self.assertIn("Товари", html)

if __name__ == "__main__":
    unittest.main()
