"""unit test for the flask application"""
import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    """Test case for flask application."""
    def setUp(self):
        """Set up the test client."""
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """Test the home page."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'1RVU23CSE018', response.data)

if __name__ == '__main__':
    unittest.main()
    # Run the tests