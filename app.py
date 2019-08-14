from  flask import Flask,jsonify,request,Response,json

app= Flask(__name__)

books=[
{
	"name":"A",
	"price":3.25,
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


def validBookObject(bookObject):
	if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
		return True
	else:
		return False


@app.route('/')
def hello_world():
	return 'Hello'

@app.route('/books')
def get_books():
	return jsonify({'books':books})

@app.route('/add_books',methods=['POST'])
def add_books():
	res = request.get_json()
	if(validBookObject(res)):
		new_data={
		"name":res['name'],
		"price":res['price'],
		"isbn":res['isbn']
		}
		books.insert(len(books),new_data)
		response=Response("",201,mimetype="application/json")
		response.headers['Location'] = "/books/" + str(new_data['isbn'])
		return response
	else:
		errorMsg={
		"msg":"Error Message",
		"solution": " Try to send data in proper method"
		}
		response=Response(json.dumps(errorMsg),400,mimetype='application/json')
		return response

@app.route('/books/<int:isbn>')
def get_books_by_isbn(isbn):
	return_value={}
	for book in books:
		if book['isbn'] == isbn:
			return_value={
			'name':book['name'],
			'price':book['price']
			}
	return return_value

@app.route('/books/<int:isbn>',methods=['PUT'])
def replace_books(isbn):
	request_data=request.get_json()
	new_book={
	'name':request_data['name'],
	'price':request_data['price'],
	'isbn':isbn
	}
	i=0
	for book in books:
		current_isbn=book['isbn']
		if current_isbn==isbn:
			books[i]=new_book
		i+=1
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
	i=0
	for book in books:
		if book['isbn']==isbn:
			books.pop(i)
			response=Response("",204)
		i += 1
	return response

app.run(port=5000)