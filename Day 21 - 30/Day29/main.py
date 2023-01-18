
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", text="Perhaps you typed wrong website or password")
    else:
        messagebox.askokcancel(title=website, message="Data uploaded to text_file")
        # is_ok = messagebox.askokcancel(title=website, message="Data uploaded to text_file")
        # if is_ok:
        with open("data.txt", "w") as data_file:
            data_file.write(f"Website: {website} / email: {email} / password: {password}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "xxx@gmail.com")
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)


gen_button = Button(text="Generate Password")
gen_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()