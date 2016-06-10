from tkinter import *
from drawable import Floor, Wall


class Mainboard():
    def __init__(self, canvas, hero):
        self.board = [[0,0,1,0,0,1,0,0,0,0],
                [0,0,1,0,0,1,1,1,0,1],
                [0,1,0,0,0,1,1,1,0,1],
                [0,1,0,0,0,1,0,0,0,1],
                [0,1,1,1,1,1,0,1,0,1],
                [0,0,0,0,0,0,0,1,0,1],
                [1,1,1,1,1,1,1,1,0,1],
                [1,1,0,0,0,1,1,1,0,1],
                [1,1,0,0,0,0,0,0,0,0],
                [1,1,0,0,0,1,1,1,0,1]]
        # self.floor = Floor(0, 0)
        # self.wall = Wall(0, 0)
        self.map = []
        # self.canvas = canvas
        # self.floor = PhotoImage(file = 'floor.gif')
        # self.wall = PhotoImage(file = 'wall.gif')
        # self.drawerpen = drawerpen
        self.hero = hero
        # self.hero = hero
        # self.hero-down = PhotoImage(file = 'hero-down.gif')
        self.createmap(canvas)
        self.createhero(canvas)

    def creatmapvalues(self):
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if self.board[y][x] == 0:
                    self.map.append(Floor(x, y))
                elif self.board[y][x] == 1:
                    self.map.append(Wall(x, y))

    def createmap(self, canvas):
        self.creatmapvalues()
        for i in self.map:
            i.drawobjects(canvas)

    def createhero(self, canvas):
        self.hero.drawobjects(canvas)

    # def move_down(self, canvas):
    #     # self.empty()
    #     # self.position['type'] = self.hero
    #     self.hero.y += 1
    #     self.createmap(canvas)
    #     self.hero.drawobjects(canvas)


    def keyroute(self, key):
        key = key.keysym
        if key == 'Down':
            self.hero.move_down()
        elif key == 'Up':
            self.hero.move_up()
        # if border_in({currentposition()[0]+1}):

    # def border_in(self, charachterpostion):
        # return self.charachterpostion[0] < 9 and self.charachterpostion[0] > 0 and self.charachterpostion[1] < 9 and self.charachterpostion[1] > 0

    # def wall_out(self):
        # charachterpostion = self.currentposition()
        # mapelemets = self.creatmapvalues()
        # return mapelemets['type'] == self.floor and mapelemets['x'] == charachterpostion[0] and mapelemets['y'] == charachterpostion[1]
