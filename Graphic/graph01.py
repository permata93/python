from graphics import *
import random

# Read in and print out the data in the data file
datafile = open("data.txt",'r')
data = datafile.readlines()

# Do some simple drawing
window = GraphWin("Visualisation", 600,600)

listOfBoxes = []

# Processing version looks like this...
# for(int i=0; i<datafile.length; i-i+2) {

for i in range(0,len(data),2):
    firstnumber = int(float(data[i].strip())) 
    secondnumber = int(float(data[i+1].strip()))
    print(str(firstnumber) + " and " + str(secondnumber))
    box = Oval(Point(50,50),Point(firstnumber,secondnumber))
    box.setFill(color_rgb(120,120,120))
    box.draw(window)
    listOfBoxes.append(box)
    time.sleep(0.2)

for i in range(0,len(data),2):
    firstnumber = int(float(data[i].strip()))
    secondnumber = int(float(data[i+1].strip()))
    print(str(firstnumber) + " and " + str(secondnumber))
    text = Text(Point(350,500),Point(firstnumber,firstnumber))
    text.setFill(color_rgb(120,120,120))
    text.draw(window)
    listOfBoxes.append(box)
    time.sleep(0.2)

for i in range(0,len(data),2):
    firstnumber = int(float(data[i].strip()))
    secondnumber = int(float(data[i+1].strip()))
    print(str(firstnumber) + " and " + str(secondnumber))
    box = Rectangle(Point(600,50),Point(firstnumber,firstnumber))
    box.setFill(color_rgb(120,120,120))
    box.draw(window)
    listOfBoxes.append(box)
    time.sleep(0.2)



while True:
    for box in listOfBoxes:
        box.setFill(color_rgb(random.randint(0,),random.randint(0,255),random.randint(0,255)))

window.getMouse()

#box = Rectangle(Point(200,50),Point(nextnumber,nextnumber))


    
