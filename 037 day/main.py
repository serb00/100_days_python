import os
import requests
import datetime as dt
from icecream import ic

# Constants
PIXELA_USER = os.environ.get("PIXELA_USER")
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
CURRENT_GRAPH_ID = "graph1"
DATE_FORMAT = "%Y%m%d"


def create_user(token=PIXELA_TOKEN,
                username=PIXELA_USER,
                agree_terms_of_service="yes",
                not_minor="yes"):
    """Create a user"""
    pixela_endpoint = "https://pixe.la/v1/users"
    parameters = {
        "token": token,
        "username": username,
        "agreeTermsOfService": agree_terms_of_service,
        "notMinor": not_minor,
    }

    response = requests.post(url=pixela_endpoint, json=parameters)
    return response.json()


def create_graph(graph_id=CURRENT_GRAPH_ID,
                 name="Coding Graph",
                 unit="hours",
                 unit_type="float",
                 color="ajisai",
                 token=PIXELA_TOKEN):
    """Create a graph"""
    graph_endpoint = f"https://pixe.la/v1/users/{PIXELA_USER}/graphs"
    headers = {
        "X-USER-TOKEN": token,
    }
    parameters = {
        "id": graph_id,
        "name": name,
        "unit": unit,
        "type": unit_type,
        "color": color,
    }

    response = requests.post(url=graph_endpoint, json=parameters, headers=headers)
    return response.json()


def post_pixel(date="20231115",
               quantity="2.5",
               token=PIXELA_TOKEN,
               graph_id=CURRENT_GRAPH_ID):
    """Post a pixel to a graph"""
    pixel_endpoint = f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/{graph_id}"
    headers = {
        "X-USER-TOKEN": token,
    }
    parameters = {
        "date": date,
        "quantity": quantity,
    }

    response = requests.post(url=pixel_endpoint, json=parameters, headers=headers)
    return response.json()


def change_graph_parameter(param_name="color",
                           param_value="sora",
                           token=PIXELA_TOKEN,
                           graph_id=CURRENT_GRAPH_ID):
    """Change a graph parameter (color, name, unit, type) to a new value"""
    graph_endpoint = f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/{graph_id}"
    headers = {
        "X-USER-TOKEN": token,
    }
    parameters = {
        param_name: param_value,
    }
    response = requests.put(url=graph_endpoint, json=parameters, headers=headers)
    return response.json()


def delete_pixel(date="20231115",
                 token=PIXELA_TOKEN,
                 graph_id=CURRENT_GRAPH_ID):
    """Delete a pixel from a graph"""
    pixel_endpoint = f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/{graph_id}/{date}"
    headers = {
        "X-USER-TOKEN": token,
    }
    response = requests.delete(url=pixel_endpoint, headers=headers)
    return response.json()


def update_pixel(date="20231115",
                 quantity="1.5",
                 token=PIXELA_TOKEN,
                 graph_id=CURRENT_GRAPH_ID):
    """Update a pixel in a graph"""
    pixel_endpoint = f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/{graph_id}/{date}"
    headers = {
        "X-USER-TOKEN": token,
    }
    parameters = {
        "quantity": quantity,
    }
    response = requests.put(url=pixel_endpoint, json=parameters, headers=headers)
    return response.json()


# Main program
if __name__ == "__main__":
    day = dt.datetime(year=2023, month=11, day=15)
    formatted_date = day.strftime(DATE_FORMAT)
    success = False
    while not success:  # Keep trying until success
        result = update_pixel(date=formatted_date, quantity="3.5")
        success = result["isSuccess"]
        ic(result["message"])
