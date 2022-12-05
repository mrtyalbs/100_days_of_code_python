from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    if len(password_input.get()) > 0:
        password_input.delete(0, END)
        password_input.insert(0, password)
    else:
        password_input.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_datas():
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"This are the details entered : \nEmail/Username : {email_username} \nPassword : {password} \nIs it OK to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email_username} | {password}\n")

            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, width=600, height=600)

# Canvas setup
canvas = Canvas(width=200, height=200, highlightthickness=0)
image_file = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_file)
canvas.grid(column=1, row=0)

# Website input label
website_label = Label(text="Website :")
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, columnspan=2, row=1, sticky="EW")

# E-mail username input
email_username_label = Label(text="E-mail / Username :")
email_username_label.grid(column=0, row=2)
email_username_input = Entry(width=35)
email_username_input.insert(END, "muratalbas@outlook.com")
email_username_input.grid(column=1, row=2, columnspan=2, sticky="EW")

# Password label
password_label = Label(text="Password :")
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")
password_generate_button = Button(text="Generate Password", command=generate_password)
password_generate_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", width=36, command=save_datas)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
