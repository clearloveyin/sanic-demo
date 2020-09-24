import os
from __init__ import app
from config import development, production
from lib.middleware import print_on_request, print_on_response


def create_app():
    config_type = os.getenv('ENV_CONFIG') or 'development'
    config_obj = load_config(config_type)
    app.config.from_object(config_obj)
    # 注册中间件
    app.register_middleware(print_on_request, attach_to='request')
    app.register_middleware(print_on_response, attach_to='response')

    return app


def load_config(config_type):
    if config_type == 'development':
        config_obj = development
    else:
        config_obj = production
    return config_obj

