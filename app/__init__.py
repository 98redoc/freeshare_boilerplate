import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import config


db = SQLAlchemy()


def create_app(config_name="dev"):
	""" Application Factory.

	Args:
		config_name (str): name of the config class used for configuration.
	"""
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(getattr(config, config_name.title()+'Config'))
	db.init_app(app)

	# ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	with app.app_context():
		from .apis import api
		api.init_app(app)

	return app
