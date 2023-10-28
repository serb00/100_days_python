from icecream import ic
# def read_file(file_path):
#     with open(file_path, mode="r") as file:
#         lines = file.readlines()
#         return [int(x) for x in lines]
#
#
# file1: list[int] = read_file("file1.txt")
# file2: list[int] = read_file("file2.txt")
#
# result = [x for x in file1 if x in file2]
#
# print(result)

# import random
#
# names = ["Alex", "Beth", "Caroline", "Eleanor", "Fred", "Greg"]
# student_scores = {name: random.randint(1,100) for name in names}
# print(student_scores)
# passed_students = {key: value for (key, value) in student_scores.items() if value > 70}
# print(passed_students)

# sentence = "What is the airspeed velocity of an unladen swan?"
# result = {word: len(word) for word in sentence.split()}
# ic(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
ic(weather_f)
