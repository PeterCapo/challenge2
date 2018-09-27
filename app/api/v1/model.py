orders = []

class Orders:

    def __init__(self, name=None, price=None,
                 description=None, status="Pending"):
        self.id = len(orders)+1
        self.name = name
        self.price = price
        self.description = description
        self.status = status


    def get_id(self, order_id):
        for order in orders:
            if order.id == order_id:
                return order