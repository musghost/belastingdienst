import unittest
from flask import url_for
from flask_testing import TestCase

from app import app

class TestApp(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_index_page(self):
        response = self.client.get(url_for('index'))
        self.assert200(response)
        self.assertIn(b"Enter Your Name and Age", response.data)