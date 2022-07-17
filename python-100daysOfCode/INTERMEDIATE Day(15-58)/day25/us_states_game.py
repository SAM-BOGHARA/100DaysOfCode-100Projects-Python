import turtle as t
import pandas as pd
FONT = ("Ariel", 9, "bold")

data = pd.read_csv("INTERMEDIATE/day25/50_states.csv")

all_states = data.state.to_list()
# print(all_states)

screen = t.Screen()
screen.title("U.S States Game")

image = "INTERMEDIATE/day25/blank_states_img.gif"
screen.addshape(image)
t.shape(image)

guessed_states = []

while len(guessed_states) <= 50:

    answer = screen.textinput(title=f"States guessed:{len(guessed_states)}/50",
                              prompt="What's another state name?").title()
    if answer == "Exit":
        missing_states = [
            state for state in all_states if state not in guessed_states]
        states_to_learn = pd.DataFrame(missing_states)
        states_to_learn.to_csv("INTERMEDIATE/day25/states_to_learn.csv")
        break
    # if answer == "Exit":
    #     missing_states = []
    #     for state in all_states:
    #         if state not in guessed_states:
    #             missing_states.append(state)
        # states_to_learn = pd.DataFrame(missing_states)
        # states_to_learn.to_csv("INTERMEDIATE/day25/states_to_learn.csv")
        # break

    if answer in all_states:
        guessed_states.append(answer)
        tom = t.Turtle()
        tom.hideturtle()
        tom.penup()
        state_data = data[data.state == answer]
        tom.goto(int(state_data.x), int(state_data.y))
        tom.write(f"{answer}", font=FONT)

# states to learn .csv
