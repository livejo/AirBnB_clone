#!/usr/bin/python3
"""
    Unit Testing For BaseModel class
"""
from models import BaseModel
import unittest
import inspect
import time
from datetime import datetime
import pep8 as pcs
import models


class TestBaseModel(unittest.TestCase):
    """ Testing the Base Class """
    def test_doc1(self):
        """test documentation for module"""
        res = "Module has no documenation"
        self.assertIsNotNone(models.base_model.__doc__, res)

    def test_doc2(self):
        """test documentation for class"""
        res = "Module has no documenation"
        self.assertIsNotNone(models.base_model.BaseModel.__doc__, res)

    def test_doc3(self):
        """test documentation for methods"""
        res = "method init has no documenation"
        self.assertIsNotNone(models.base_model.BaseModel.__init__.__doc__, res)
        res1 = "method __str__ has no documenation"
        self.assertIsNotNone(models.base_model.BaseModel.__str__.__doc__, res1)
        res2 = "method save has no documenation"
        self.assertIsNotNone(models.base_model.BaseModel.save.__doc__, res2)
        res3 = "method to_dict has no documenation"
        self.assertIsNotNone(models.base_model.BaseModel.to_dict.__doc__, res3)
        
    
