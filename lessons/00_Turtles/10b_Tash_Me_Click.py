# Tash Me with a Click
# 
# Update your Tash Me program ( copy your old program here )to put 
# the moustache where you click on the screen.
#
# Hint: See 08a_More Turtle Programs, section 'Click on the Screen'
 


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


t.shape("turtle")
t.turtlesize(stretch_wid=10, stretch_len=10, outline=4) # Make the turtle really big

def turtle_clicked(t, x, y):
    print('turtle clicked!')
    t.goto(x,y)
screen.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))



turtle.done()