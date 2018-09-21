from App.Tests.test_config import testClient
import unittest
import json
from unittest import TestCase
from App.api.v1.views import get_one_order


new_order = {"address":"nairobi","date":13,"deliveryTime":1600,"description":"beef & stew","price":1400,"status":"ready"}


        
def test_get_orders(testClient):
        response = testClient.get('/api/v1/orders')
        assert response.status_code == 200

def test_post_order(testClient):   
        response = testClient.post('/api/v1/orders',data = json.dumps(new_order), content_type='application/json')
        assert response.status_code == 201

def test_get_one_order(testClient):
        response = testClient.get('/api/v1/orders/0')
        assert response.status_code == 200

def test_update_order(testClient):   
        response = testClient.put('/api/v1/orders/<string:id>',data = json.dumps(new_order), content_type='application/json')
        assert response.status_code == 202         

        