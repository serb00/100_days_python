# # example without any libraries
# # with open("weather-data.csv", mode="r") as file:
# #     lines = file.readlines()
# #     for line in lines:
# #         print(line.strip())
#
# # example using csv library
# # import csv
# #
# # with open("weather-data.csv", mode="r") as file:
# #     data = csv.reader(file)
# #     temperatures: list[int] = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# # example using pandas library
# import pandas
#
# data = pandas.read_csv("weather-data.csv")
# # temperatures = data["temp"].to_list()
# # average_temp = sum(temperatures) / len(temperatures) if temperatures else 0
# print(data["temp"].mean())  # average of temp column by pandas
# print(data["temp"].max())  # max of temp column by pandas
# print(data.temp.max())  # max of temp column by pandas
# print(data[data.day == "Monday"])  # get the row where day equal to "Monday"
# print(data[data.temp == data.temp.max()])  # get the row where the temperature is the max
# print((int(data[data.day == "Monday"].temp[0]) * 9/5) + 32)  # get temperature on Monday in Fahrenheit

import pandas

# # clever way
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231022.csv")
# aggr = data.groupby("Primary Fur Color").size().reset_index(name="Count")
# aggr.to_csv("squirrels_by_color.csv")

# straightforward way
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231022.csv")
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])

aggr_dict = {
    "Fur color": ["Black", "Gray", "Cinnamon"],
    "Count": [black_squirrels, gray_squirrels, cinnamon_squirrels]
}

aggr = pandas.DataFrame(aggr_dict)
print(aggr)
