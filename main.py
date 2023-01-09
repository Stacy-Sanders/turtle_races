import turtle
from turtle import Turtle, Screen
from random import choice

screen = Screen()
screen.setup(width=500, height=400)  # height and width text not needed, added for clarity

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

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
y = 150
# for turtle in turtle_racers:
for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-220, y=y)
    y -= 50


screen.exitonclick()


#  for turtle_index in range(0, 6):
#      tim = Turtle(shape="turtle")
#      tim.color[colors[turtle_index]]
#      tim.penup()
#      tim.goto(x=-230, y=-100)
