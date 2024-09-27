from webapp.app import app
import pytest
from datetime import datetime

@pytest.fixture()
def client():
    return app.test_client()

def test_root(client):
    response = client.get("/")
    date_raw = datetime.now()
    date_pretty = date_raw.strftime("%m-%d-%Y")
    print(response.data)
    assert date_pretty.encode() in response.data

def test_calc(client):
    response = client.get("/calc?a=5&op=*&b=3")
    print(response.data)
    assert b"15" in response.data
