#!/usr/bin/python3
"""Test User"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class Testuser(unittest.TestCase):

    def test_pep8_user(self):
        """Test that we conform to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code errors.")

    def test_User(self):
        """
        Test Class Use
        """
        my_user = User()
        my_user.first_name = 'ALX'
        my_user.last_name = 'SE'
        my_user.email = '11@gmail.com'
        self.assertEqual(my_user.first_name, 'ALX')
        self.assertEqual(my_user.last_name, 'SE')
        self.assertEqual(my_user.email, '11@gmail.com')
