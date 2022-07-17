# exercise 1

sentence = "Its not who i am underneath but what i do that defines me"

lister = [item for item in sentence.split()]
# print(list)

count_dict = {word: len(word) for word in lister}
print(count_dict)

# exercise 2
weather_c = {
    "Monday": 12, "Tuesday": 14, "Wednesday": 14, "Thursday": 20, "Friday": 21, "Saturday": 16, "Sunday": 22
}

weather_f = {
    day : temp_c*9/5 + 32  for (day,temp_c) in weather_c.items()
}
print(weather_f)

