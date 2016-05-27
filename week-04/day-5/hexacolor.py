from tkinter import *
from math import *
import random

canvas_width = 610
canvas_height = 610
python_green = 'black'

master = Tk()

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()
colors = [ '#62727B', '#353A3B', '#7E827A', '#E2E1DE', '#C77966', ]
i = 0

def create_hexa(xs, ys, size, color):
    s2 = sqrt(2)
    sizexplus = 1 / 2 * size
    sizeyplus = sqrt(3) / 2 * size
    points = [xs, ys, xs + size, ys, xs + size + sizexplus, ys + sizeyplus, xs + size, ys + 2 * sizeyplus, xs, ys + 2 * sizeyplus, xs - sizexplus, ys + sizeyplus]
    w.create_polygon(points, outline = python_green,
                fill = color, width = 1)


def create_fractalhexa(xs, ys, size):
    global i
    i += 1
    if i >= 5:
        i = 0
    color = colors[i]
    create_hexa(xs, ys, size, color)
    third = size / 3
    sizey2littleone = sqrt(3) / 3 * size
    if size < 10:
        pass
    else:
        create_fractalhexa(xs, ys, third)
        create_fractalhexa(xs + 2 * third, ys, third)
        create_fractalhexa(xs + 3 * third, ys + sizey2littleone, third)
        create_fractalhexa(xs + third, ys + sizey2littleone, third)
        create_fractalhexa(xs - third, ys + sizey2littleone, third)
        create_fractalhexa(xs , ys + 2 * sizey2littleone, third)
        create_fractalhexa(xs + 2 * third, ys + 2 * sizey2littleone, third)

create_fractalhexa(155, 10, 300)

mainloop()
