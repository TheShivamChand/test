from flask import Blueprint

mod=Blueprint('site',__name__)

@mod.route('/homepage')
def home():
	return '<h1>You are in the homepage</h1>'