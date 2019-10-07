import datetime as dt
from flask import Flask, jsonify
from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs

app = Flask(__name__)

hello_args = {"name": fields.Str(missing='Friend')}

@app.route('/')
@use_args(hello_args)
def index(args):
	return jsonify({"message": "Welcome, {}!".format(args['name'])})


add_args = {"x": fields.Float(required=True), "y": fields.Float(required=True)}


@app.route('/add', methods=['POST'])
@use_kwargs(add_args)
def add(x, y):
	return jsonify({"result": x+y})


dateadd_args = {
    "value": fields.Date(required=False),
    "addend": fields.Int(required=True, validate=validate.Range(min=1)),
    "unit": fields.Str(missing="days", validate=validate.OneOf(["minutes", "days"])),
}s


@app.route("/dateadd", methods=["POST"])
@use_kwargs(dateadd_args)
def dateadd(value, addend, unit):
    value = value or dt.datetime.utcnow()
    if unit == "minutes":
        delta = dt.timedelta(minutes=addend)
    else:
        delta = dt.timedelta(days=addend)
    result = value + delta
    return jsonify({"result": result.isoformat()})


if __name__ == '__main__':
	app.run(debug=True)