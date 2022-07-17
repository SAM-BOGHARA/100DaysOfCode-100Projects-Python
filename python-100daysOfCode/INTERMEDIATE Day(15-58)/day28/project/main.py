
from tkinter import *
import math

# -----------------------------CONSTANTS-----------------------------------#

PINK = "#FFAFAF"
RED = "#FF1700"
GREEN = "#06FF00"
YELLOW = "#FFE162"
FONT_NAME = "Courier"
BUTTON_FONT = ("Courier", 15, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repss = 0
timer = None
# -----------------------------TIMER RESET--------------------------------#


def reset_timer():
    window.after_cancel(timer)
    # timer text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title label == "Timer
    timer_label.config(text="Timer")
    # reset check_marks
    check_marks.config(text="")


# -----------------------------TIMER MECHANISM------------------------------#


def start_timer():
    global repss
    repss += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if its the 8th repo
    if repss % 8 == 0:
        timer_label.config(text="BREAK", fg=RED)
        count_down(long_break_sec)
    # if its 2nd ,4th,6th rep:
    elif repss % 2 == 0:
        timer_label.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
    else:
        # if its 1st/3rd/5th/7th repss
        timer_label.config(text="WORK", fg=GREEN)
        count_down(work_sec)


# -----------------------------COUNTDOWN MECHANISM ------------------------------#

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(repss / 2)
        for i in range(work_sessions):
            mark += "✅"
        check_marks.config(text=mark)


# -----------------------------UI SETUP MECHANISM ------------------------------#
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", font=(
    FONT_NAME, 44, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=1, column=2)


canvas = Canvas(width=550, height=450, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="INTERMEDIATE/day28/tomato.png")
canvas.create_image(280, 230, image=tomato_img)
canvas.grid(row=2, column=2)
timer_text = canvas.create_text(280, 230, text="00:00", justify="center",
                                font=(FONT_NAME, 50, "bold"), fill=YELLOW)

start_button = Button(text="Start", font=BUTTON_FONT, fg=RED, bg=YELLOW,
                      command=start_timer)
start_button.grid(padx=28, pady=28, row=3, column=1)
start_button.config(width=10, height=3)

reset_button = Button(text="Reset", font=BUTTON_FONT, fg=RED, bg=YELLOW,
                      command=reset_timer)
reset_button.grid(padx=28, pady=28, row=3, column=3)
reset_button.config(width=10, height=3)

# ✔️✅
check_marks = Label(font=BUTTON_FONT, fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=2)
check_marks.config(width=10, height=3)

window.mainloop()
