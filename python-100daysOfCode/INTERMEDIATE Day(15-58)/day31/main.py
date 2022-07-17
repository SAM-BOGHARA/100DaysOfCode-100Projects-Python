from tkinter import *
from matplotlib.pyplot import fill
import pandas as pd
import random
import time

BGCOLOR = "#F9F9F9"
TITLE_FONT = ("Ariel", 35, "italic")
WORD_FONT = ("Arial", 50, "bold")
current_card = {}
to_learn = {}
try:
    data = pd.read_csv("INTERMEDIATE/day31/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv(
        "INTERMEDIATE/day31/data/english--hindi--flashy.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card["French"])
    canvas.itemconfig(card_title, text="HINDI", fill="black")
    canvas.itemconfig(card_word, text=current_card["HINDI"], fill="black")
    canvas.itemconfig(card_background, image=front_card)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="ENGLISH", fill="white")
    canvas.itemconfig(card_word, text=current_card["ENGLISH"], fill="white")
    canvas.itemconfig(card_background, image=back_card)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("INTERMEDIATE/day31/data/words_to_learn.csv", index=False)

    next_card()


window = Tk()
window.title("Flash Card")
window.config(padx=10, pady=20, bg=BGCOLOR)

flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=900, height=450)
front_card = PhotoImage(file="INTERMEDIATE/day31/images/label_front.png")
back_card = PhotoImage(file="INTERMEDIATE/day31/images/back_label.png")
card_background = canvas.create_image(450, 250, image=front_card)
card_title = canvas.create_text(450, 200, text="", font=TITLE_FONT)
card_word = canvas.create_text(450, 270, text="", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BGCOLOR, highlightthickness=0)

wrong_image = PhotoImage(file="INTERMEDIATE/day31/images/wrong_image.png")
wrong_button = Button(image=wrong_image, highlightthickness=0,
                      bg=BGCOLOR, border=0, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="INTERMEDIATE/day31/images/right_image.png")
right_button = Button(image=right_image, highlightthickness=0,
                      bg=BGCOLOR, border=0, borderwidth=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()


window.mainloop()
