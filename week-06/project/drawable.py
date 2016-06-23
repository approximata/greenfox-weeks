from tkinter import *

class Drawable(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 72

    def drawobjects(self, canvas):
        canvas.create_image(self.x * self.size, self.y * self.size, anchor = NW, image = self.imageofelem)

    def drawtext(self, canvas):
        canvas.create_text(self.x * self.size, self.y * self.size, text = 'print something long again again' )

class Floor(Drawable):
    def __init__(self, x, y):
        super ().__init__(x, y)
        self.imageofelem = PhotoImage(file = 'pic/floor.gif')

class Wall(Drawable):
    def __init__(self, x, y):
        super ().__init__(x, y)
        self.imageofelem = PhotoImage(file = 'pic/wall.gif')
