import unittest
from unittest.mock import patch
from main import get_workouts, post_workout, format_workout, process_query


class TestMain(unittest.TestCase):
    @patch("requests.get")
    def test_get_workouts(self, mock_get):
        mock_response = {"workouts": [{"date": "01/01/2022", "time": "12:00:00", "exercise": "Running",
                                       "duration": 30, "calories": 300}]}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        response = get_workouts()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), mock_response)

    @patch("requests.post")
    def test_post_workout(self, mock_post):
        mock_workout = {"workout": {"date": "01/01/2022", "time": "12:00:00", "exercise": "Running",
                                    "duration": 30, "calories": 300}}
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_workout
        response = post_workout(mock_workout)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), mock_workout)

    def test_format_workout(self):
        exercise = "Running"
        duration = 30
        calories = 300
        expected_output = {"workout": {"date": "01/01/2022", "time": "12:00:00", "exercise": "Running",
                                       "duration": 30, "calories": 300}}
        with patch("main.dt") as mock_dt:
            mock_dt.datetime.now.return_value.strftime.side_effect = ["01/01/2022", "12:00:00"]
            output = format_workout(exercise, duration, calories)
            self.assertEqual(output, expected_output)

    @patch("requests.post")
    def test_process_query(self, mock_post):
        mock_response = {"exercises": [{"name": "Running", "duration_min": 30, "nf_calories": 300}]}
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response
        query = "ran 3 miles"
        headers = {"x-app-id": "test_id", "x-app-key": "test_key", "Content-Type": "application/json"}
        parameters = {"query": query, "gender": "male", "weight_kg": 60, "height_cm": 180, "age": 35}
        expected_output = [("Running", 30, 300)]
        with patch("main.dt") as mock_dt:
            mock_dt.datetime.now.return_value.strftime.side_effect = ["01/01/2022", "12:00:00"]
            output = process_query(query, headers, parameters)
            self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
