#!/usr/bin/python3
"""Defines unittests for base_model.py

Unittest classes:
	TestBaseModel_instantiation - line 21
        TestBaseModel_save - line 27
        TestBaseModel_to_dict - line 32
        TestBaseModel__str__  -  line 38
"""
import io
import sys
import unittest
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
   """Unittests for testing instantiation of the BaseModel class."""

   def test_no_args(self):
       bm1 = BaseModel()
       bm2 = BaseModel()
       self.assertNotEqual(bm1.id, bm2,id)

   def test_three_base(self):
       bm1 = BaseModel()
       bm2 = BaseModel()
       bm3 = BaseModel()
       self.assertNotEqual(bm1.id, bm3.id)

   def test_None_input(self):
       with self.assertRaises(TypeError):
          print(BaseModel(None))

   def test_value_input(self):
       with self.assertRaises(TypeError):
          print(BaseModel(12))

   def test_date(self):
       bm1 = BaseModel()
       self.assertNotEqual(bm1.created_at, bm1.updated_at)

   def test_id_type(self):
       bm1 = BaseModel()
       self.assertIsInstance(bm1.id, str)

class TestBaseModel_save(unittest.TestCase):
   """unittests for testing the save method of the basemodel class"""

   def test_check_updatetime(self):
       bm1 = BaseModel()
       time1 = bm1.updated_at
       bm1.save()
       time2 = bm1.updated_at
       self.assertNotEqual(time1, time2)

   def test_three_updatetime(self):
       bm1 = BaseModel()
       time1 = bm1.updated_at
       bm1.save()
       bm1.save()
       bm1.save()
       time2 = bm1.updated_at
       self.assertNotEqual(time1, time2)


class TestBaseModel_to_dict(unittest.TestCase):
  """unittestfor testing the to_dict  method the BaseModel class"""

  def test_to_dict(self):
       bm1 = BaseModel()
       dict1 = bm1.__dict__
       dict2 = bm1.to_dict()
       self.assertEqual(dict1, dict2)

class TestBaseModel__str__(unittest.TestCase):
   """unittests for testing the print of the BaseModel class"""

   def test_str_method(self):
       bm1 = BaseModel()
       class_name = bm1.__class__.__name__
       class_id = bm1.id
       class_dict = bm1.__dict__
       strout = "[{}] ({}) {}\n".format(class_name, class_id, class_dict)
       capture = io.StringIO()
       sys.stdout = capture
       print(bm1)
       sys.stdout = sys.__stdout__
       self.assertEqual(strout, capture.getvalue())

