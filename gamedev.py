import turtle as t

t.hideturtle()

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

class Sprite:
    def create_sprite(name, x, y, size, colour, draw, dot):
        sprites.append(name)
        name.x, name.y, name.size, name.colour, name.draw, name.dot = x, y, size, colour, draw, dot

def game_frame():
    for i in range(len(sprites)):
        t.penup()
        t.goto(sprites[i].x, sprites[i].y)

        if sprites[i].draw == 1:
            t.pendown()
        else:
            t.penup()

        t.pencolor(sprites[i].colour)

        if sprites[i].dot == 1 and sprites[i].draw == 1:
            t.penup()
            t.dot(sprites[i].size, sprites[i].colour)

    t.penup()
    t.update()
