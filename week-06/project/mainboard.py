from tkinter import *
from drawable import Floor, Wall

class Mainboard(object):
    def __init__(self):
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
        self.map = []

    def creatmapvalues(self):
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if self.board[y][x] == 0:
                    self.map.append(Floor(x, y))
                elif self.board[y][x] == 1:
                    self.map.append(Wall(x, y))

    def drawmap(self, canvas):
        self.creatmapvalues()
        for i in self.map:
            i.drawobjects(canvas)

    # def border_in(self):
    #     return

    # def wall_out(self):
        # charachterpostion = self.currentposition()
        # mapelemets = self.creatmapvalues()
        # return mapelemets['type'] == self.floor and mapelemets['x'] == charachterpostion[0] and mapelemets['y'] == charachterpostion[1]
