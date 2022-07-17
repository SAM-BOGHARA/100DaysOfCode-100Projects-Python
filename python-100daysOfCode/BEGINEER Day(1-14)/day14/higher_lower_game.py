
# display art
from os import name
from re import A, T
from art import logo, vs
from game_data import data
import random
import os


def clear(): return os.system("cls")


def format_data(account):
    # format the account data
    account_name = account["name"]
    account_dis = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_dis}, from {account_country}")


def check_answer(guess, a_followers, b_followers):
    # check if the user is correct # #  get follower count of each account # # use if statement to check if user is correct
    # 1st approach
    # if a_followers > b_followers and guess == "a":
    #     print("correct")
    # elif a_followers < b_followers and guess == "a":
    #     print("wrong")
    # elif a_followers < b_followers and guess == "b":
    #     print("correct")
    # elif a_followers > b_followers and guess == "b":
    #     print("wrong")
    # 2nd approach
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
account_b = random.choice(data)

game_continues = True
# make the game repeatablea

while game_continues:
    # genearte random account from game data
    # making account at pos B become the next account at pos A
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # ask the user for the guess
    guess = input("Who has more followers? Type 'a' or 'b' :").lower()
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    is_correct = check_answer(guess, a_followers, b_followers)

    clear()
    print(logo)
    # give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right, Current Score : {score}")
    else:
        game_continues = False
        print(f"Oops! Game over, Final Score : {score}")


# clear the screen
