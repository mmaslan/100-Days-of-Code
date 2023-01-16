
from tkinter import *


window = Tk()
window.title("Converter")
window.minsize(width=500, height=300)

my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "Convert the miles to kilometers."
my_label.config(text="Convert the miles to kilometers.")

input = Entry(width=10, )
input.pack()


def button_converter():
    miles = float(input.get())
    result = float(miles) * 1.609
    my_label.config(text=f"{miles} is {result} km.")


button = Button(text="Convert", command=button_converter)
button.pack()


window.mainloop()