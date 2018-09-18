from App.Tests.test_config import testClient


def test(testClient):
        response = testClient.get('/api/v1/orders')
        assert response.status_code == 200

        