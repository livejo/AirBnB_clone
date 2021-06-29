#!/usr/bin/python3
"""Test City"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class Testcity(unittest.TestCase):

    def test_pep8__city(self):
        """Test PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code errors.")

    def test_class(self):
        city1 = City()
        self.assertEqual(city1.__class__.__name__, "City")

    def test_Base(self):
        city1 = City()
        self.assertTrue(issubclass(city1.__class__, BaseModel))

    def test_city(self):
        """
        Test attributes of Class City
        """
        my_city = City()
        my_state = State()
        my_city.name = "Addis Ababa"
        my_city.state_id = my_state.id
        self.assertEqual(my_city.name, 'Addis Ababa')
        self.assertEqual(my_city.state_id, my_state.id)
