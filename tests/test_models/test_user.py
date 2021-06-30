#!/usr/bin/python3
"""Test User"""
import unittest
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
