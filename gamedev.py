from turtle import *

sprites = []

listen()
tracer(False)
speed(0)


def paint(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)
    update()


def paint_start():
    pendown()
    update()


def paint_stop():
    penup()
    update()


def paint_color(color):
    pencolor(color)
    update()


def paint_size(size):
    pensize(size)
    update()


def paint_rectangle(x, y, width, height):
    penup()
    goto(x, y)
    pendown()

    for i in range(2):
        forward(width)
        right(90)
        forward(height)
        right(90)

    penup()
    update()


def get_x():
    return pos()[0]


def get_y():
    return pos()[1]


def paint_move(x, y):
    goto(x, y)
    update()


def key(key_name, command):
    onkey(command, key_name)
    update()


def move_by_x(x):
    setx(get_x() + x)
    update()


def move_by_y(y):
    sety(get_y() + y)
    update()


def paint_circle(x, y, size):
    penup()
    goto(x, y)
    pendown()
    circle(size / 2)
    penup()
    update()


class Sprite:
    def create_sprite(name, x, y, size, colour, draw, dot):
        sprites.append(name)
        name.x, name.y, name.size, name.colour, name.draw, name.dot = x, y, size, colour, draw, dot

def game_frame():
    for i in range(len(sprites)):
        goto(sprites[i].x, sprites[i].y)

        if sprites[i].draw == 1:
            pendown()
        else:
            penup()

        pencolor(sprites[i].colour)

        if sprites[i].dot == 1 and sprites[i].draw == 1:
            dot(sprites[i].size, sprites[i].colour)

    update()
