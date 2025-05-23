from datetime import datetime
import pytest
from ..app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def _validate_isoformat(json_data):
    try:
        datetime.fromisoformat(json_data["datetime"])
    except ValueError:
        assert False, "Invalid date format"

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Welcome to the Flask API!"}

def test_about(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert response.get_json() == {"version": "1.0", "author": "William Yanez"}

def test_datetime_local(client):
    """Verify that the '/datetime' endpoint returns the local time by default."""
    response = client.get('/datetime')

    assert response.status_code == 200
    json_data = response.get_json()

    assert "datetime" in json_data
    assert json_data["format"] == "local"

    _validate_isoformat(json_data)


def test_datetime_utc(client):
    """Verify that the '/datetime/utc' endpoint returns the UTC time."""
    response = client.get('/datetime/utc')
    
    assert response.status_code == 200
    json_data = response.get_json()

    assert "datetime" in json_data
    assert json_data["format"] == "utc"

    _validate_isoformat(json_data)
