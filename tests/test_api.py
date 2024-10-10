from fastapi.testclient import TestClient

from olympics import api


client = TestClient(api.app)


def test_countries():
    response = client.get("/countries/")
    assert response.status_code == 200
    assert len(response.json()) > 100


def test_athletes():
    response = client.get("/athletes/")
    assert response.status_code == 200
    assert len(response.json()) > 100


def test_discipline():
    response = client.get("/discipline/")
    assert response.status_code == 200
    assert len(response.json()) > 100


def test_connection():
    response = client.get("/connection/")
    assert response.status_code == 200
    assert len(response.json()) > 100


def test_teams():
    response = client.get("/teams/")
    assert response.status_code == 200
    assert len(response.json()) > 100


def test_events():
    response = client.get("/events/")
    assert response.status_code == 200
    assert len(response.json()) > 100


def test_medals():
    response = client.get("/medals/")
    assert response.status_code == 200
    assert len(response.json()) > 100


def test_discipline_athletes():
    response = client.get("/discipline_athletes/")
    assert response.status_code == 200
    assert len(response.json()) > 100


def test_top_countries():
    response = client.get("/top-countries/")
    assert response.status_code == 200
    assert len(response.json()) > 100


def test_collective_medals():
    response = client.get("/collective-medals/")
    assert response.status_code == 200
    assert len(response.json()) > 100


def test_top_collective():
    response = client.get("/top-collective/")
    assert response.status_code == 200
    assert len(response.json()) > 100


def test_individual_medals():
    response = client.get("/individual-medals/")
    assert response.status_code == 200
    assert len(response.json()) > 100


def test_top_individual():
    response = client.get("/top-indiviual/")
    assert response.status_code == 200
    assert len(response.json()) > 100


def test_select_country():
    response = client.get("/country/")
    assert response.status_code == 200
    assert len(response.json()) > 100
