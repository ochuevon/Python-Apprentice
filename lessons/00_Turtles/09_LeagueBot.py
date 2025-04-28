""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle


def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)
set_turtle_image(turtle, "leaguebot_bolt.gif" )

turtle.shapesize

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

tina = turtle.Turtle() 
tina.shapesize(10,10)
tina.pencolor('blue')

tina.speed(3)
for i in range(8): 
    tina.forward(120)
    tina.left(45)

turtle.exitonclick()