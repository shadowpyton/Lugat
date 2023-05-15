import turtle, random
border = turtle.Turtle()
border.speed(0)
border.hideturtle()
border.pensize(10)
border.color("red")
border.up()
border.goto(300, 300)
border.down()
border.goto(300, -300)
border.goto(-300, -300)
border.goto(-300, 300)
border.goto(300, 300)

ball = turtle.Turtle()
ball.shape("triangle")
randx = random.randint (-290, 290)
randy = random.randint (-290, 290)
ball.goto(randx, randy)
dx = 6
dy = 4
while True:
    x, y = ball.position()
    if x >= 300 or x <= -300:
        dx = -dx
    if y >= 300 or y <= -300:
        dy = -dy
    ball.goto(x + dx, y + dy)
