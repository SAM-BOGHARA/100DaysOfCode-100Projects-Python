

# with open("C:/Users/Harshit Boghara/vs_codeProjects/python-100daysOfCode/INTERMEDIATE/day25/weather_data.csv") as read_data:
#     lines = read_data.readlines()
#     print(lines)
#     for line in lines:
#         stripped_line = line.strip()
#         print(stripped_line)


# csv inbuilt module in python
# import csv

# with open("C:/Users/Harshit Boghara/vs_codeProjects/python-100daysOfCode/INTERMEDIATE/day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data) <_csv.reader object at 0x0000022655591E20>
#     day = []
#     temperature = []
#     condition = []
#     for row in data:
#         if row[0] != "day":
#             day.append(row[0])
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#         if row[2] != "condition":
#             condition.append(row[2])
#     print(day)
#     print(temperature)
#     print(condition)


# one of the best library in python for data analysis
import pandas as pd

data = pd.read_csv(
    "C:/Users/Harshit Boghara/vs_codeProjects/python-100daysOfCode/INTERMEDIATE/day25/weather_data.csv")
print(type(data))

print(data["day"],
      data["temp"],
      data["condition"])

print(type(data["day"]),
      type(data["temp"]),
      type(data["condition"]))


data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)
print(len(temp_list))


avg = sum(temp_list) / len(temp_list)
print(avg)

print(data["temp"].mean())
print(data["temp"].median())
print(data["temp"].mode())

print(data["temp"].max())
print(data.condition)

# get data in row ,, from row perspective
print(data[data.day == "Monday"])
print(data[data.temp == 24])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)


monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
print(monday_temp * 9/5 + 32)


# Create a dataframe from scratch

data_dict = {
    "students": ["amy", "james", "angela"],
    "scores": [76, 56, 65]
}


data = pd.DataFrame(data_dict)
print(data)
data.to_csv("C:/Users/Harshit Boghara/vs_codeProjects/python-100daysOfCode/INTERMEDIATE/day25/new_data.csv")