#!/usr/bin/python3
"""
Define a base model class
"""
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes
    JSON file to instances
    Arttributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store all objects
        by <class name>.id
    methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key
        save(self): serializes __objects to the JSON file
        reload(self): deserializes the JSON file to __objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return type(self).__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        Arttributes:
            obj: all objects value  by <class name>.id
        """
        key = "{}.{}".format(self.__class__.__name__,self.id)
        type(self).__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(type(self).__file_path, "w", encoding="utf-8") as f:
            serialize = json.dumps(type(self).__objects)
            f.write(serialize)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        with open(type(self).__file_path, "r") as f:
            data = json.loads(f.read)
            type(self).__objects = data


