import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)  # Enable RGB color mode

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def draw_shape(sides, length):
    angle = 360 / sides
    tim.color(random_color())  # Set random color for each shape
    for _ in range(sides):
        tim.forward(length)
        tim.right(angle)

# Draw shapes from triangle (3) to decagon (10)
for shape_side in range(3, 11):
    draw_shape(shape_side, 100)

screen = Screen()
screen.exitonclick()
