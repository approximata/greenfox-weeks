
from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width=300, height=300)

def createlinesinsquare(w, xs, ys):

    x1 = [xs + w / 3, xs + w / 3 * 2, xs + 0, xs + 0]
    y1 = [ys + 0, ys + 0,  ys + w / 3, ys + (w / 3) * 2]
    x2 = [xs + w / 3, xs + (w / 3) * 2, xs + w, xs + w]
    y2 = [ys + w, ys + w,  ys + w / 3, ys + (w / 3) * 2]

    color1 = "#%06x" % random.randint(0, 0xFFFFFF)
    canvas.create_line(x1[0], y1[0], x2[0], y2[0], fill = color1)
    canvas.create_line(x1[1], y1[1], x2[1], y2[1], fill = color1)
    canvas.create_line(x1[2], y1[2], x2[2], y2[2], fill = color1)
    canvas.create_line(x1[3], y1[3], x2[3], y2[3], fill = color1)

    color2 = "#%06x" % random.randint(0, 0xFFFFFF)
    canvas.create_rectangle(xs, ys, xs + w, ys + w, fill = color2)

def createfractal(w, xs, ys):
    createlinesinsquare(w, xs, ys)
    if w < 10:
        pass
    else :
        createfractal(w / 3, xs + w / 3, ys)
        createfractal(w / 3, xs + 2 * w / 3, ys + w / 3)
        createfractal(w / 3, xs, ys + w / 3)
        createfractal(w / 3, xs + w / 3, ys + 2 * w / 3)

createfractal(300, 0, 0)

canvas.pack()
mainloop()
