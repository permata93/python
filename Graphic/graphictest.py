from graphics import *
import random, time

# Do some simple drawing
window = GraphWin("Visualisation", 300, 300)

# Read in and print out the data in the data file
datafile = open("data.txt",'r')
data = datafile.readlines()

for line in data:
    nextnumber = float(line.strip())
    box = Rectangle(Point(200,50),Point(nextnumber,nextnumber))
    box.setFill(color_rgb(0,0,0))
    box.draw(window)
    time.sleep(0.2)



