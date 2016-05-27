from tkinter import *
from math import *

canvas_width = 610
canvas_height = 610
python_green = "#476042"

master = Tk()

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

def create_hexa(xs, ys, size):
    points = [xs, ys, xs + size, ys, xs, ys + size]
    w.create_polygon(points, outline = python_green,
                fill = 'yellow', width = 2)

def create_fractalrectangle(xs, ys, size):
    create_triangle(xs, ys, size)
    half = size / 2
    if size < 10:
        pass
    else:
        create_fractalrectangle(xs, ys, half)
        create_fractalrectangle(xs + half, ys, half)
        create_fractalrectangle(xs + half / 2, ys + (sqrt(3)/2 * half), half)

create_hexa(10, 10, 300)

mainloop()
