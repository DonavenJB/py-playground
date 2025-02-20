import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")            # Set first color
tess.pensize(3)

# Draw the bottom-right square
for _ in range(4):
    tess.forward(50)
    tess.left(90)

# Move to the touching corner
tess.penup()
tess.goto(0, 50)          # Go to (0, 50)
tess.setheading(90)       # Face up
tess.pendown()

# Draw the top-left square
tess.color("red")             # Set second color
for _ in range(4):
    tess.forward(50)
    tess.left(90)

tess.hideturtle()             # Hide turtle
wn.exitonclick()