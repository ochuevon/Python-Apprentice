"""
For this program, you will tell Tina the Turtle to draw a triangle.

You should look at the previous programs to see how to use the turtle commands.
Copy lines of code from those programs to this one to draw a triangle.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()
tina.penup()
tina.begin_fill()


tina.pencolor('blue')
tina.forward(160)
tina.left(130)

tina.pencolor('red')
tina.forward(150)

tina.pencolor('green')
tina.right(250)
tina.forward(140)

tina.end_fill()

turtle.exitonclick()                    # Close the window when we click on it
