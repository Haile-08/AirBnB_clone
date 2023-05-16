#!/usr/bin/python3
"""
Define a amenity class that inherits form BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Reprsent a Amenity

    Attributes:
        name: string - empty string
    """

    name = ""
