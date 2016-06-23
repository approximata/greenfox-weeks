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

    def is_in_the_map(self, x, y):
        return x <= 9 and x >= 0 and y <= 9 and y >= 0

    def is_in_the_floor(self, x, y):
        return self.board[y][x] == 0

    def is_step_valid(self, x, y):
        return self.is_in_the_map(x, y) and self.is_in_the_floor(x, y)
