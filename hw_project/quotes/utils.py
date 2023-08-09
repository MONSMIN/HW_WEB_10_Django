from pymongo import MongoClient
from bson import ObjectId

def get_mongodb():
    client = MongoClient("mongodb://localhost")
    db = client.hw
    return db