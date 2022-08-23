import colorgram

# my solution:

# colors_from_image = colorgram.extract('image.jpg', 30)
#
# color_list = []
#
#
# def separate_each_color(empty_colors_list, new_list):
#     x = 0
#     for _ in range(len(empty_colors_list)):
#         color = empty_colors_list[x]
#         r = color.rgb[0]
#         g = color.rgb[1]
#         b = color.rgb[2]
#         color = (r, g, b)
#         x += 1
#         new_list.append(color)
#
#
# separate_each_color(colors_from_image, color_list)
#
# print(color_list)
#

# teacher's solution:

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# create a painting with 10x10 rows of colored dots.
# dots should be 20 in size and spaced apart by 50 spaces.


# my solution 10 x 10 dot grid
#
# import turtle as t
# from turtle import Screen
# import random
#
# t.colormode(255)
#
# color_list = [
#     (232, 233, 236), (236, 230, 233), (225, 234, 229), (175, 48, 79), (43, 97, 146), (204, 162, 94), (223, 210, 103),
#     (137, 90, 65), (110, 176, 206), (176, 164, 39), (211, 132, 173), (225, 74, 51), (199, 76, 119), (90, 105, 190),
#     (27, 145, 91), (124, 218, 208), (95, 157, 64), (119, 43, 71), (227, 170, 187), (131, 187, 161), (49, 186, 201),
#     (172, 186, 220), (233, 173, 164), (153, 208, 217), (98, 52, 44), (35, 64, 111), (43, 77, 80), (51, 59, 66),
#     (73, 51, 44)
# ]
#
#
# tim = t.Turtle()
# tim.pensize(10)
#
# tim.penup()
# tim.setheading(225)
# tim.forward(250)
# tim.setheading(0)
#
#
# def draw_dots():
#     if tim.xcor() == 500.00:
#         y = tim.ycor()
#         tim.goto(0.00, y + 50.00)
#     else:
#         tim.color(random.choice(color_list))
#         tim.pendown()
#         tim.dot(20)
#         tim.penup()
#         tim.forward(50)
#
#
# for _ in range(110):
#     draw_dots()



# teacher's solution 10 x 10 dot grid

import turtle as turtle_module
import random

tim = turtle_module.Turtle()
color_list = [
    (232, 233, 236), (236, 230, 233), (225, 234, 229), (175, 48, 79), (43, 97, 146), (204, 162, 94), (223, 210, 103),
    (137, 90, 65), (110, 176, 206), (176, 164, 39), (211, 132, 173), (225, 74, 51), (199, 76, 119), (90, 105, 190),
    (27, 145, 91), (124, 218, 208), (95, 157, 64), (119, 43, 71), (227, 170, 187), (131, 187, 161), (49, 186, 201),
    (172, 186, 220), (233, 173, 164), (153, 208, 217), (98, 52, 44), (35, 64, 111), (43, 77, 80), (51, 59, 66),
    (73, 51, 44)
    ]
turtle_module.colormode(255)
tim.speed('fastest')
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 101
tim.shape('turtle')



for dot_count in range(1, number_of_dots):
    tim.pendown()
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
