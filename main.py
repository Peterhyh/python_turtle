from turtle import Turtle, Screen


turtle = Turtle()

turtle.shape("turtle")
turtle.color("#DAA520")


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


screen = Screen()
screen.exitonclick()
