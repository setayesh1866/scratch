import turtle as tr
import random as rnd

tr.speed(100000)
for j in range(10000):
    tr.penup()
    x_position = rnd.randint(-400, 300)
    y_position = rnd.randint(-200, 200)
    tr.goto(x_position, y_position)
    tr.pendown()
    pen_size = rnd.randint(1, 5)
    tr.pensize(pen_size)
    for i in range(6):
        tr.fd(100)
        tr.lt(60) 

tr.done()