import random
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# function to check user's guess against the actual answer


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it correct.The answer was {answer}")


# make a function to set difficulty

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # choosing random number between 1 and 100
    answer = random.randint(1, 100)
    s = "Welcome to the Number Guessing Game!"
    print(art.logo)
    s = s.center(100, '*')
    print("\n" + s + "\n")
    print("I'm thinking of a number 1 and 100")

    turns = set_difficulty()

    # repeat guessing functionality
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the answer.")
        # let the user guess the number
        guess = int(input("Make a Guess:> "))
        turns = check_answer(guess, answer, turns)

        # track the number of attempts
        if turns == 0:
            print("You have run out of guesses. You Lose")
            print(f"Correct answer was {answer}")
            return


game()
