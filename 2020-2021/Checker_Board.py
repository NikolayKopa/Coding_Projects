#There are 30 lines of code in my program.
from turtle import *
speed(0)
color_value = 1
square_length = int(input("What should the length of the square be?"))
#This function draws a row and also draws each square in the row. This function also determines what color each square should be.
def draw_row(color_value,square_length):
   for i in range(8):
       pendown()
       if color_value % 2 != 0:
           color('red')
       else:
           color('black')
       begin_fill()
       for i in range(4):
           forward(square_length)
           left(90)
       end_fill()
       penup()
       forward(square_length)
       color_value += 1
#This function gets the turtle to a position where it can draw the next row.
def move_up_a_row(square_length):
   left(90)
   forward(square_length)
   right(90)
   backward(square_length*8)
#This part of the program sets the turtle to its starting position.
penup()
setposition(-square_length*8/2,-square_length*8/2)
#This part of the program draws the actual checkerboard.
for i in range(8):
   draw_row(color_value,square_length)
   color_value -= 1
   move_up_a_row(square_length)

