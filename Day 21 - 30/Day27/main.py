
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


def button_converter(km=1.6):
    miles = input.get()
    if miles == int:
        result = float(miles) * km
        my_label.config(text=f"{miles} is {result} km.")
    else:
        my_label.config(text=f"Please enter correct number.")


button = Button(text="Convert", command=button_converter)
button.pack()


window.mainloop()