from tkinter import *


class Drawable():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawobjects(self, canvas):
        canvas.create_image(self.x * 72, self.y * 72, anchor = NW, image = self.imageofelem)

class Hero(Drawable):
    def __init__(self, x, y):
        super ().__init__(x, y)
        self.imageofelem = PhotoImage(file = 'pic/hero-down.gif')

    def move_down(self):
        # self.empty()
        # self.position['type'] = self.hero
        self.y += 1
        print(self.y)

    def move_up(self):
    #     self.empty()
    #     self.position['type'] = self.heroup
        self.y -= 1
        print(self.y)
        

    # def move_right(self):
    #     self.empty()
    #     self.position['type'] = self.heroright
    #     self.position['x'] += 1
    #     self.drawobjects(self.position)
    #
    # def move_left(self):
    #     self.empty()
    #     self.position['type'] = self.heroleft
    #     self.position['x'] -= 1
    #     self.drawobjects(self.position)
    #
    # def currentposition(self):
    #     return [self.position['x'], self.position['y']]


class Floor(Drawable):
    def __init__(self, x, y):
        super ().__init__(x, y)
        self.imageofelem = PhotoImage(file = 'pic/floor.gif')

class Wall(Drawable):
    def __init__(self, x, y):
        super ().__init__(x, y)
        self.imageofelem = PhotoImage(file = 'pic/wall.gif')
