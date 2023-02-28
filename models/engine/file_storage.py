#!/usr/bin/python3
"""import"""
import json
import os.path
"""class"""


class FileStorage:
    __file_path = __name__.__class__ + "json"
    __objects = {}

    def all(self):
        """"return dictionary __objects"""
        return self.__objects
    def new(self, obj):
        self.__objects = obj
        setattr(obj, 'id', obj.__class__.__name__)
    def save(self):
        with open(__name__.__class__ + "json", "w") as file:
            json.dump()