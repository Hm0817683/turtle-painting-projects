import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
screen = Screen()
tim = Turtle()
tim.speed("fastest")  # Draw quickly

def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def circle_maker(size_of_gap):
    for _ in range(int(360 / size_of_gap)):  # 360/5 = 72 (for 5° steps)
        tim.color(random_colors())
        tim.circle(100)
        tim.left(size_of_gap)  # Rotate left to change orientation

circle_maker(int(input("Please enter size of gap between circle: ")))

screen.exitonclick()
