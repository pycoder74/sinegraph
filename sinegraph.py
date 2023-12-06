from turtle import *
from draw_nums import draw_number

t = Turtle()
t.pendown()

def draw_numbers():
    for i in range(1, 4):
        draw_number(i, screen=t.screen, turtle=t)
        if i != 3:
            t.forward(160)
        else:
            t.backward(320)


def draw_xy():
    # draw x axis
    t.forward(400)
    t.backward(800)
    # draw y axis
    t.setheading(90)
    t.forward(400)
    t.backward(800)
    t.forward(400)
    draw_numbers()

def draw_sine():
    for i in range(0, 4):  # Change the range to cover the full 360 degrees
        t.circle(-200, 90)
        t.circle(-200, 90)
        t.circle(200, 90)
        t.circle(200, 90)

draw_xy()
draw_sine()
done()
