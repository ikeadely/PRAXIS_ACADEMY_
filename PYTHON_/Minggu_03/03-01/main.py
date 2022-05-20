from dotenv import load_dotenv, find_dotenv
import os
import pprint
load_dotenv(find_dotenv())
from pymongo import MongoClient

password = os.environ.get("MONGODB_PWD")

connection_string =f"mongodb+srv://adel:{password}@cluster0.gds4d.mongodb.net/test"
client = MongoClient(connection_string)


# memasukkan database
mydb = client["mydb"]
mycol = mydb["riwayat"]

datalist = [{'nama':'adel', 'umur':'22', 'alamat':'trangkil'}, {'nama':'cha', 'umur':'21', 'alamat':'jepara'}, {'nama':'nis', 'umur':'24', 'alamat':'kajen'}, {'nama':'adi', 'umur':'25', 'alamat':'tayu'}, {'nama':'uut', 'umur':'30', 'alamat':'rembang'}, {'nama':'sya', 'umur':'29', 'alamat':'rembang'}, {'nama':'don', 'umur':'40', 'alamat':'jogja'}]
mycol.insert_many(datalist)