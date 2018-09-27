from flask import Flask
from flask_restful import Api


import config
from app.api.v1.views import *


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config)

    api = Api(app)
    api.add_resource(Order, '/api/v1/order/<string:name>')
    api.add_resource(OrderList, '/api/v1/orders')


    return app
