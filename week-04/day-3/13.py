# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.
from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
def create_line(x, y):
    px = 150
    py = 150
    canvas.create_line(x, y, px, py, fill= 'blue')
    # 0 0,  5 0,  10 0 .... 300 0           x += 5 y = 0
    # 300 5,  300 10  ...... 300 300        x = 300 y += 5
    # 295 300,  290 300 ......  0, 300      x -= 5  y = 300
    # 0 295, 0 290, .... 0 0                x = 0 y -= 5

w = 300

def creat_lines_from_center():
    for xy in range(w):
        if xy % 5 == 0:
            create_line(xy, 0)
            create_line(300, xy)
            yx = w - xy
            create_line(yx, 300)
            create_line(0, yx)

creat_lines_from_center()
canvas.pack()
mainloop()
