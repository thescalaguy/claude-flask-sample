import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_divide_integers(client):
    response = client.post("/divide", json={"a": 10, "b": 2})
    assert response.status_code == 200
    assert response.get_json() == {"result": 5.0}


def test_divide_floats(client):
    response = client.post("/divide", json={"a": 7.5, "b": 2.5})
    assert response.status_code == 200
    assert response.get_json() == {"result": 3.0}


def test_divide_negative_numbers(client):
    response = client.post("/divide", json={"a": -10, "b": 2})
    assert response.status_code == 200
    assert response.get_json() == {"result": -5.0}


def test_divide_by_zero(client):
    response = client.post("/divide", json={"a": 1, "b": 0})
    assert response.status_code == 400
    assert "zero" in response.get_json()["error"].lower()


def test_divide_missing_field(client):
    response = client.post("/divide", json={"a": 1})
    assert response.status_code == 400
    assert "required" in response.get_json()["error"]


def test_divide_non_numeric(client):
    response = client.post("/divide", json={"a": "x", "b": 1})
    assert response.status_code == 400
    assert "numbers" in response.get_json()["error"]
