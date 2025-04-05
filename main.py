import turtle
import pandas

"""Write name of states or type "exit" :keyword to comeout from this game"""

screen = turtle.Screen()
screen.title("U.S Sates Game")
image ="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) <50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 State Correct",
                                    prompt= "what's another state's name?").title()
    if answer_state == "Exit":    #Type Exit Keyword to exit the game

        """Here we will make a file that contains the states which has not been guessed"""
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)





