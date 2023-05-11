#!/usr/bin/python3
"""Defines unittests for base_model.py

Unittest classes:
	TestBaseModel_instantiation - line 21
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
   """Unittests for testing instantiation of the BaseModel class."""

   def test_no_args(self):
       b1 = BaseModel();
       b2 = BaseModel();
       self.assertEqual(b1.id, b
