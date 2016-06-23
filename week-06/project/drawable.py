from tkinter import *

class Drawable(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawobjects(self, canvas):
        canvas.create_image(self.x * 72, self.y * 72, anchor = NW, image = self.imageofelem)

class Floor(Drawable):
    def __init__(self, x, y):
        super ().__init__(x, y)
        self.imageofelem = PhotoImage(file = 'pic/floor.gif')

class Wall(Drawable):
    def __init__(self, x, y):
        super ().__init__(x, y)
        self.imageofelem = PhotoImage(file = 'pic/wall.gif')
