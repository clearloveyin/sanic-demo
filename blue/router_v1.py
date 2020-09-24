from sanic import Blueprint
from .views import UserInfo, Demo
from sanic_restful import Api

bp_v1 = Blueprint('v1', url_prefix='/v1')
api = Api(bp_v1)

api.add_resource(UserInfo, '/')
api.add_resource(Demo, '/demo')
