from App.Tests.test_config import testClient
import json

def test(testClient):   
    response = testClient.put('/api/v1/orders', content_type='application/json')
    assert response.status_code == 405