# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
def create_size_color_rectangle(x, y, size, color):
    x_end_point = x + size
    y_end_point = y + size
    canvas.create_rectangle(x, y, x_end_point, y_end_point, fill=color)

create_size_color_rectangle(140, 140, 50, 'green')
create_size_color_rectangle(120, 100, 50, 'red')
create_size_color_rectangle(50, 50, 50, 'blue')

canvas.pack()
mainloop()
