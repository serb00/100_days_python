import pytest
import requests_mock
import os
from main import get_workouts, post_workout, format_workout, process_query

NUTRTIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRTIONIX_API_KEY = os.environ.get("NUTRITIONIX_APP_KEY")
NUTRTIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT_GET = os.environ.get("SHEETY_ENDPOINT_GET")
SHEETY_ENDPOINT_POST = os.environ.get("SHEETY_ENDPOINT_POST")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")


# Mock environment variables
@pytest.fixture(autouse=True)
def mock_env_vars(monkeypatch):
    monkeypatch.setenv("NUTRITIONIX_APP_ID", NUTRTIONIX_APP_ID)
    monkeypatch.setenv("NUTRITIONIX_APP_KEY", NUTRTIONIX_API_KEY)
    monkeypatch.setenv("SHEETY_ENDPOINT_GET", SHEETY_ENDPOINT_GET)
    monkeypatch.setenv("SHEETY_ENDPOINT_POST", SHEETY_ENDPOINT_POST)
    monkeypatch.setenv("SHEETY_TOKEN", SHEETY_TOKEN)


# Test get_workouts function
def test_get_workouts():
    with requests_mock.Mocker() as m:
        m.get(SHEETY_ENDPOINT_GET, json={"workouts": []})
        response = get_workouts()
        assert response.status_code == 200
        assert response.json() == {"workouts": []}


# Test post_workout function
def test_post_workout():
    with requests_mock.Mocker() as m:
        m.post(SHEETY_ENDPOINT_POST, json={"workout": {"id": 1}}, status_code=201)
        response = post_workout({"workout": {}})
        assert response.status_code == 201


# Test format_workout function
def test_format_workout():
    workout = format_workout("Running", 30, 300)
    assert workout["workout"]["exercise"] == "Running"
    assert workout["workout"]["duration"] == 30
    assert workout["workout"]["calories"] == 300


# Test process_query function
def test_process_query():
    with requests_mock.Mocker() as m:
        m.post(NUTRTIONIX_ENDPOINT, json={"exercises": [{"name": "running", "duration_min": 30, "nf_calories": 300}]})
        results = process_query("ran 3 miles", {"Content-Type": "application/json"}, {"query": "ran 3 miles"})
        assert len(results) == 1
        assert results[0][0] == "Running"
        assert results[0][1] == 30
        assert results[0][2] == 300
