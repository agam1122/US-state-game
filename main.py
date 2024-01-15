import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
guessed_states = []
while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed correctly", prompt="What's "
                                                                                                       "another "
                                                                                                       "state's "
                                                                                                       "name?").title()
    state_list = data['state'].to_list()

    if answer_state == "Exit":
        break
    if answer_state in guessed_states:
        continue
    elif answer_state in state_list:
        timmy = turtle.Turtle()
        timmy.penup()
        timmy.hideturtle()
        state_data = data[data.state == answer_state]
        timmy.goto(int(state_data.x), int(state_data.y))
        timmy.write(answer_state)
        guessed_states.append(answer_state)

turtle.mainloop()
