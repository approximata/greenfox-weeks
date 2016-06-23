from mainboard import *
from drawable import *
from characters import *
from random import randint
from stats import *

class Game(object):
    def __init__(self, canvas):
       self.canvas = canvas
       self.map = Mainboard()
       self.hero = Hero(0, 0)
       self.startcoordvar = self.startpoints()
       self.skeleton0 = Skeleton(self.startcoordvar[0][0], self.startcoordvar[0][1])
       self.skeleton1 = Skeleton(self.startcoordvar[1][0], self.startcoordvar[1][1])
       self.skeleton2 = Skeleton(self.startcoordvar[2][0], self.startcoordvar[2][1])
       self.boss = Boss(self.startcoordvar[3][0], self.startcoordvar[3][1])
       self.stats = Stats(2, 10.1)

    def get_enemystartpoint(self):
        x = randint(0, 9)
        y = randint(0, 9)
        if self.map.is_step_valid(x, y):
            coordinate = []
            coordinate.append(x)
            coordinate.append(y)
            print(coordinate)
            return coordinate
        else:
            return self.get_enemystartpoint()

    def startpoints(self):
        startpoint = []
        while len(startpoint) < 4:
            startpoint.append(self.get_enemystartpoint())
        print(startpoint)
        return startpoint

    def drawall(self):
        self.map.drawmap(self.canvas)
        self.hero.drawchar(self.canvas)
        self.skeleton0.drawchar(self.canvas)
        self.skeleton1.drawchar(self.canvas)
        self.skeleton2.drawchar(self.canvas)
        self.boss.drawchar(self.canvas)
        self.stats.statsprint(self.canvas)

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
