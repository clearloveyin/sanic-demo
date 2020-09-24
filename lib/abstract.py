import ast
from functools import wraps
from sanic.response import json
from sanic_restful import reqparse
from werkzeug.exceptions import BadRequest


def parse_arguments(*parse_args):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            request = args[1]
            parser = reqparse.RequestParser(bundle_errors=True)
            try:
                arguments = dict()
                for argument in parse_args:
                    parser.add_argument(argument)
                arguments.update(parser.parse_args(request))
                return f(arguments=arguments, *args, **kwargs)
            except BadRequest as e:
                return json({"success": False, "message": u"参数错误", "data": str(e), "code": 10400})
        return decorated_function
    return decorator

