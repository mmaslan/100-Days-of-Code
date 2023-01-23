
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
french_word = data.French.to_dict()


def random_text():
    current_card = random.choice(dict(french_word))
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card)


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="text", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage

wrong_image = PhotoImage(file="images/wrong.png")
wrong_buttons = Button(image=wrong_image, highlightthickness=0, command=random_text)
wrong_buttons.grid(row=1, column=0)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=random_text)
right_button.grid(row=1, column=1)


window.mainloop()