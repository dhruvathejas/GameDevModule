import turtle as t

version = 1.00

sprites = []

t.listen()
t.tracer(False)
t.speed(0)


def paint(x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.update()


def paint_start():
    t.pendown()
    t.update()


def paint_stop():
    t.penup()
    t.update()


def paint_color(color):
    t.pencolor(color)
    t.update()


def paint_size(size):
    t.pensize(size)
    t.update()


def paint_rectangle(x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.pendown()

    for i in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

    t.penup()
    t.update()

def paint_move(x, y):
    t.goto(x, y)
    t.update()


def key(key_name, command):
    t.onkey(command, key_name)
    t.update()


def move_by_x(x):
    t.setx(t.getx() + x)
    t.update()


def move_by_y(y):
    t.sety(t.gety() + y)
    t.update()


def paint_circle(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(size / 2)
    t.penup()
    t.update()

def clear():
    t.clear()
    t.update()

names = []
attributes = []


class Sprite:
    def create_sprite(name, x, y, size, colour, draw, dot):
        names.append(name)
        attributes.append([x, y, size, colour, draw, dot])


class GameLoop:
    def game_loop():
        for i in range(len(names)):
            a = attributes[i]

            t.penup()
            t.color(a[3])
            t.goto(a[0], a[1])
            if a[4] == 1:
                t.pendown
            if a[5] and a[4] == 1:
                t.dot(a[2], a[3])
        t.done()