import requests
import os
import datetime as dt

GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 180
AGE = 35


NUTRTIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRTIONIX_API_KEY = os.environ.get("NUTRITIONIX_APP_KEY")
NUTRTIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT_GET = os.environ.get("SHEETY_ENDPOINT_GET")
SHEETY_ENDPOINT_POST = os.environ.get("SHEETY_ENDPOINT_POST")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

query_headers = {
    "x-app-id": NUTRTIONIX_APP_ID,
    "x-app-key": NUTRTIONIX_API_KEY,
    "Content-Type": "application/json",
}
query_parameters = {
    "query": "ran 3 miles",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}


def get_workouts():
    """Get workouts from sheety
    :rtype: Response
    """
    response = requests.get(url=SHEETY_ENDPOINT_GET, headers=sheety_headers)
    response.raise_for_status()
    return response


def post_workout(workout):
    """Post workout to sheety
    :param workout:
    :type workout: dict
    :rtype: Response
    """
    response = requests.post(url=SHEETY_ENDPOINT_POST,
                             json=workout,
                             headers=sheety_headers)
    response.raise_for_status()
    return response


def format_workout(exercise, duration, calories):
    """Format workout
    :param exercise:
    :type exercise: str
    :param duration:
    :type duration: int
    :param calories:
    :type calories: int
    :rtype: dict
    """
    return {
        "workout": {
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }


def process_query(query, headers, parameters):
    """Process the query
    :param parameters:
    :type parameters: dict
    :param headers:
    :type headers: dict
    :param query:
    :type query: str
    """
    parameters["query"] = query
    response = requests.post(
        url=NUTRTIONIX_ENDPOINT,
        json=parameters,
        headers=headers
    )
    response.raise_for_status()
    results = []
    print("Your workout for today:")
    for exercise in response.json()["exercises"]:
        exercise_name = exercise["name"].title()
        exercise_duration = exercise["duration_min"]
        exercise_calories = exercise["nf_calories"]
        results.append((exercise_name, exercise_duration, exercise_calories))
        print(f"{exercise_name}: {exercise_duration} minutes, "
              f"{exercise_calories} calories burned")
    return results


if __name__ == "__main__":
    activities = process_query(input("What did you do today? "),
                               query_headers,
                               query_parameters)
    print()
    for activity in activities:
        resp = post_workout(format_workout(*activity))
        print(f"Workout {activity[0]} for {activity[2]} cal "
              f"was posted to sheety")
