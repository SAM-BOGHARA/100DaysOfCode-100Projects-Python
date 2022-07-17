from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result.config(text=f"{km}")


# Creating a new window and configurations
window = Tk()
window.title("  MILES TO KM  ")
window.minsize(width=120, height=120)
window.config(padx=30, pady=30)


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="Is Equal to")
is_equal_label.grid(column=0, row=1)


kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

kilometers_label = Label(text="Kilometers")
kilometers_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate",command = miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
