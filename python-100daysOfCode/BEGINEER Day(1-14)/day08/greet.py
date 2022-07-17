name = input("What is your name: ")
location = input("whre are you located: ")
# name is paramter

# def greet(name):
#     print(f"Greetings {name}!!")
#     print(f"{name} I hope you are fine.")
#     print("Let's get started")


# # "shubham" is argument
# greet("shubham")
# greet(name)

def Greet(name, location):
    print(f"Hello {name}")
    print(f"I hope you are doing fine in {location}")


Greet(name = "shubham", location = "mumbai")
Greet(name,location)
