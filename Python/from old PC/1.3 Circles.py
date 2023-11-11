import turtle, random
colors = ["red", "green","blue","orange","purple","pink","yellow","brown"]
y = -300
r = 300
turtle.speed(10)
for i in range(25):
    turtle.penup()
    turtle.setposition(0,y)
    turtle.pendown()
    color = random.choice(colors)
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    y = y +10
    r = r - 10
    
    
