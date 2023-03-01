#!/usr/bin/python3
from models.base_model import BaseModel

bm = BaseModel()
bm.save()
print(type(bm.updated_at))
d_json = bm.to_dict()
print(type(d_json['updated_at']))