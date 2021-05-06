import colorgram
import turtle
import random

colors = colorgram.extract('sample.jpeg', 16)
color_list = []


def random_color(colors):
    for c in colors:
        tuple = (c.rgb[0], c.rgb[1], c.rgb[2])
        color_list.append(tuple)
    return color_list


random_color(colors)

timmy = turtle.Turtle()
timmy.hideturtle()
timmy.shape('circle')
timmy.speed('fastest')
turtle.colormode(255)
turtle.bgcolor(254, 253, 253)
timmy.up()
timmy.setheading(225)
timmy.forward(380)


def hirst():
    timmy.setheading(0)
    timmy.dot(40, random.choice(color_list))
    timmy.up()
    timmy.forward(60)


for n in range(10):
    for n in range(10):
        hirst()
    timmy.setheading(90)
    timmy.forward(60)
    timmy.setheading(180)
    timmy.forward(600)

screen = turtle.Screen()
screen.exitonclick()

