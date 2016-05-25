# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.
from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width=300, height=300)
def create_size_center_rectangle(size, color):

    x = 150 - (size / 2)
    y = 150 - (size / 2)
    x_end_point = x + size
    y_end_point = y + size
    square = canvas.create_rectangle(x, y, x_end_point, y_end_point, fill = color)

size = 10
color = "#%06x" % random.randint(0, 0xFFFFFF)

def create_many_rectangle(numberofrectange):
    for i in range(numberofrectange - 1, 0, -1):
        color = "#%06x" % random.randint(0, 0xFFFFFF)
        create_size_center_rectangle(size + 10 * i, color)

create_many_rectangle(20)

canvas.pack()
mainloop()
