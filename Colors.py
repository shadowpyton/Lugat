import  turtle
t=turtle.Turtle()
t.speed(0)
turtle.bgcolor('black')
for i in range(500):
    t.color('cyan')
    t.circle(i)
    t.left(10)
turtle.done()