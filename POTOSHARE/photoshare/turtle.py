import turtle
t = turtle.Turtle()
s = turtle.Screen()
colors = ['red', 'blue', 'white', 'yellow', 'purple', 'blue']
s.bgcolor('black')
t.pensize('2')
t.speed(0)
for x in range (360):
    t.pencolor(colors[x%6])
    t.width(x//100+1)
    t.forward(x)
    t.left(59)
    turtle.hideturtle()