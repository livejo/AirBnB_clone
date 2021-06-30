#!/usr/bin/python3
"""Test Place"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class Testplace(unittest.TestCase):

    def test_pep8_place(self):
        """Test  PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code errors.")

    def test_class(self):
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "update_at"))

    def test_place(self):
        """
        Test attributes of Class Place
        """
        my_amenity = Amenity()
        my_city = City()
        my_user = User()
        my_place = Place()
        my_place.city_id = my_city.id
        my_place.user_id = my_user.id
        my_place.name = 'Addis Ababa'
        my_place.description = 'Capital city'
        my_place.number_rooms = 4
        my_place.number_bathrooms = 2
        my_place.max_guest = 4
        my_place.price_by_night = 200
        my_place.latitude = 25.0342808
        my_place.longitude = -77.3962784
        my_place.amenity_ids = str(my_amenity.id)
        self.assertEqual(my_place.city_id, my_city.id)
        self.assertEqual(my_place.user_id, my_user.id)
        self.assertEqual(my_place.name, 'Addis Ababa')
        self.assertEqual(my_place.description, 'Capital city')
        self.assertEqual(my_place.number_rooms, 4)
        self.assertTrue(type(my_place.number_rooms), int)
        self.assertEqual(my_place.number_bathrooms, 2)
        self.assertTrue(type(my_place.number_bathrooms), int)
        self.assertEqual(my_place.max_guest, 4)
        self.assertTrue(type(my_place.max_guest), int)
        self.assertEqual(my_place.price_by_night, 200)
        self.assertTrue(type(my_place.price_by_night), int)
        self.assertEqual(my_place.latitude, 25.0342808)
        self.assertTrue(type(my_place.latitude), float)
        self.assertEqual(my_place.longitude, -77.3962784)
        self.assertTrue(type(my_place.longitude), float)
        self.assertEqual(my_place.amenity_ids, str(my_amenity.id))
        self.assertTrue(type(my_place.amenity_ids), str)

    def test_dict_value(self):
        """
            test dict values
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        place = Place()
        dict_con = place.to_dict()
        self.assertEqual(dict_con["__class__"], "Place")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
                            dict_con["created_at"],
                            place.created_at.strftime(time_format)
                                        )
        self.assertEqual(
                            dict_con["updated_at"],
                            place.updated_at.strftime(time_format))
