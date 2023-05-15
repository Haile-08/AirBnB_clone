#!/usr/bin/python3
"""
Define a User class that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represnt a user

    Attributes:
        email (str): The email of the user.
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """


    email = ""
    password = ""
    first_name = ""
    last_name = ""

