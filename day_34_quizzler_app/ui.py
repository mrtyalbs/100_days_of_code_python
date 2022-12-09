import time
from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class UI():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        # UI setup
        self.window = Tk()
        self.window.title = "Quizzler"
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        # Canvas
        self.canvas = Canvas(height=250, width=300, background="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        image_false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=image_false, highlightthickness=0, command=self.false_button_pressed)
        self.false_button.grid(column=1, row=2)
        image_true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=image_true, highlightthickness=0, command=self.true_button_pressed)
        self.true_button.grid(column=0, row=2)

        # Canvas text
        self.question_text = self.canvas.create_text(150, 125, font=("Arial", 13, "italic"), text=f"question text", width=280)

        # Score table
        self.score = Label(text=f"Score: 0", background=THEME_COLOR, foreground="white")
        self.score.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(background="white")
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(background="white")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")

    def true_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")

        else:
            self.canvas.config(background="red")

        self.window.after(1000, self.get_next_question)
