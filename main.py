#!/usr/bin/python3
"""Doc
"""
from models import *
from models import base_model


class BaseModel(BaseModel):
    """Doc
    """

    def save(self):
        self.updated_at = datetime.utcnow()