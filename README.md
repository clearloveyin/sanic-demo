# sanic-demo
## 目前集成了Sanic+Blueprint+sanic_restful，支持自定义接口参数校验
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
            return arguments`
 ## 启动：python manage.py runserver