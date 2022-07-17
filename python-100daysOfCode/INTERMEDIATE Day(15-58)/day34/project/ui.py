from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Ariel", 15, "bold")
FONT_CANVAS = ("Ariel", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            text=f"Score: 0", fg="white", bg=THEME_COLOR, font=FONT)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text=f"a", fill=THEME_COLOR, font=FONT_CANVAS)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="INTERMEDIATE/day34/project/images/true.png")
        self.truebutton = Button(
            image=true_image, highlightthickness=0, borderwidth=0, command=self.true_pressed)
        self.truebutton.grid(row=2, column=0)
        false_image = PhotoImage(file="INTERMEDIATE/day34/project/images/false.png")
        self.falsebutton = Button(
            image=false_image, highlightthickness=0, borderwidth=0, command=self.false_pressed)
        self.falsebutton.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You have reached the end of the quiz")
            self.truebutton.config(state="disabled")
            self.falsebutton.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
