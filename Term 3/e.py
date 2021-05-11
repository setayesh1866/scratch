from turtle import Pen
from random import randint

laki = Pen()

def square():
    side = 1
    length = randint(20, 100)
    while side <=4:
        laki.forward(length)
        laki.left(90)
        side += 1

while True:
    laki.speed(1000)
    laki.penup()
    laki.goto(randint(-250, 250), randint(-250, 250))
    laki.pendown()
    laki.begin_fill()
    laki.color("#" + str(randint(100000, 999999)))
    square()
    laki.end_fill()
