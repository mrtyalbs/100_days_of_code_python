import turtle
from random import choice
import colorgram
from turtle import Turtle, Screen

colors_palette = []


def create_colors_palette(image_name, piece_of_color):
    colors = colorgram.extract(image_name, piece_of_color)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        colors_palette.append((r, g, b))

    for _ in range(3):
        del colors_palette[0]

    return colors_palette


def paint_dot(distance, dot_size):
    for _ in range(10):
        painter.dot(dot_size, choice(colors_palette))
        painter.penup()
        painter.forward(distance)
        painter.pendown()

    painter.penup()
    painter.setheading(90)
    painter.forward(50)
    painter.setheading(180)
    painter.forward(500)
    painter.setheading(0)


colors = create_colors_palette("image.jpg", 30)

painter = Turtle()

screen = Screen()

screen.colormode(255)
screen.window_width()

painter.penup()
painter.goto(-335, -195)
painter.pendown()

for _ in range(10):
    paint_dot(50, 20)

screen.exitonclick()
