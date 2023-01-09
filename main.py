import turtle
from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)  # height and width text not needed, added for clarity

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt=f"{colors}\nWhich turtle will win the race?\nChoose a color:")

# tim = Turtle(shape="turtle")
# tim.color("green")
#
# purple = Turtle(shape="turtle")
# purple.color("purple")
# blue = Turtle(shape="turtle")
# blue.color("blue")
# orange = Turtle(shape="turtle")
# orange.color("orange")
# red = Turtle(shape="turtle")
# red.color("red")
# yellow = Turtle(shape="turtle")
# yellow.color("yellow")
#
# turtle_racers = [tim, purple, blue, orange, red, yellow]
turtle_racers = []
y = 150
# for turtle in turtle_racers:
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-220, y)
    y -= 50
    turtle_racers.append(new_turtle)

if user_bet:
    is_race_on = True
winners = []
while is_race_on:
    for turtle in turtle_racers:
        turtle.forward(randint(0, 10))
        if turtle.xcor() > 225:
            winners.append(turtle)
            winning_turtle = winners[0]
            is_race_on = False
            winning_color = winning_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost. The {winning_color} turtle is the winner.")
            # print(list(winners))


screen.exitonclick()


#  for turtle_index in range(0, 6):
#      tim = Turtle(shape="turtle")
#      tim.color[colors[turtle_index]]
#      tim.penup()
#      tim.goto(x=-230, y=-100)
