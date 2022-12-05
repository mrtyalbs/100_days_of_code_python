from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, background="white", width=600, height=600)

canvas = Canvas(width=200, height=200, highlightthickness=0, background="white")
image_file = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_file)
canvas.grid(column=1, row=0)

# Website input label
website_label = Label(text="Website :", background="white")
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.grid(column=1, columnspan=2, row=1, sticky="EW")

# E-mail username input
email_username_label = Label(text="E-mail / Username :", background="white",)
email_username_label.grid(column=0, row=2)
email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2, sticky="EW")

# Password label
password_label = Label(text="Password :", background="white")
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")
password_generate_button = Button(text="Generate Password")
password_generate_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")





window.mainloop()