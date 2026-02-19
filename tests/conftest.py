import pytest

from app import create_app
from app.models import Addition, Quotient, Subtraction, db


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    db.create_tables([Addition, Quotient, Subtraction])

    with app.test_client() as client:
        yield client

    db.drop_tables([Addition, Quotient, Subtraction])
