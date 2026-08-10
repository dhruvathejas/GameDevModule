from turtle import *

sprites = {}

listen()

tracer(False)

speed(0)


def paint(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)


def paint_start():
    pendown()


def paint_stop():
    penup()


def paint_color(color):
    pencolor(color)


def paint_size(size):
    pensize(size)


def paint_rectangle(x, y, width, height):
    penup()
    goto(x, y)
    pendown()

    for i in range(2):
        forward(width)
        right(90)
        forward(height)
        right(90)


def get_x():
    return pos()[0]


def get_y():
    return pos()[1]


def paint_move(x, y):
    goto(x, y)


def key(key_name, command):
    onkey(command, key_name)


def move_by_x(x):
    setx(get_x() + x)


def move_by_y(y):
    sety(get_y() + y)


def paint_circle(x, y, size):
    penup()
    goto(x, y)
    pendown()
    circle(size / 2)
    penup()

def create_sprite(name,x,y,size,colour,draw):
    sprites.append(name)
    name.x,name.y,name.size,name.colour,name.draw = x,y,size,colour,draw
