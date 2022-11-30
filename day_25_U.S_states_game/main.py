import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



states_data = pandas.read_csv("50_states.csv")
state_list = states_data.state.to_list()
guessed_states = []
score = 0

while len(guessed_states) < 50 :
    user_answer = screen.textinput(f"Guess the state ({score}/50)", "What's another state's name?").title()

    if user_answer in state_list:
        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        state_data = states_data[states_data.state == user_answer]
        text.goto(int(state_data.x), int(state_data.y))
        text.write(user_answer)
        guessed_states.append(user_answer)
        score += 1

    if user_answer == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break




