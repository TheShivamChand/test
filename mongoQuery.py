from pymongo import MongoClient
from flask import jsonify

db=MongoClient()
db=db.judgement
collection=db.tb_query_ratings

for i in collection.find():
	print(i)