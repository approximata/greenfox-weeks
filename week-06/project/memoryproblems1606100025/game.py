from mainboard import *
from drawable import *

class GameScreen(object):
    def __init__(self, canvas, hero):
       self.canvas = canvas
       self.hero = hero
       self.itemsonscreen = Mainboard(canvas, hero)
       self.createmap(canvas)
       self.createhero(canvas)

    def createmap(self, canvas):
       self.creatmapvalues()
       for i in self.map:
           i.drawobjects(canvas)

    def createhero(self, canvas):
        self.hero.drawobjects(canvas)
