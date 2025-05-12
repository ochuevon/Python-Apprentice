"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""
               
import random
import turtle

def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

colors = ["red", "blue", "green", "yellow", "orange", "black", "pink"]


def getNextColor(i):
    return colors[i % len(colors)]

turtle.setup (width=600, height=600) 
window = turtle.Screen()

def make_a_shape(t):
    t.forward(100)
    t.right(20)

    for i in range(4):
        t.forward(10)
        t.right(20)

t = turtle.Turtle() 

t.shape("turtle") 

t.width(5) 

t.speed(2) 

for i in range(100):
    make_a_shape(t)


turtle.done()

   


    
 


# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 
# for example 100, or it could use islice(), cycle(), or a list of numbers.

