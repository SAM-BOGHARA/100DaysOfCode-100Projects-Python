from tkinter import *


def button_clicked():
    new_text = (input.get())
    my_label.config(text=new_text)


window = Tk()
window.title('gui program')
window.minsize(width=800, height=500)
window.config(padx=100, pady=200)
# label
my_label = Label(text="label", font=("Ariel", 24, "normal"))
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)


# button
button = Button(text="Check data", font=("Ariel", 24, "normal"),
                justify="center", activeforeground="green", activebackground="yellow", command=button_clicked)
button.grid(row=1, column=1)

button = Button(text="Check data", font=("Ariel", 24, "normal"),
                justify="center", activeforeground="green", activebackground="yellow", command=button_clicked)
button.grid(row=0, column=2)
# entry
input = Entry(width=40)
print(input.get())
input.grid(row=2, column=3)


window.mainloop()
