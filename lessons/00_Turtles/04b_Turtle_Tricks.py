"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

tina.penup()
tina.color('red')
tina.begin_fill()

tina.pencolor('blue')
tina.forward(100)
tina.left(45)

tina.pencolor('red')
tina.forward(100)
tina.left(90)

tina.pencolor('black')
tina.forward(100)
tina.left(45)

tina.pencolor('purple')
tina.forward(100)
tina.left(45)

tina.pencolor('yellow')
tina.forward(100)
tina.left(90)

tina.pencolor('orange')
tina.forward(100)

tina.end_fill()

turtle.exitonclick()                    # Close the window when we click on it
