import turtle
import random
from turtle import Screen

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.pensize(10)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

directions = [0, 90, 180, 270]

for _ in range(1000):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))













screen = turtle.Screen()
screen.exitonclick()
