import turtle as tr
import random as rnd

shape = input ("Enter witch shape square/traiangle?(s/t)")

if shape == 's':
    tr.speed(10000)
    for j in range(100):
        tr.penup()
        x_position = rnd.randint(-400, 300)
        y_position = rnd.randint(-200, 200)
        tr.goto(x_position, y_position)
        tr.pendown()
        pen_size = rnd.randint(1, 5)
        tr.pensize(pen_size)
        for i in range(3):
            tr.fd(100)
            tr.lt(120) 

if shape == 't':
    tr.speed(10000)
    for j in range(100):
        tr.penup()
        x_position = rnd.randint(-400, 300)
        y_position = rnd.randint(-200, 200)
        tr.goto(x_position, y_position)
        tr.pendown()
        pen_size = rnd.randint(1, 5)
        tr.pensize(pen_size)
        for i in range(4):
            tr.fd(150)
            tr.lt(90) 

    tr.done()
