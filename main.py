from turtle import Turtle, Screen
import random

turtle = Turtle()

turtle.shape("turtle")


# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)

# Easier way to move the turtle in a square:
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)


# Draw a horzional dashed line:
# for i in range(15):
#     turtle.forward(10)
#     if i % 2 == 0:
#         turtle.penup()
#     else:
#         turtle.pendown()


# Increase the side of the shape by 1 and change the lines to a random color each iteration:
arr = ["orange", "red", "blue", "green", "purple",
       "pink", "yellow", "#ADFF2F", "#8A2BE2", "#FF7F50"]

for i in range(3, 11):
    ran_num = random.randint(0, 9)
    turtle.color(arr[ran_num])
    int_ang = (180 * i - 360)/i
    tilt_ang = 180 - int_ang
    for _ in range(i):
        turtle.forward(100)
        turtle.right(tilt_ang)


screen = Screen()
screen.exitonclick()
