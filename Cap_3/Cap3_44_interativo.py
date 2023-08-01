import turtle
def poli(lados, comp):
    angulo = 360 / lados
    for _ in range(lados):
        turtle.forward(comp)
        turtle.right(angulo)

    turtle.done()