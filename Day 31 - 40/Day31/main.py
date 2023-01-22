
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

canvas = Canvas(height=800, width=526)

wrong_buttons = Button(image=wrong_image)
wrong_buttons.grid(row=1, column=1)
right_button = Button(image=right_image)
right_button.grid(row=1, column=2)


window.mainloop()