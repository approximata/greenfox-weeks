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
        if key == 'Down' and self.map.is_step_valid(self.hero.x, self.hero.y + 1):
            self.hero.move_down()
            self.hero.drawchar(self.canvas)
        elif key == 'Up' and self.map.is_step_valid(self.hero.x, self.hero.y - 1):
            self.hero.move_up()
            self.hero.drawchar(self.canvas)
        elif key == 'Right' and self.map.is_step_valid(self.hero.x + 1, self.hero.y):
            self.hero.move_right()
            self.hero.drawchar(self.canvas)
        elif key == 'Left'and self.map.is_step_valid(self.hero.x - 1, self.hero.y):
            self.hero.move_left()
            self.hero.drawchar(self.canvas)
        print(self.map.is_step_valid(self.hero.x, self.hero.y))
