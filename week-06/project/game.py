from mainboard import *
from drawable import *

class Game(object):
    def __init__(self, canvas):
       self.canvas = canvas
       self.map = Mainboard()
       self.hero = Hero(0, 0)

    def drawall(self):
        self.map.drawmap(self.canvas)
        self.hero.drawchar(self.canvas)

    def keyroute(self, key):
        key = key.keysym
        if key == 'Down':
            self.hero.move_down()
            self.hero.drawchar(self.canvas)
        elif key == 'Up':
            self.hero.move_up()
            self.hero.drawchar(self.canvas)
