import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017/")  #connects to the MongoDB server

db = cluster["Test"] #initializes the database
collection= db["test_data"] #initializes the collection

# post = {"_id": 0, "name": "test", "score":6}  #example data
# post2 = {"_id": 1, "name": "test2", "score": 7}  #another example data
# post3 = {"_id": 2, "name": "test3", "score": 8}  #yet another example data
# post4 = {"_id": 3, "name": "test4", "score": 9}  #more example data

# collection.insert_one(post2)  #inserts  data into the collection 
# #id without underscore = jibrish

# collection.insert_many([post3, post4]) 

result=collection.find({"name": "test2"})  #finds the data with name "test"

for result in result: #prints the result of the find operation
    print(result["_id"])  