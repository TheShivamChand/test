from flask import Flask, request
from webargs import fields, validate
from webargs.flaskparser import use_args

user_args = {
	"username": fields.Str(required=True),
	"password": fields.Str(validate=validate.Length(min=6)),
	"limit": fields.Int(missing=10),
	"nickname": fields.List(fields.Str()),
	"languages": fields.DelimitedList(fields.Str()),
	"profile_photo": fields.Field(location="files", validate=lambda f: f.mimetype in ["image/jpeg", "image/png"])
}


app = Flask(__name__)


@app.route('/')
@use_args({"name": fields.Str(required=True)})
def index(args):
	return "Hello "+args['name']


@app.route('/register', methods=["POST"])
def register():
	args = parser.parse(user_args, request)
	return register_user(args['username'],
		args['password'],
		args['limit'],
		fullname=args['fullname']
		)


if __name__ == "__main__":
	app.run(debug=True)