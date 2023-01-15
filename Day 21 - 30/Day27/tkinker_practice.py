
from tkinter import *


window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New text"
my_label.config(text="New text")

# Button

input = Entry(width=10, )
input.pack()


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=f"{new_text}")


button = Button(text="Click me", command=button_clicked)
button.pack()


window.mainloop()