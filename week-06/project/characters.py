from tkinter import *
from draw import *
from mainboard import *

class Character():
    def __init__(self, drawerpen):

        # self.health = health
        # self.defend = defend
        # self.strike = strike
        self.drawerpen = drawerpen


class Hero(Character):

    def __init__(self, drawerpen):
        super ().__init__(drawerpen)
        self.floor = PhotoImage(file = 'floor.gif')
        self.hero = PhotoImage(file = 'hero-down.gif')
        self.heroup = PhotoImage(file = 'hero-up.gif')
        self.heroright = PhotoImage(file = 'hero-right.gif')
        self.heroleft = PhotoImage(file = 'hero-left.gif')
        self.position = {'x': 0, 'y': 0, 'type': self.hero}
        # self.x = 0
        # self.y = 0


    def startpoint(self):
        self.drawerpen.drawobjects(self.position)

    def empty(self):
        self.drawerpen.drawobjects({'x': self.position['x'], 'y': self.position['y'], 'type': self.floor })

    def move_down(self):
        self.empty()
        self.position['type'] = self.hero
        self.position['y'] += 1
        self.drawerpen.drawobjects(self.position)

    def move_up(self):
        self.empty()
        self.position['type'] = self.heroup
        self.position['y'] -= 1
        self.drawerpen.drawobjects(self.position)

    def move_right(self):
        self.empty()
        self.position['type'] = self.heroright
        self.position['x'] += 1
        self.drawerpen.drawobjects(self.position)

    def move_left(self):
        self.empty()
        self.position['type'] = self.heroleft
        self.position['x'] -= 1
        self.drawerpen.drawobjects(self.position)

    def currentposition(self):
        return [self.position['x'], self.position['y']]
