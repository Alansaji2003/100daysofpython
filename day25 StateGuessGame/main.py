from turtle import Screen
from turtle import Turtle
import pandas
import csv

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)

t_image = Turtle()
t_image.shape(image)
write = Turtle()
write.hideturtle()

data = pandas.read_csv("50_states.csv")
states_data = data["state"].to_list()

lower_state = []  # array to store the states in lower case
guessed = []  # array for storing the user guesses

for x in states_data:
    x = x.lower()
    lower_state.append(x)
print(lower_state)


def showText():
    user_input = screen.textinput(title="Guess the State", prompt="Type any state to mark on the map")
    guessed.append(user_input.lower())
    if user_input.lower() == "exit":
        for guess in guessed:
            for state in lower_state:
                if guess == state:
                    lower_state.remove(state)

        new_data = pandas.DataFrame(lower_state)
        new_data.to_csv("states_to_learn.csv")
        exit()
    while user_input.lower() in lower_state:

        for state in states_data:

            if user_input.lower() == state.lower():
                x_cor_data = data[data.state == state]
                xcor = x_cor_data.x.iloc[0]  # we can use xcor = int(x_corl.x)

                y_cor_data = data[data.state == state]
                ycor = y_cor_data.y.iloc[0]

                write.penup()
                write.goto(xcor, ycor)
                write.write(f"{state}", move=False, font=("Lilita One", 10, "normal"))
                showText()


showText()


