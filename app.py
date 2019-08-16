from  flask import Flask,jsonify,request,Response
import json
#from settings import *
from pymongo import MongoClient
import jwt
import datetime

app=Flask(__name__)

app.config['SECRET_KEY']= 'r2d2'

@app.route('/login')
def get_token():
	expirationDate= datetime.datetime.utcnow()+datetime.timedelta(seconds=100)
	token= jwt.encode({'exp':expirationDate}, app.config['SECRET_KEY'],algorithm='HS256')
	return token

'''
books=[
{
	"name":"A"
,	"price":3.25,
	"isbn":1
},
{
	"name":"B",
	"price":5.16,
	"isbn":2
},
{
	"name":"C",
	"price":2.96,
	"isbn":3
}
]

try:
	conn=MongoClient()
	print("Connected Successfully")
except:
	print("Could not connect to database")
db=conn.database

collection=db.test

for i in books:
	collection.insert_one(i)
	#print(i)
'''


def validBookObject(bookObject):
	if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
		return True
	else:
		return False

@app.route('/home')
def hello_world():
	token=request.args.get('token')
	try:
		jwt.decode(token,app.config['SECRET_KEY'])
	except:
		return jsonify({'error':'enter a valid token'}), 401

	return 'Hello'

@app.route('/books')
def get_books():
	token= request.args.get('token')
	try:
		jwt.decode(token,app.config['SECRET_KEY'])
		try:
			conn=MongoClient()
		except:
			print("Could not connect to database")
		db=conn.database
		collection=db.test
		cursor=collection.find().sort("isbn")

		lists=[]

		for record in cursor:
			lists.append({'name':record['name'],'price':record['price'],'isbn':record['isbn']})
	except:
		return jsonify({'error':'Enter a valid token'}),401

	return jsonify({'books:':lists})

@app.route('/add_books',methods=['POST'])
def add_books():
	try:
		conn=MongoClient()
	except:
		print("Could not connect")
	db=conn.database
	collection=db.test
	cursor=collection.find()

	res = request.get_json()
	if(validBookObject(res)):
		new_data={
		"name":res['name'],
		"price":res['price'],
		"isbn":res['isbn']
		}
		#books.insert(len(books),new_data)
		collection.insert_one(new_data)
		response=Response("",201,mimetype="application/json")
		response.headers['Location'] = "/books/" + str(new_data['isbn'])
		return response
	else:
		errorMsg={
		"msg":"Error Message",
		"solution": "Try to send data in proper method"
		}
		response=Response(json.dumps(errorMsg),400,mimetype='application/json')
		return response

@app.route('/books/<int:isbn>')
def get_books_by_isbn(isbn):
	try:
		conn=MongoClient()
	except:
		print("Could not connect")
	db=conn.database
	collection=db.test

	book=collection.find_one({'isbn':isbn})
	return jsonify({'name':book['name'],'price':book['price'],'isbn':book['isbn']})

	'''return_value={}
	for book in books:
		if book['isbn'] == isbn:
			return_value={
			'name':book['name'],
			'price':book['price']
			}
	return return_value'''

@app.route('/books/<int:isbn>',methods=['PUT'])
def replace_books(isbn):
	request_data=request.get_json()
	name1=request_data['name'],
	price1=request_data['price'],
	isbn1=isbn
	try:
		conn=MongoClient()
	except:
		print("could not connect")
	db=conn.database
	collection=db.test
	
	collection.update_one({"isbn":isbn},{"$set":{"name":name1,"price":price1,"isbn":isbn1}})

	'''
	i=0
	for book in books:
		current_isbn=book['isbn']
		if current_isbn==isbn:
			books[i]=new_book
		i+=1
	'''
	response=Response("",204)
	return response

@app.route('/books/<int:isbn>',methods=['PATCH'])
def update_book(isbn):
	request_data=request.get_json()
	updated_book={}
	if "name" in request_data:
		updated_book['name']=request_data['name']
	if "price" in request_data:
		updated_book['price']=request_data['price']
	for book in books:
		if book['isbn']==isbn:
			book.update(updated_book)
	response=Response("",204)
	response.headers['Location']='/books/'+str(isbn)
	return response

@app.route('/books/<int:isbn>',methods=['DELETE'])
def delete_book(isbn):
	try:
		conn=MongoClient()
	except:
		print("could not connect")
	db=conn.database
	collection=db.test
	cursor=collection.find()
	collection.delete_one({'isbn':isbn})
	response=Response("",204)
	return response

	'''
	i=0
	for book in books:
		if book['isbn']==isbn:
			books.pop(i)
			response=Response("",204)
		i += 1
	return response
	'''

app.run(port=5000)