#!/usr/bin/python3
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

fs = FileStorage()
file_path = "file.json"
try:
    file_path = FileStorage._FileStorage__file_path
except:
    pass
try:
    os.remove(file_path)
except:
    pass
try:
    fs._FileStorage__objects.clear()
except:
    pass
ids = []
objs_by_id = {}
for i in range(10):
    bm = BaseModel()
    fs.new(bm)
    bm.save()
    ids.append(bm.id)
    objs_by_id[bm.id] = bm

try:
    fs._FileStorage__objects.clear()
except:
    pass
fs.reload()

all_reloaded = fs.all()

if len(all_reloaded.keys()) != len(ids):
    print("Missing after reload")

for id in ids:
    if all_reloaded.get(id) is None and all_reloaded.get("{}.{}".format("BaseModel", id)) is None:
        print("Missing {}".format(id))

for id in ids:
    obj_reloaded = all_reloaded.get(id)
    if obj_reloaded is None:
        obj_reloaded = all_reloaded.get("{}.{}".format("BaseModel", id))
    print(obj_reloaded.__class__.__name__)
    obj_created = objs_by_id[id]
    print(obj_reloaded.id == obj_created.id)
    print(obj_reloaded.created_at == obj_created.created_at)
    print(obj_reloaded.updated_at == obj_created.updated_at)

try:
    os.remove(file_path)
except Exception as e:
    pass