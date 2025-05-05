"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""

import turtle
turtle.setup(width=600, height=600)

t = turtle.Turtle()

t.shape('turtle')                    


colors = [ 'red', 'blue', 'black', 'orange']    

for color in colors:                           
    
                              
    t.pencolor(color)                     
    t.forward(100)                           
    t.right(90)

def make_a_shape(t):
    t.forward(10)
    t.right(20)
screen = turtle.Screen()
t = turtle.Turtle()

for _ in range(100): 
 make_a_shape(t)

 
# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 
# for example 100, or it could use islice(), cycle(), or a list of numbers.

num_shapes = ...

for i in range(...):
    make_a_shape(t)
    t.right(360/num_shapes)
