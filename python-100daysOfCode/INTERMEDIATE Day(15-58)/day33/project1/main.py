from tkinter import *
import requests as req

def get_quote():
    response = req.get(url = "https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text,text = quote,fill = "black")

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=450, height=500)
background_img = PhotoImage(file="INTERMEDIATE/day33/project1/background.png")
canvas.create_image(225, 250, image=background_img)
quote_text = canvas.create_text(225, 250, text="", width=250, font=("Arial", 22, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="INTERMEDIATE/day33/project1/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote,bd = 0)
kanye_button.grid(row=1, column=0)

window.mainloop()