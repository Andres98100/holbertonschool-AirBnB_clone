#!/usr/bin/python3
from models.base_model import BaseModel

bm1 = BaseModel()
bm2 = BaseModel(**bm1.to_dict())
print(bm1.id == bm2.id)