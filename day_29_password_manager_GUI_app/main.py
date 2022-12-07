from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


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
    new_data = {
        website: {
            "e-mail": email_username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading the old data
                data = json.load(data_file)
                # Updating the old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Writing the new data
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                # Saving the updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if website in data:
                email = data[website]["e-mail"]
                password = data[website]["password"]
                messagebox.showinfo(website, f"E-mail/Username: {email} \nPassword: {password}")
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found!")

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
website_input = Entry(width=21)
website_input.focus()
website_input.grid(column=1, row=1, sticky="EW")

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

# Search button
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

window.mainloop()
