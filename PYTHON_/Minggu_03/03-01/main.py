# import pymongo
from dotenv import load_dotenv, find_dotenv
import os
import pprint
load_dotenv(find_dotenv())
from pymongo import MongoClient


password = os.environ.get("MONGODB_PWD")

connection_string =f"mongodb+srv://adel:{password}@cluster0.fjcgf.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)

