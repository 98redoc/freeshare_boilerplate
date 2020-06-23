""" Flask App Config Module."""
import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
env = os.path.join(basedir, '.env')
if os.path.exists(env):
	load_dotenv(env)
else:
	print('Warning: .env file not found')


class Config(object):
	DEBUG = False
	TESTING = False
	SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
	# database configs
	SQLALCHEMY_DATABASE_URI = os.environ.get(
		'DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'db.sqlite'))
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	RESTPLUS_MASK_SWAGGER = False
	MAX_CONTENT_LENGTH = 100 * 1024 * 1024
	# version configs
	VERSION_MAJOR = 1
	VERSION_MINOR = 0
	VERSION_PATCH = 0


class DevConfig(Config):
	DEBUG = True


class TestConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'users.sqlite')


class ProdConfig(Config):
	pass
