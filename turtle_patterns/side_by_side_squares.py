import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

# Draw the first square
for _ in range(4):
    tess.forward(50)
    tess.left(90)

# Move to a new spot
tess.penup()        # Lift the pen up
tess.forward(100)   # Move without drawing
tess.pendown()      # Put the pen down

# Draw the second square
tess.color("red")
for _ in range(4):
    tess.forward(50)
    tess.left(90)

wn.exitonclick()