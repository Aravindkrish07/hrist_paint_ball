# import colorgram
#
# colors = colorgram.extract('image.jpeg', 30)
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
# print(rgb_color)
import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
color_image = [(205, 158, 99), (207, 166, 21), (224, 238, 232), (118, 183, 205), (157, 56, 93), (224, 205, 107), (10, 20, 48), (145, 27, 54), (15, 106, 160), (47, 13, 25), (185, 155, 171), (168, 65, 44), (56, 19, 15), (44, 123, 67), (10, 29, 22), (65, 165, 96), (146, 28, 22), (109, 180, 160), (159, 206, 212), (209, 178, 200), (190, 100, 94), (185, 96, 116), (34, 46, 106), (236, 201, 9), (11, 104, 49), (163, 209, 200), (5, 89, 112)]
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
numbers_dots= 100
for i in range(1, numbers_dots+1):
    tim.pendown()
    tim.dot(20, random.choice(color_image))
    tim.penup()
    tim.forward(50)
    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()