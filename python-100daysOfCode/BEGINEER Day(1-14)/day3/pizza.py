print("Welcome to Python pizza corner!!")
size = input("What pizza size do you want? S , M, L ?")
pepp = input("Do you want Pepperoni? Y or N ?")
cheese = input("Do you want extra cheese? Y or N ?")
bill = 0
# if size == "S":
#     bill = 15
#     if pepp == "Y":
#         bill += 2
#     if cheese == "Y":
#         bill += 1
#     print(f"Your bill is ${bill}")

# if size == "M":
#     bill = 20
#     if pepp == "Y":
#         bill += 3
#     if cheese == "Y":
#         bill += 1
#     print(f"Your bill is ${bill}")

# if size == "L":
#     bill = 25
#     if pepp == "Y":
#         bill += 2
#     if cheese == "Y":
#         bill += 1
#     print(f"Your bill is ${bill}")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Incorrect input.Try S,M,L")

if pepp == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if cheese == "Y":
    bill += 1

print(f"Your bill is ${bill}")
