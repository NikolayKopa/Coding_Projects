from turtle import *
drawing_area = turtle.Screen()
screenWidth = input("What should the width of the grid be?")
screenLength = input("What should the length of the grid be?")
gridSpacing = input("What should the grid spacing be?")
drawing_area.setup(screenWidth, screenLength)
numberoflineswidth = screenWidth/gridSpacing
numberoflineslength = screenLength/gridSpacing
xposition = screenLength/-2
yposition = screenWidth/2
for i in range(numberoflineswidth):
    turtle.setposition(xposition, yposition)
    turtle.forward(screenLength)
    yposition = yposition - gridSpacing

xposition = screenLength/-2
yposition = screenWidth/-2
turtle.right(90)

for i in range(numberoflineslength):
    turtle.setposition(xposition, yposition)
    turtle.forward(screenWidth)
    xposition = xposition + gridSpacing


petalarcsize = screenLength/5
fillcolor("yellow")
for i in range(13):
    begin_fill()
    turtle.circle(petalarcsize, 70)
    end_fill()
