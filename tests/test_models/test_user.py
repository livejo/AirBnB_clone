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
    """unit test"""
    def test_User(self):
        """
        Test Class Use
        """
        my_user = User()
        my_user.first_name = 'ALX'
        my_user.last_name = 'SE'
        my_user.email = '11@gmail.com'
        my_user.password = '1234'
        self.assertEqual(my_user.first_name, 'ALX')
        self.assertEqual(my_user.last_name, 'SE')
        self.assertEqual(my_user.email, '11@gmail.com')
        self.assertEqual(my_user.password, '1234')
