# from turtle import Turtle, Screen


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
# arr = ["orange", "red", "blue", "green", "purple",
#        "pink", "yellow", "#ADFF2F", "#8A2BE2", "#FF7F50"]

# for i in range(3, 11):
#     ran_num = random.randint(0, 9)
#     turtle.color(arr[ran_num])
#     tilt_ang = (360/i)
#     for _ in range(i):
#         turtle.forward(100)
#         turtle.right(tilt_ang)


# Draw random walk:
# colors = ["#556B2F", "#D2691E", "#800000", "#800080", "#8A2BE2	",
#           "#4B0082", "#483D8B", "##006400", "##000080", "##2F4F4F"]
# directions = [0, 90, 180, 270]

# turtle.pensize(10)
# turtle.speed(2)

# for _ in range(200):
#     ran_num = random.randint(0, 2)
#     ran_color = random.randint(0, 9)
#     turtle.color(random.choice(colors))
#     turtle.forward(30)
#     turtle.setheading(random.choice(directions))


# Create a random color function that returns a tuple of (R, G, B):
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

# print(random_color())


# Create a spirograph:
# import turtle as t
# import random

# t.colormode(255)
# turtle = t.Turtle()
# turtle.speed(10)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)


# def spirograph(gap_size):
#     for _ in range(360 // gap_size):
#         turtle.color(random_color())
#         turtle.circle(100)
#         turtle.setheading(turtle.heading() + 10)


# spirograph(5)


screen = t.Screen()
screen.exitonclick()
