import turtle
while True:
    s = turtle.Screen()
    sol  = turtle.Turtle("circle")
    sol.shapesize(2.5,2.5)  
    Merc = turtle.Turtle("circle")
    Venu = turtle.Turtle("circle")
    Terr = turtle.Turtle("circle")
    Mart = turtle.Turtle("circle")
    #declaração das funções:
    def salt(t,x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()
    def mov(t,rai,ang,vel):
        t.circle(rai,ang)
        t.speed(vel)
    #posicionamento dos planetas:
    salt(Merc, 0, -58)
    salt(Venu, 0, -108)
    salt(Terr, 0, -150)
    salt(Mart, 0, -228)
    #movimento dos planetas:
    mov(Merc,58,300,9)
    mov(Venu,108,160,3)
    mov(Terr, 150, 120, 5)
    mov(Mart, 228, 45, 7)






