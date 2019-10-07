from marshmallow import Schema, fields, pprint, post_load, ValidationError, validate
import datetime as dt

# class User:
# 	def __init__(self, name, email):
# 		self.name = name
# 		self.email = email
# 		self.created_at = dt.datetime.now()

# 	def __repr__(self):
# 		return "<User(name={self.name!r})>".format(self=self)


# class UserSchema(Schema):
# 	name = fields.Str()
# 	email = fields.Email()
# 	created_at = fields.DateTime()

# 	@post_load
# 	def make_user(self, data, **kwargs):
# 		return User(**data)

# user = User("Shivam", "shivamdeopa@gmail.com")
# schema = UserSchema()
# # result = schema.dump(user)
# json_result = schema.dumps(user)	#result in json format
# # pprint(json_result)


# user_data = {
#     "email": "shivamdeopa@gmail.com",
#     "name": "Shivam",
# }
# schema = UserSchema()
# result = schema.load(user_data)
# # pprint(result)


# user1 = User(name="shivam", email="shivam@gmail.com")
# user2 = User(name="satyam", email="satyam@gmail.com")
# users = [user1, user2]
# schema = UserSchema(many=True)
# result = schema.dump(users)  # OR UserSchema().dump(users, many=True)
# # pprint(result)

# # invalid_user_data = {
# # 	"name": 7,
# # 	"email": "shivam"
# # }
# # try:
# # 	result = UserSchema().load(invalid_user_data)
# # 	pprint(result)
# # except ValidationError as err:
# # 	print(err.messages)
# # 	print(err.valid_data)



# class bandMemberSchema(Schema):
# 	name = fields.Str(required=True)
# 	email = fields.Email()

# user_data = [
# 	{'name':"shivam", 'email':"shivam@gmail.com"},	#valid data
# 	{'name':"Satyam", 'email':"satyam"},		#invalid email
# 	{'email':"sundaram@gmail.com"}		#missing name
# ]

# try:
# 	bandMemberSchema(many=True).load(user_data)
# except ValidationError as err:
# 	# pprint(err.messages)


class validateDataSchema(Schema):
	name = fields.Str(validate=validate.Length(min=4))
	age = fields.Int(validate=validate.Range(min=18, max=40))
	permission = fields.Str(validate=validate.OneOf(['read','write','admin']), data_key="role")

data= {'name':"shivam", "age":35, "role":"read"}

try:
	result = validateDataSchema().load(data)
	pprint(result)
except ValidationError as err:
	pprint(err.messages) 
