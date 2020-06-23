""" Hello API Namespace Module. """
from flask_restplus import Resource, Namespace
from flask import request
from ..services.hello_service import hello_world

api = Namespace(name='hello', description="Hello World!")


@api.route('')
class Hello(Resource):
	def get(self):
		return hello_world()
