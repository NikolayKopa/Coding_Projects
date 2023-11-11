from turtle import *
bgcolor("black")
tracer(10)
pensize(2)
def myShape():
    s = Shape("compound")

    figure1 = ((0,0),(50,0),(50,50),(0,50))
    figure2 = ((0,0),(50,0),(25,50))
    rt(90)
    figure3 = ((-50,-50),(0,-50),(0,0),(-50,0))
    figure4 = ((-50,0),(0,0),(-25,-50))

    s.addcomponent(figure1, "white", "blue")
    s.addcomponent(figure2, "red")
    s.addcomponent(figure3, "white", "red")
    s.addcomponent(figure4, "green")

    register_shape("newshape", s)
    shape("newshape")

    for i in range(8):
        for i in range(36):
            pendown()
            pencolor("black")
            fd(10)
            tilt(10)
            forward(20)
            rt(10)
            clone()
        penup()
        left(90)
        forward(100)
        right(90)
        penup()
        exitonclick()


myShape()
