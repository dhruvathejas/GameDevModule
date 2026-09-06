import turtle as t

version = 1.10

sprites = []

names = []
attributes = []

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

    @staticmethod
    def create_sprite(name, x, y, size, colour, draw, dot):
        names.append(name)
        attributes.append([x, y, size, colour, draw, dot])

    @staticmethod
    def delete_sprite(name):
        for i in range(len(names)):
            if names[i] == name:
                names.pop(i)
                attributes.pop(i)
                return

    @staticmethod
    def move_x(name, amount):
        for i in range(len(names)):
            if names[i] == name:
                attributes[i][0] += amount

    @staticmethod
    def move_y(name, amount):
        for i in range(len(names)):
            if names[i] == name:
                attributes[i][1] += amount

    @staticmethod
    def move(name, x, y):
        for i in range(len(names)):
            if names[i] == name:
                attributes[i][0] += x
                attributes[i][1] += y

    @staticmethod
    def set_x(name, x):
        for i in range(len(names)):
            if names[i] == name:
                attributes[i][0] = x

    @staticmethod
    def set_y(name, y):
        for i in range(len(names)):
            if names[i] == name:
                attributes[i][1] = y

    @staticmethod
    def set_size(name, size):
        for i in range(len(names)):
            if names[i] == name:
                attributes[i][2] = size

    @staticmethod
    def set_colour(name, colour):
        for i in range(len(names)):
            if names[i] == name:
                attributes[i][3] = colour

    @staticmethod
    def set_draw(name, draw):
        for i in range(len(names)):
            if names[i] == name:
                attributes[i][4] = draw

    @staticmethod
    def set_dot(name, dot):
        for i in range(len(names)):
            if names[i] == name:
                attributes[i][5] = dot

    @staticmethod
    def get_x(name):
        for i in range(len(names)):
            if names[i] == name:
                return attributes[i][0]

    @staticmethod
    def get_y(name):
        for i in range(len(names)):
            if names[i] == name:
                return attributes[i][1]

    @staticmethod
    def get_size(name):
        for i in range(len(names)):
            if names[i] == name:
                return attributes[i][2]

    @staticmethod
    def get_colour(name):
        for i in range(len(names)):
            if names[i] == name:
                return attributes[i][3]

    @staticmethod
    def get_draw(name):
        for i in range(len(names)):
            if names[i] == name:
                return attributes[i][4]

    @staticmethod
    def get_dot(name):
        for i in range(len(names)):
            if names[i] == name:
                return attributes[i][5]


class GameLoop:

    @staticmethod
    def game_loop():
        while True:
            t.clear()

            for i in range(len(names)):
                a = attributes[i]

                t.penup()
                t.color(a[3])
                t.goto(a[0], a[1])

                if a[4] == 1:
                    t.pendown()

                if a[5] == 1 and a[4] == 1:
                    t.dot(a[2], a[3])

            t.update()