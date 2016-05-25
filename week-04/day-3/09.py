# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)

def create_size_color_center_rectangle(size, color):
    x = 150 - (size / 2)
    y = 150 - (size / 2)
    x_end_point = x + size
    y_end_point = y + size
    canvas.create_rectangle(x, y, x_end_point, y_end_point, fill=color)

create_size_color_center_rectangle(130, 'green')
create_size_color_center_rectangle(40, 'red')
create_size_color_center_rectangle(20, 'blue')

canvas.pack()
mainloop()
