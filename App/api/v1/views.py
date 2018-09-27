from flask_restful import Resource, reqparse
from flask import Flask, request


from .model import Orders, orders


class Order(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type=float, required=True,
    help="This field cannot be left blank!")

    def get(self, name):
        return {'order': next(filter(lambda x:
    x['name'] == name, orders), None)}, 200

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, orders), None) is not None:
            return {'message':
            "An order with name'{}' already exists.".format(name)}

        data = Order.parser.parse_args()

        order = {'name': name, 'price': data['price']}
        orders.append(order)
        return order, 201

    def delete(self, name):
        global orders
        orders = list(filter(lambda x: x['name'] != name, orders))
        return {'message': 'Orders deleted'}

    def put(self, name):
        data = Order.parser.parse_args()
        order = next(filter(lambda x: x['name'] == name, orders), None)
        if order is None:
            order = {'name': name, 'price': data['price']}
            orders.append(order)
        else:
            order.update(data)
        return order


class OrderList(Resource):

    def get(self):
        return {'orders': orders}
