from graphics import *
import random

# Read in and print out the data in the data file
datafile = open("data.txt",'r')
for line in datafile: print(line)

# Do some simple drawing
window = GraphWin("Visualisation", 300, 300)

ball = Circle(Point(100,100), 30)
ball.setFill(color_rgb(255,255,0))
ball.draw(window)

box = Rectangle(Point(200,50),Point(250,150))
box.setOutline(color_rgb(255,0,0))
box.draw(window)

line = Line(Point(200,200),Point(250,280))
line.setWidth(4)
line.draw(window)

text = Text(Point(50,200),"Hello")
text.draw(window)

# Waits until the mouse is clicked before closing the window
window.getMouse()
