from turtle import *
screen = Screen()
screen.setup(1000,1000)
speed(0)
block_size = int(input("What should the size of the block be? Range of 5 to 50."))
num_blocks = int(input("How many blocks should be at the bottom row? At most 20."))
row_number = 0
def draw_block_row(num_blocks):
    for i in range(num_blocks):
        for i in range(4):
            forward(block_size)
            left(90)
        forward(block_size)
def move_to_row(num_blocks):
    x_value = -((num_blocks*block_size)/2)
    y_value = -410+(block_size*row_number)
    penup()
    setposition(x_value,y_value)
    pendown()
for i in range(num_blocks):
    if row_number%2 == 0:
        fillcolor("red")
        pencolor("red")
    elif row_number%2 != 0:
        fillcolor("yellow")
        pencolor("yellow")
    move_to_row(num_blocks)
    row_number=row_number+1
    begin_fill()
    draw_block_row(num_blocks)
    end_fill()
    num_blocks=num_blocks-1
