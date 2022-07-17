import random

# test_seed = int(input("create a seed number :\n"))
# random.seed(test_seed)

name_input = input("Give me everybody's name,separated by commas.")
names = name_input.split(", ")
no_of_people = len(names)
choice = random.randint(0, no_of_people - 1)
person = names[choice]
print(person + " will pay the bill for meal")
# person_pay = random.choice(names)
# print(person_pay + " will pay the bill for meal")
