"""
Integration tests for the Flask routes.

Uses Flask's built-in test client — no network, fast, deterministic.
"""
import json
import pytest
from app.main import app as flask_app


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as c:
        yield c


def test_index_returns_service_info(client):
    resp = client.get("/")
    assert resp.status_code == 200
    payload = resp.get_json()
    assert payload["service"] == "sit707-calculator"
    assert "endpoints" in payload


def test_health_endpoint(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "healthy"


def test_add_endpoint(client):
    resp = client.get("/add?a=2&b=3")
    assert resp.status_code == 200
    assert resp.get_json()["result"] == 5


def test_subtract_endpoint(client):
    resp = client.get("/subtract?a=10&b=4")
    assert resp.status_code == 200
    assert resp.get_json()["result"] == 6


def test_multiply_endpoint(client):
    resp = client.get("/multiply?a=6&b=7")
    assert resp.status_code == 200
    assert resp.get_json()["result"] == 42


def test_divide_endpoint(client):
    resp = client.get("/divide?a=20&b=5")
    assert resp.status_code == 200
    assert resp.get_json()["result"] == 4


def test_missing_params_returns_400(client):
    resp = client.get("/add?a=2")
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_non_numeric_params_returns_400(client):
    resp = client.get("/add?a=hello&b=3")
    assert resp.status_code == 400
