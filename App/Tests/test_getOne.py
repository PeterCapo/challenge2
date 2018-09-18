from App.Tests.test_config import testClient


def test(testClient):
        response = testClient.get('/api/v1/orders/0')
        assert response.status_code == 500