# Self generated code for generating dot painting image
# import turtle
# import random
# from turtle import Screen
#
# # Setup
# pen = turtle.Turtle()
# pen.hideturtle()
# pen.penup()
# pen.speed("fastest")
#
# turtle.colormode(255)
# screen = Screen()
#
# # Predefined color list
# color_list = [(208, 81, 160), (54, 131, 89), (144, 40, 91), (140, 48, 26),
#               (222, 108, 206), (133, 203, 177), (46, 103, 56), (158, 84, 45),
#               (167, 38, 160), (128, 143, 189), (83, 44, 20), (36, 69, 42),
#               (187, 106, 93), (186, 171, 140), (84, 181, 125), (88, 91, 157),
#               (60, 32, 39), (78, 165, 153), (195, 71, 79), (161, 220, 201),
#               (45, 77, 74), (80, 44, 74), (59, 122, 129), (218, 187, 176),
#               (220, 167, 182), (167, 167, 207)]
#
# # Function to draw dot grid
# def draw(space, count):
#     start_x = -space * count / 2
#     start_y = -space * count / 2
#     pen.goto(start_x, start_y)
#
#     for i in range(count):
#         for j in range(count):
#             pen.dot(20, random.choice(color_list))
#             pen.forward(space)
#         pen.backward(space * count)
#         pen.right(90)
#         pen.forward(space)
#         pen.left(90)
#
# # Draw the grid
# draw(30, 10)
#
# # Exit on click
# screen.exitonclick()
import turtle
# Copied code for generating dot painting
import turtle as turtle_module
import random

turtle.colormode(255)
tim = turtle_module.Turtle()
color_list = [(208, 81, 160), (54, 131, 89), (144, 40, 91), (140, 48, 26),
              (222, 108, 206), (133, 203, 177), (46, 103, 56), (158, 84, 45),
              (167, 38, 160), (128, 143, 189), (83, 44, 20), (36, 69, 42),
              (187, 106, 93), (186, 171, 140), (84, 181, 125), (88, 91, 157),
              (60, 32, 39), (78, 165, 153), (195, 71, 79), (161, 220, 201),
              (45, 77, 74), (80, 44, 74), (59, 122, 129), (218, 187, 176),
              (220, 167, 182), (167, 167, 207)]
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.speed("fastest")

for dot_counts in range(1, number_of_dots + 1):
    tim.dot(20,random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if dot_counts % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

# For extracting color from images
# import colorgram
#
# rgb_colors = []
#
# # Extract 30 colors from the image
# colors = colorgram.extract('img.jpg', 30)
#
# # Print RGB values
# # for i, color in enumerate(colors, 1):
# #     rgb = color.rgb
# #     print(f"{i}. RGB: ({rgb.r}, {rgb.g}, {rgb.b})")
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, b, g)
#     rgb_colors.append(new_color)
# print(rgb_colors)