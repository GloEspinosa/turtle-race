from turtle import Turtle, Screen
import random

# INSTANCES:
# Both turtle Objects are Instances of Turtle Class

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? "
                                               "Enter a color: (Yellow / Green / Blue / Red / Black) ")
y_positions = [-140, -70, 0, 70, 140]
colors = ["yellow", "green", "blue", "red", "black"]
all_turtles = []

for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        random_distance = (random.randint(0, 10))
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()
            if winner == bet.lower():
                print("You've won! ")
            else:
                print("You've lost! ")
            print(f"The {winner} turtle is the winner!")


screen.exitonclick()

