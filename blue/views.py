from sanic.response import text
from sanic_restful import Resource
from sanic_restful.reqparse import Argument

from lib.abstract import parse_arguments


class UserInfo(Resource):

    async def get(self, request):
        return 'I am get method'

    async def post(self, request):
        return 'I am post method'

    async def put(self, request):
        return 'I am put method'

    async def patch(self, request):
        return 'I am patch method'

    async def delete(self, request):
        return 'I am delete method'


class Demo(Resource):
    # type为list或dict的参数必须放在body里才能被发现
    @parse_arguments(
        Argument("name", type=str, required=True),
        Argument("age", type=int, default=0),
        Argument("di", type=dict, location="json"),
        Argument("li", type=list, location="json")
    )
    async def get(self, request, arguments):
        print(arguments)
        return arguments

    async def post(self, request, arguments):
        print(arguments)
        return arguments
