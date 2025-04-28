""" Tash Me

Write a program that:
1) Loads an emoji image as the background
2) Make the turtle shape a moustach
3) Move the moustache to the right spont on the emoji

Hint: See 08a_More Turtle Programs, section 'Change the Background Image' and
'Change the Turtle Shape'
"""

import turtle as turtle 

def set_turtleimage(turtle, sanic_64):
    """Set the turtles shape into a custom image."""
    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / sanic_64)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
t = turtle.Turtle()
set_turtleimage(t, "pikachu.gif")

mustache=turtle.Turtle()
set_turtleimage(mustache, "moustache1.gif")
"Set the turtles shape into a custom image"

from pathlib import Path
image_dir = Path(__file__).parent / "images"
image_path = str(image_dir / "moustache1.gif")
screen = turtle.getscreen()
screen.addshape(image_path)


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
t = turtle.Turtle()


mustache.goto(0,-50)

turtle.exitonclick()