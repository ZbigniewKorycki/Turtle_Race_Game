from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(
    title="Make your bets",
    prompt="Which turtle will win the race (red, orange, yellow, green, blue, purple)?\n"
    "Enter a color:",
)
all_turtles = []

x_position = -230
y_position = -100
for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=x_position, y=y_position)
    y_position += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win. The {winning_color} turtle is the winner.")
            else:
                print(f"You lose. The {winning_color} won.")
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


screen.exitonclick()
