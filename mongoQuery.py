from pymongo import MongoClient
from flask import jsonify

client=MongoClient()
db=db.examples

def user_mentions():
	result=db.tweets.aggregate([a
		{ "$unwind":"entitites.user_mentions"},
		{"$group":{"$_id":"user.screen_name",
		"count":{"$sum":1}}},
		{"$sort":{"$count":-1}},
		{"$limit":1}
		])

	return result

if __name__=='__main__':
	result=user_mentions()
	print(result)