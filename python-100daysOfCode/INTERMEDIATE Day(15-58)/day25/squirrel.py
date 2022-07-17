import pandas as pd

data = pd.read_csv(
    "INTERMEDIATE/day25/228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])

red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
# print((gray_squirrel_count))
# print((red_squirrel_count))
# print((black_squirrel_count))


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

print(data_dict)

df = pd.DataFrame(data_dict)
print(df)
df.to_csv("INTERMEDIATE/day25/squirrel_count.csv")
