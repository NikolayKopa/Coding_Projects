import turtle as t
t.pencolor("blue")
t.fillcolor("blue")
x = 0
while True:
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    x = x + 60
    t.penup()
    t.setposition(x,0)
    t.pendown()
    t.clear()

