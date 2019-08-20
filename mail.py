from flask import Flask,jsonify
from pymongo import MongoClient

app=Flask(__name__)


@app.route('/')
def mail_save():
	try:
		conn=MongoClient()
	except:
		print('Could not connect')
	db=conn.judgement
	collection=db.tb_user
	cursor=collection.find()

	lists=[]

	for record in cursor:
		lists.append({'':record["username"]})
	#return jsonify({'emails':lists})
	return lists

app.run(debug=True)