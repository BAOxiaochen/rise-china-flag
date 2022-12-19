import turtle
import time
t=turtle.Pen()
t_pole=turtle.Pen()
t.speed(10)
t_pole.speed(10)
t_pole.pensize(2)
def pole(x,y):#---定义旗杆（坐标）---
    t_pole.penup()
    t_pole.goto(x,y)
    t_pole.pendown()
    t_pole.left(90)
    t_pole.begin_fill()
    t_pole.color('black','black')
    for i in range(2):
        t_pole.forward(600)
        t_pole.right(90)
        t_pole.forward(10)
        t_pole.right(90)
    t_pole.end_fill()
    t_pole.hideturtle()
def flag(L,x,y):#----定义旗面(宽，坐标)-----
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.setheading(0)
    t.color('red','red')
    for i in range(2):
        t.forward(1.5*L)
        t.right(90)
        t.forward(L)
        t.right(90)
    t.end_fill()
def star(an,L,x,y):#-----定义星星(角度，边长，坐标)-----
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(an)
    t.begin_fill()
    t.color('yellow','yellow')
    for i in range(5):
        t.forward(L)
        t.right(144)
    t.end_fill()
def China_flag(x,y):#------定义中国国旗（坐标）-----
    turtle.tracer(0)
    flag(200,x,y)
    star(0,60,x+35,y-60)    #---大星星---
    star(-10,15,x+85,y-20)    #---01小星星---
    star(-52,15,x+110,y-50)    #---02小星星---
    star(-75,15,x+115,y-85)    #---03小星星---
    star(-35,15,x+85,y-112)    #---04小星星---
    turtle.tracer(10)
    t.hideturtle()
pole(-100,-300)
for w in range(170):
    China_flag(-90,-100+w*3)
    time.sleep(0.03)
    t.clear()
