# print("Welcome to the rollercoster!")
# height = int(input("What is your height in cm : "))
# # age = int(input("What is your age: "))
# # if height >= 170:
# #     print("Congratulations ! You can ride.")
# #     if age > 18:
# #         print("Your Ride fees is 12$")
# #     else:
# #         print("Since you are minor,Your Ride fees is 7$")
# # else:
# #     print("Oops! You cannot ride.")

# #nested  elif
# if height >= 170:
#     print("Congratulations ! You can ride.")
#     age = int(input("What is your age: "))
#     if age > 18:
#         print("Your Ride fees is 12$")
#     elif age > 12:
#         print("Your Ride fees is 7$")
#     else:
#         print("Your fees is 5$")
# else:
#     print("Oops! You cannot ride.")

# #exercise:1

# height = input("enter you height : ")
# weight = input("enter your weight : ")
# bmi = (float(weight)/float(height)**2)
# print(bmi)
# if bmi <= 18.5:
#     print(f"Your BMI is {bmi},you are slightly underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi},you have a normal weight")
# elif bmi < 30:
#     print(f"Your BMI is {bmi},you are slightly overweight")
# elif bmi <  35:
#     print(f"Your BMI is {bmi},you are obese")
# else:
#     print(f"Your BMI is {bmi},you are clinically obese")

# exercise : 2
# height = int(input("What is your height in cm : "))
# bill = 0
# if height >= 170:
#     print("Congratulations ! You can ride.")
#     age = int(input("What is your age: "))
#     if age > 18:
#         bill = 12
#         print(f"Your Ride fees is ${bill}")
#     elif age > 12:
#         bill = 7
#         print(f"Your Ride fees is ${bill}")
#     else:
#         bill = 5
#         print(f"Your fees is ${bill}")
#     photo = input("Do you want photo? Y or N ?")
#     if photo == "Y":
#         bill = bill + 3
#         # bill += 3
#     print(f"Your final bill is ${bill}")
# else:
#     print("Oops! You cannot ride.")

# exercise logical operators
height = int(input("What is your height in cm : "))

if height >= 170:
    print("Congratulations ! You can ride.")
    age = int(input("What is your age: "))
    if age < 12:
        print("Your Ride fees is 5$")
    elif age <= 18:
        print("Your Ride fees is 7$")
    elif age >= 45 and age <= 55:
        bill = 0
        print(f"Your Ride fees is ${bill},Everything will be fine.")
    else:
        print("Your fees is 12$")
else:
    print("Oops! You cannot ride.")
