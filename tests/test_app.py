import sys
import os
sys.path.insert(0, os.path.abspath("src"))

import unittest
from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello from EC2 🚀")

if __name__ == "__main__":
    unittest.main()

