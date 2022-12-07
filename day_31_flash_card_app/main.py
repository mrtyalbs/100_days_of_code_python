from tkinter import *
import pandas
from random import choice


BACKGROUND_COLOR = "#B1DDC6"

# Read data from csv file
try:
    french_words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_words_data = pandas.read_csv("data/french_words.csv")
finally:
    french_words_dict = french_words_data.to_dict(orient="records")

current_card = {}


# ------------------------------ GENERATE RANDOM CARD ------------------------------#
def next_card():
    global flip_timer, current_card

    window.after_cancel(flip_timer)

    current_card = choice(french_words_dict)
    french_word = current_card["French"]

    canvas.itemconfig(card_background, image=card_front_image)
    canvas.itemconfig(word_text, text=french_word, fill="black")
    canvas.itemconfig(language_text, text="French", fill="black")

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card

    current_card = choice(french_words_dict)
    english_word = current_card["English"]

    canvas.itemconfig(card_background, image=card_back_image)
    canvas.itemconfig(word_text, text=english_word, fill="white")
    canvas.itemconfig(language_text, text="English", fill="white")

def is_known():
    french_words_dict.remove(current_card)
    data = pandas.DataFrame(french_words_dict)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()



# ------------------------------ UI SETUP ------------------------------#
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Card setup
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
language_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=1, row=1, columnspan=2)

# Buttons setup
image_right = PhotoImage(file="images/right.png")
button_right = Button(image=image_right, highlightthickness=0, background=BACKGROUND_COLOR, command=is_known)
button_right.grid(column=2, row=2)

image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, background=BACKGROUND_COLOR, command=next_card)
button_wrong.grid(column=1, row=2)

next_card()


window.mainloop()
