
from tkinter import *


window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New text"
my_label.config(text="New text")

# Button


def button_clicked():
    print("I got clicked")
    my_label.config(text="Button has been clicked")


button = Button(text="Click me", command=button_clicked)
button.pack()

input = Entry()
input.pack()


window.mainloop()