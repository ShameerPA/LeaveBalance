import pymongo
from pymongo import MongoClient

string = 'mongodb+srv://AdminProject1:<password>@project1-rtnkb.gcp.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(string)
print(f'\n\n {client}')
db = client.accounts
collections = db.list_collection_names()
print(f'\n\n{collections}')