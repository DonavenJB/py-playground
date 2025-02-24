import turtle

wn = turtle.Screen()              # Create a screen
wn.bgcolor("lightgreen")        # Set background color

alex = turtle.Turtle()            # Create a turtle
alex.speed(10)                  # Set turtle speed
alex.pensize(2)                 # Set pen size

# Make a list of colors
colors = ["red", "blue", "purple", "orange", "green", "yellow"]

# This outer loop draws the whole pattern
for i in range(18):
    
    alex.color(colors[i % 6])   # Choose a color from the list
    
    # This inner loop draws one square
    for side in range(4):
        alex.forward(100)
        alex.left(90)
    
    alex.left(20)               # Turn to start the next square
    
wn.exitonclick()                # Wait for a click to close