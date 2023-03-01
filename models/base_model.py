#!/usr/bin/python3
"""import"""
import uuid
from datetime import datetime
from . import storage
import models
"""class"""


class BaseModel:
    """method init"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
            self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        
    def __str__(self):
        """return"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update the date"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """new dictionary"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        """return new dictionary"""
        return new_dict
