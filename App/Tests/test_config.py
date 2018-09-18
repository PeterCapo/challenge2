import os 
import pytest
from App.api.v1.views import app

@pytest.fixture
def testClient():
    app.config['Testing'] = True
    client = app.test_client()
    return client 