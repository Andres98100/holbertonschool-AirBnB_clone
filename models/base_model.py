#!/usr/bin/python3
"""import"""
import uuid
from datetime import datetime
from . import storage
"""class"""


class BaseModel:
    """method init"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%d"
                                                         "T%H:%M:%S.%f"))
        storage.new(self)

    def __str__(self):
        """return"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update the date"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """new dictionary"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        """return new dictionary"""
        return new_dict
