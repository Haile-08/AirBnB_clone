#!/usr/bin/python3
"""Defines unittests for base_model.py.
Unittest classes:
        TestBase_instantiation - line 21
"""
import io
import sys
import unittest
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_id_value(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_date_value(self):
        b1 = BaseModel()
        self.assertNotEqual(b1.created_at, b1.updated_at)

    def test_date_created(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.created_at, b2.created_at)

    def test_date_update(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.updated_at, b2.updated_at)

class TestBaseModel_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of BaseModel class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.
        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method(self):
        b1 = BaseModel()
        capture = TestBaseModel_stdout.capture_stdout(b1, "print")
        self.assertEqual("[BaseModel] ({}) {}\n".format(b1.id, b1.__dict__), capture.getvalue())

class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing the save method of BaseModel class"""

    def test_save(self):
        b1 = BaseModel()
        val1 = b1.updated_at
        b1.save()
        val2 = b1.updated_at
        self.assertNotEqual(val1, val2)

class TestBaseModel_dict(unittest.TestCase):
    """Unittests for testing the to_dict model of the basemodel class"""

    def test_to_dict(self):
        b1 = BaseModel()
        self.assertNotEqual(b1.__dict__, b1.to_dict())
