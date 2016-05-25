# create a 300x300 canvas.
# fill it with a checkerboard pattern.
from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
def create_square(x, y, size, color):
    x_end_point = x + size
    y_end_point = y + size
    square = canvas.create_rectangle(x, y, x_end_point, y_end_point, fill = color)

size = 5
w = 300
h = 300
maxI = w / size
maxJ = h / size

def create_checkboard(size):
    w = 300
    h = 300
    maxI = w // size
    maxJ = h // size

    for i in range(-1, maxI-1):
        i += 1
        for j in range(-1, maxJ-1):
            j += 1
            if i % 2 == 0 and j % 2 == 0 or i % 2 != 0 and j % 2 != 0:
                color = 'black'
                create_square(i * size, j * size, size, color)
            else:
                color = 'white'
                create_square(i * size, j * size, size, color)

create_checkboard(25)

canvas.pack()
mainloop()
