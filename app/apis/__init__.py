from flask_restplus import Api
from .hello import api as hello_ns


api = Api(prefix='/api', doc='/api/docs')
api.add_namespace(hello_ns)
