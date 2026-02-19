from app.models import Subtraction


def test_subtract_integers(client):
    response = client.post("/subtract", json={"a": 10, "b": 3})
    assert response.status_code == 200
    assert response.get_json() == {"result": 7}


def test_subtract_saves_operands(client):
    Subtraction.delete().execute()
    client.post("/subtract", json={"a": 15, "b": 5})
    record = Subtraction.select().order_by(Subtraction.id.desc()).get()
    assert record.a == 15
    assert record.b == 5
    assert record.created_at is not None


def test_subtract_floats(client):
    response = client.post("/subtract", json={"a": 5.5, "b": 2.5})
    assert response.status_code == 200
    assert response.get_json() == {"result": 3.0}


def test_subtract_negative_numbers(client):
    response = client.post("/subtract", json={"a": -1, "b": -2})
    assert response.status_code == 200
    assert response.get_json() == {"result": 1}


def test_subtract_missing_field(client):
    response = client.post("/subtract", json={"a": 1})
    assert response.status_code == 400
    assert "required" in response.get_json()["error"]


def test_subtract_non_numeric(client):
    response = client.post("/subtract", json={"a": "x", "b": 1})
    assert response.status_code == 400
    assert "numbers" in response.get_json()["error"]


def test_subtract_no_json_body(client):
    response = client.post("/subtract", content_type="text/plain", data="not json")
    assert response.status_code == 415
