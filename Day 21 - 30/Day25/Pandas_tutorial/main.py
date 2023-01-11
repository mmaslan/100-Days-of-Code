# Pandas tutorial

# with open("weather_data.csv") as file:
#     content = file.readlines()
#     data = [i.strip("\n") for i in content]
#
# print(data)


# import csv
#
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#
# print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")

# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)


# def average(lst):
#     sum_of_list = 0
#     for i in range(len(lst)):
#         sum_of_list += lst[i]
#     avg = sum_of_list/len(lst)
#     return avg
#
#
# print(round(average(temp_list), 2))

# print(round(data["temp"].mean(), 2))
# print(data["temp"].max())

# Get data in Columns
# print(data["condition"])
# print(data.condition)

# Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# Extract data
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp_F = int(monday.temp) * 9/5 + 32
# print(monday_temp_F)

# Create a dataframe from stratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")