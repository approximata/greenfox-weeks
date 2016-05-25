# create a 300x300 canvas.
# draw a green 10x10 square to its center.
from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
def create_color_rectangle(x, y, color):
    x_end_point = x + 10
    y_end_point = y + 10
    canvas.create_rectangle(x, y, x_end_point, y_end_point, fill=color)

create_color_rectangle(145, 145, 'green')
canvas.pack()
mainloop()
