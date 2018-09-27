import json
from unittest import TestCase


from app import create_app


class TestOrders(TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
    
    def tearDown(self):
        self.app_context.pop()    
    
    def test_get_all_orders(self):

        res = self.client.get(
            "/api/v1/orders",
            headers={"content-type": "application/json"}
        )

        self.assertEqual(res.status_code, 200)

    def test_get_one_order(self):
        res = self.client.get(
            "/api/v1/order/1",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)
    
    def test_create_order(self):
        data = {
            "name": "ugali",
            "price": 50,
            "description": "delicious"
        }

        res = self.client.post(
            "/api/v1/order/1",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )

        self.assertEqual(res.status_code, 201)
    
    def test_update(self):
        data = {
            "name": "ugali",
            "price": 50,
            "description": "delicious"
        }

        res = self.client.put(
            "/api/v1/order/1",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )

        self.assertEqual(res.status_code, 200)

    def test_invalid_id(self):
        res = self.client.get(
            "/api/v1/orders/111",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 404)

    def test_non_order_delete(self):
        res = self.client.delete(
            "api/v1/order/1",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)
   
           


        

   


