#!/usr/bin/python3
"""This module instantiates a storage object

-> Instantiates db storage when ENV 'HBNB_TYPE_STORAGE' = 'db'
-> Otherwise instantiates a file storage
"""
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
