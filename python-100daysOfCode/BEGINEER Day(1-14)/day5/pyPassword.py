# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# map = [letters,numbers,symbols]
s = "Welcome to the PyPassword Generator!"
s = s.center(100,'*')

print("\n" + s + "\n")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# code below
# password = ""

# for i in range(1, nr_letters + 1):
#      password += random.choice(letters)

# for i in range(1, nr_symbols + 1):
#      password += random.choice(symbols)

# for i in range(1, nr_numbers + 1):
#      password += random.choice(numbers)

# print (password)

# Hard Level - Order randomised:
# e.g. 4 letter, 2 symbol, 2 number = Jd2uE&3#

password_list = []

for i in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for i in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for i in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

# print(password_list)


password = ""

for s in password_list:
    password += s


print(f"Your secured password is {password}")
