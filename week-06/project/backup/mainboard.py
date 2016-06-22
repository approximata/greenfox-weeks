from tkinter import *
from draw import *
from characters import *



class Mainboard():
    def __init__(self, drawerpen):
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
        # self.canvas = canvas
        self.floor = PhotoImage(file = 'floor.gif')
        self.wall = PhotoImage(file = 'wall.gif')
        self.drawerpen = drawerpen
        self.hero = Hero(drawerpen)
        # self.hero = hero
        # self.hero-down = PhotoImage(file = 'hero-down.gif')

    def creatmapvalues(self):
        mapvalues = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                mapplace = {}
                mapplace['x'] = j
                mapplace['y'] = i
                if self.board[i][j] == 0:
                    mapplace['type'] = self.floor
                elif self.board[i][j] == 1:
                    mapplace['type'] = self.wall
                mapvalues.append(mapplace)
        return mapvalues

    def createmap(self):
        mapcoords = self.creatmapvalues()
        for i in range(len(mapcoords)):
            self.drawerpen.drawobjects(mapcoords[i])

    # def keypressed(self, event):
        # if border_in({currentposition()[0]+1}):

    # def border_in(self, charachterpostion):
        # return self.charachterpostion[0] < 9 and self.charachterpostion[0] > 0 and self.charachterpostion[1] < 9 and self.charachterpostion[1] > 0

    # def wall_out(self):
        # charachterpostion = self.currentposition()
        # mapelemets = self.creatmapvalues()
        # return mapelemets['type'] == self.floor and mapelemets['x'] == charachterpostion[0] and mapelemets['y'] == charachterpostion[1]
