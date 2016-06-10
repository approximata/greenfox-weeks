from tkinter import *
from mainboard import *

canvas_width = 720
canvas_height = 720
master = Tk()
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack()
# floor = PhotoImage(file = 'floor.gif')
# wall = PhotoImage(file = 'wall.gif')
#
#
# table1 =[[0,0,1,0,0,1,0,0,0,0],
#         [0,0,1,0,0,1,1,1,0,1],
#         [0,1,0,0,0,1,1,1,0,1],
#         [0,1,0,0,0,1,0,0,0,1],
#         [0,1,1,1,1,1,0,1,0,1],
#         [0,0,0,0,0,0,0,1,0,1],
#         [1,1,1,1,1,1,1,1,0,1],
#         [1,1,0,0,0,1,1,1,0,1],
#         [1,1,0,0,0,0,0,0,0,0],
#         [1,1,0,0,0,1,1,1,0,1]]
#
# def creatmapvalues(table):
#     mapvalues = []
#     for i in range(len(table)):
#         for j in range(len(table)):
#             mapplace = {}
#             mapplace['x'] = j
#             mapplace['y'] = i
#             if table[i][j] == 0:
#                 mapplace['type'] = 'floor'
#             elif table[i][j] == 1:
#                 mapplace['type'] = 'wall'
#             elif table[i][j] == 2:
#                 mapplace['type'] = 'hero'
#             mapvalues.append(mapplace)
#     return mapvalues
#
# def floorincanvas():
#     mapcoords = creatmapvalues(table1)
#     size = 72
#     for i in range(len(mapcoords)):
#         if mapcoords[i]['type'] == 'floor':
#             w.create_image(mapcoords[i]['x'] * size, mapcoords[i]['y'] * size, anchor = NW, image = floor)
#         elif mapcoords[i]['type'] == 'wall':
#             w.create_image(mapcoords[i]['x'] * size, mapcoords[i]['y'] * size, anchor = NW, image = wall)

class Character():
    def __init__(self, health, defend, strike):
        self.health = health
        self.defend = defend
        self.strike = strike

    def startpoint(self):
        w.create_image(self.x, self.y, anchor = NW, image = self.image)

class Hero(Character):

    def __init__(self, health, defend, strike):
        self.x = 0
        self.y =0
        self.image = PhotoImage(file = 'hero-down.gif')

boardlevel1 = Mainboard(w)
boardlevel1.drawcanvas()

# floorincanvas()
greenfox = Hero(0,0,0)
greenfox.startpoint()

master.mainloop()
main()
