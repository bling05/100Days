import turtle
import random

# import colorgram
# colors = colorgram.extract('image.jpg', 21)
# rgb_colors = []
# color_list = []
# for i in range(1,len(colors)):
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#     rgb = (r,g,b)
#     color_list.append(rgb)

color_list = [(208, 165, 125), (250, 235, 237), (140, 49, 106), 
            (164, 169, 38), (244, 80, 57), (230, 114, 163), 
            (3, 143, 55), (215, 234, 232), (241, 65, 140), 
            (1, 143, 184), (162, 55, 52), (50, 203, 226), 
            (254, 230, 0), (21, 166, 126), (245, 224, 47), 
            (212, 235, 238), (28, 196, 219), (119, 184, 146), 
            (231, 167, 191), (140, 213, 225)]
turtle.colormode(255)



myturt = turtle.Turtle()
myturt.up()
myturt.hideturtle()
myturt.speed("fastest")

myturt.goto(-300,-300)
for x in range(-250, 250, 50):
    for y in range(-250, 250, 50):
        myturt.goto(x,y)
        myturt.dot(20, random.choice(color_list))
    y = -250

turtle.exitonclick()