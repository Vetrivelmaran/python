# import turtle

# window = turtle.Screen()
# my_turtle = turtle.Turtle()
# my_turtle.speed(1)
# my_turtle.color("black")
# my_turtle.penup()
# my_turtle.goto(-100, 0)
# my_turtle.pendown()
# my_turtle.left(90)
# my_turtle.forward(200)
# my_turtle.right(90)
# my_turtle.forward(130)
# my_turtle.right(90)
# my_turtle.forward(30)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(30)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(30)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(110)
# my_turtle.right(90)
# my_turtle.forward(30)
# window.exitonclick()

import turtle

window = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.speed(1)

# Set the fill color to blue
my_turtle.fillcolor("blue")

# Move the turtle to the starting position
my_turtle.penup()
my_turtle.goto(-100, 0)
my_turtle.pendown()

# Start filling the shape
my_turtle.begin_fill()

# Draw the vertical line
my_turtle.left(90)
my_turtle.forward(200)

# Draw the horizontal line
my_turtle.right(90)
my_turtle.forward(130)

# Draw the first diagonal line
my_turtle.right(90)
my_turtle.forward(30)

# Draw the second diagonal line
my_turtle.right(90)
my_turtle.forward(100)

# Draw the third diagonal line
my_turtle.left(90)
my_turtle.forward(30)

# Draw the fourth diagonal line
my_turtle.left(90)
my_turtle.forward(100)

# Draw the fifth diagonal line
my_turtle.right(90)
my_turtle.forward(30)

# Draw the sixth diagonal line
my_turtle.right(90)
my_turtle.forward(100)

# Draw the seventh diagonal line
my_turtle.left(90)
my_turtle.forward(110)

# Draw the eighth diagonal line
my_turtle.right(90)
my_turtle.forward(30)

# Stop filling the shape
my_turtle.end_fill()

# Lift the pen
my_turtle.penup()

# Exit the screen when the user clicks on it
window.exitonclick()
