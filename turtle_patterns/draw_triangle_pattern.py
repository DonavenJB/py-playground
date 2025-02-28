import turtle

wn = turtle.Screen()              # Create a screen
wn.bgcolor("lightgreen")        # Set background color

tess = turtle.Turtle()            # Create a turtle
tess.speed(10)                  # Set turtle speed
tess.pensize(2)                 # Set pen size

# Make a list of colors
colors = ["red", "blue", "purple", "orange", "green", "yellow"]

# This outer loop draws the whole pattern
for i in range(18):
    
    tess.color(colors[i % 6])   # Choose a color from the list
    
    # This inner loop draws one triangle
    for _ in range(3):
        tess.forward(100)
        tess.left(120)
    
    tess.left(20)               # Turn to start the next triangle
    
tess.hideturtle()                 # Hide turtle
wn.exitonclick()                # Wait for a click to close