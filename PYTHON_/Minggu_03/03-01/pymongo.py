from typing import Collection
import pymongo

db = pymongo.MongoClient("mongodb://localhost:27017")
dbku = db["blog"]
collectionku = dbku['artikel']

data = {"judul": "belajar ngoding python-mongodb", "penulis": "adel"}

collectionku.insert_one(data)
