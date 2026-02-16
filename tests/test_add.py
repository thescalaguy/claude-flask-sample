import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_add_integers(client):
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.get_json() == {"result": 5}


def test_add_floats(client):
    response = client.post("/add", json={"a": 1.5, "b": 2.5})
    assert response.status_code == 200
    assert response.get_json() == {"result": 4.0}


def test_add_negative_numbers(client):
    response = client.post("/add", json={"a": -1, "b": -2})
    assert response.status_code == 200
    assert response.get_json() == {"result": -3}


def test_add_missing_field(client):
    response = client.post("/add", json={"a": 1})
    assert response.status_code == 400
    assert "required" in response.get_json()["error"]


def test_add_non_numeric(client):
    response = client.post("/add", json={"a": "x", "b": 1})
    assert response.status_code == 400
    assert "numbers" in response.get_json()["error"]


def test_add_no_json_body(client):
    response = client.post("/add", content_type="text/plain", data="not json")
    assert response.status_code == 415
