from tkinter import *
from draw import *

class Character():
    def __init__(self, drawerpen):

        # self.health = health
        # self.defend = defend
        # self.strike = strike
        self.drawerpen = drawerpen

class Hero(Character):

    def __init__(self, drawerpen):
        super ().__init__(drawerpen)
        self.hero = PhotoImage(file = 'hero-down.gif')
        self.xposition = 0
        self.yposition = 0
        self.position = {'x': self.xposition, 'y': self.yposition, 'type': self.hero }

    def startpoint(self):
        self.drawerpen.drawobjects(self.position)

    def move_down(self):
        self.yposition += 1
        self.drawerpen.drawobjects({'x': self.xposition, 'y': self.yposition , 'type': self.hero })
