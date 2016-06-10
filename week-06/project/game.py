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
        elif key == 'Right':
            self.hero.move_right()
            self.hero.drawchar(self.canvas)
        elif key == 'Left':
            self.hero.move_left()
            self.hero.drawchar(self.canvas)
        self.is_in_the_map()
        self.is_in_the_floor()

    def is_in_the_map(self):
        x = self.hero.get_currentposition()[0]
        y = self.hero.get_currentposition()[1]
        print(x, y)
        if x <= 9 and x >= 0 and y <= 9 and y >= 0:
            print('in')
        else:
            print('out')

    def is_in_the_floor(self):
        print(self.map.board[self.hero.get_currentposition()[1]][self.hero.get_currentposition()[0]])
