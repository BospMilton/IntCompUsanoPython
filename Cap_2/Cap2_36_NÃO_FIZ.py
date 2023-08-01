import turtle

s = turtle.Screen()
t = turtle.Turtle()

while True:
    # lua cheia
    t.penup()
    t.goto(-500,0)
    t.pendown()
    t.circle(25)

    #lua nova
    t.penup()
    t.goto(-400,0)
    t.pendown()
    t.circle(25,180)