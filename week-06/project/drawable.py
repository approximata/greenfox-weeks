from tkinter import *

class Drawable(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawobjects(self, canvas):
        canvas.create_image(self.x * 72, self.y * 72, anchor = NW, image = self.imageofelem)

class Hero(Drawable):
    def __init__(self, x, y):
        super ().__init__(x, y)
        self.imageofelem = PhotoImage(file = 'pic/hero-down.gif')

    def drawchar(self, canvas):
        self.drawobjects(canvas)

    def move_down(self):
        self.imageofelem = PhotoImage(file = 'pic/hero-down.gif')
        self.y += 1
        print(self.y)

    def move_up(self):
        self.imageofelem = PhotoImage(file = 'pic/hero-up.gif')
        self.y -= 1
        print(self.y)

    def move_right(self):
        self.imageofelem = PhotoImage(file = 'pic/hero-right.gif')
        self.x += 1
        print(self.x)

    def move_left(self):
        self.imageofelem = PhotoImage(file = 'pic/hero-left.gif')
        self.x -= 1
        print(self.x)

    def get_currentposition(self):
        return [self.x, self.y]

class Floor(Drawable):
    def __init__(self, x, y):
        super ().__init__(x, y)
        self.imageofelem = PhotoImage(file = 'pic/floor.gif')

class Wall(Drawable):
    def __init__(self, x, y):
        super ().__init__(x, y)
        self.imageofelem = PhotoImage(file = 'pic/wall.gif')