import turtle
from random import randint

def draw_track(t):
    for i in range(22):
        t.pd()
        t.forward(10)
        t.pu()
        t.forward(10)
        t.up()

def set_race(t):
    t.penup()
    t.setpos(-200,100)
    t.right(90)
    t.pd()
    t.forward(200)
    t.pu()
    t.setpos(200,100)
    t.pd()
    t.forward(200)
    t.up()
    t.setpos(-210,50)
    t.left(90)
    draw_track(t)
    t.setpos(-210,0)
    draw_track(t)
    t.setpos(-210,-50)
    draw_track(t)
    t.ht()

def set_players():
    p1 = turtle.Turtle()
    p1.shape('turtle')
    p1.color('red')
    p1.up()
    p1.setpos(-220,75)
    p1.pd()

    p2 = turtle.Turtle()
    p2.shape('turtle')
    p2.color('green')
    p2.up()
    p2.setpos(-220,25)
    p2.pd()

    p3 = turtle.Turtle()
    p3.shape('turtle')
    p3.color('yellow')
    p3.up()
    p3.setpos(-220,-25)
    p3.pd()

    p4 = turtle.Turtle()
    p4.shape('turtle')
    p4.color('blue')
    p4.up()
    p4.setpos(-220,-75)
    p4.pd()

    return (p1,p2,p3,p4)

def start_race(t):
    p1,p2,p3,p4 = set_players()
    flag = 1
    while(p1.xcor()<200 or p2.xcor()<200 or p3.xcor()<200 or p4.xcor()<200):
        if(p1.xcor()<200):
            p1.forward(randint(1,10))
        if(p2.xcor()<200):
            p2.forward(randint(1,10))
        if(p3.xcor()<200):
            p3.forward(randint(1,10))
        if(p4.xcor()<200):
            p4.forward(randint(1,10))
        if(flag):
            if(p1.xcor()>=200):
                t.write('Player 1 wins',align='center',font=("Arial", 20, "normal"))
                flag = 0
            elif(p2.xcor()>=200):
                t.write('Player 2 wins',align='center',font=("Arial", 20, "normal"))
                flag = 0
            elif(p3.xcor()>=200):
                t.write('Player 3 wins',align='center',font=("Arial", 20, "normal"))
                flag = 0
            elif(p4.xcor()>=200):
                t.write('Player 4 wins',align='center',font=("Arial", 20, "normal"))
                flag = 0

t = turtle.Turtle()
scr = turtle.Screen()
scr.title('Turtle Race')
t.pu()
t.setpos(0,150)
t.write('Turtle Race',align='center',font=("Arial", 20, "bold"))
set_race(t)
t.setpos(0,-250)
start_race(t)
turtle.exitonclick()
