from webapp.app import app
import pytest
from datetime import datetime
import requests
import json

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

def test_weather(client):
    response = client.get("/weather")
    latitude = 40.107166238 
    longitude = -85.659664028
    res = requests.get(f"https://api.weather.gov/points/{latitude},{longitude}")
    points = json.loads(res.text)
    forecast_url = points["properties"]["forecast"]
    res = requests.get(forecast_url)
    forecast = json.loads(res.text)
    current = forecast["properties"]["periods"][0]
    print(response.data)
    assert b"with a high near" in response.data
