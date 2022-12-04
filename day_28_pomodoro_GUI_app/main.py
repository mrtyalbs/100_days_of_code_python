from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(2 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60

    if count_sec <= 9:
        count_sec = f"0{count_sec}"

    if count_min <= 9:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(background=YELLOW, width=500, height=500, padx=100, pady=50)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
image_file = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image_file)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=2)

top_label = Label(font=(FONT_NAME, 50, "bold"), text="Timer", background=YELLOW, foreground=GREEN)
top_label.grid(column=1, row=1)

# Start Button
start_button = Button(text="Start", background="white", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

# Reset Button
reset_button = Button(text="Reset", background="white", highlightthickness=0)
reset_button.grid(column=2, row=3)

# Check Mark
checkmark = Label(text="✔", foreground=GREEN, background=YELLOW)
checkmark.grid(column=1, row=4)


window.mainloop()