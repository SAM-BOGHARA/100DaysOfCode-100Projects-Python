import email
import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from mysqlx import Result
import pyperclip

BGCOLOR = "#FFD365"

LIGHT_ORANGE = "#FDFFA9"
# ------------------------- PASSWORD GENERATOR  ---------------------------------------#
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
    pyperclip.paste()


# --------------------------SAVE PASSWORD --------------------------------------#


def save_password():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please enter all the fields")

    else:
        try:
            with open("INTERMEDIATE/day29/project/data.json", "r") as data_file:
                # reading old data_file
                data = json.load(data_file)
        except FileNotFoundError:
            with open("INTERMEDIATE/day29/project/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("INTERMEDIATE/day29/project/data.json", "w") as data_file:
                # saving updated data_file
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ----------------------------FIND PASSWORD-------------------------

def find_password():
    website = website_input.get().lower()
    try:
        with open("INTERMEDIATE/day29/project/data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title="Search Result", message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(
                title="Error", message=f"No Search result found \n resembling to {website}")


# --------------------------UI SETUP ----------------------------------------------#
# window
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=80, pady=80, bg=BGCOLOR)

# canvas
canvas = Canvas(width=200, height=200, bg=BGCOLOR, highlightthickness=0)
pass_image = PhotoImage(file="INTERMEDIATE/day29/project/password.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(row=0, column=0, columnspan=3)

# labels
website_label = Label(text="WEBSITE:",
                      bg=BGCOLOR, font=("Ariel", 14, "bold"))
website_label.grid(row=1, column=0)

email_label = Label(text="EMAIL/USERNAME:",
                    bg=BGCOLOR, font=("Ariel", 14, "bold"))
email_label.grid(row=2, column=0)

password_label = Label(text="PASSWORD:",
                       bg=BGCOLOR, font=("Ariel", 14, "bold"))
password_label.grid(row=3, column=0)


#  user entry point
website_input = Entry(width=21, bg=LIGHT_ORANGE, font=("Ariel", 25, "bold"))
website_input.grid(row=1, column=1)
website_input.focus()


email_input = Entry(width=36, bg=LIGHT_ORANGE, font=("Ariel", 25, "bold"))
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "shubhamboghara444@gmail.com")

password_input = Entry(width=21, bg=LIGHT_ORANGE, font=("Ariel", 25, "bold"))
password_input.grid(row=3, column=1)


# buttons

search_button = Button(text="Search", width=15, borderwidth=1,
                       bg=BGCOLOR, font=("Ariel", 21, "bold"), command=find_password)
search_button.grid(row=1, column=2)


generate_password_button = Button(text="GENERATE", bg=BGCOLOR, width=15, borderwidth=1,
                                  command=generate_password, font=("Ariel", 21, "bold"))
generate_password_button.grid(row=3, column=2)

add_button = Button(text="ADD TO CLIPBOARD", bg=BGCOLOR, width=32, borderwidth=1,
                    command=save_password, font=("Ariel", 25, "bold"))
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
