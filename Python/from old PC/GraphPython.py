import turtle, random
colors = ["red","blue","yellow","green","brown","purple"]
turtle.speed(10)
y = 200
x = -200
turtle.right(90)
for i in range(40):
    turtle.penup()
    turtle.setposition(x,y)
    color = random.choice(colors)
    turtle.color(color)
    turtle.pendown()
    turtle.forward(400)
    x = x + 10
turtle.left(90)
x = -200
y = 190
for i in range(40):
    turtle.penup()
    turtle.setposition(x,y)
    color = random.choice(colors)
    turtle.color(color)
    turtle.pendown()
    turtle.forward(400)
    y = y - 10
