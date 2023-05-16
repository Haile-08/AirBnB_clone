#!/usr/bin/python3
"""
Define a State class that inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Reprsent a state

    Attribute:
        name: string - empty string
    """

    name = ""
