from turtle import *

speed(1000)
penup()
goto(-200, -150)
pendown()
pensize(10)
color('black', 'sky blue')
begin_fill()
for i in range(2):
    fd(400)
    lt(90)
    fd(300)
    lt(90)
end_fill()

penup()
goto(-196, -150)
pendown()
pensize(0)
color('black', 'green')
begin_fill()
for i in range(2):
    fd(391)
    lt(90)
    fd(30)
    lt(90)
end_fill()



done() 