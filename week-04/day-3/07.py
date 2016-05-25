# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
def create_size_color_rectangle(x, y, size, color):
    x_end_point = x + size
    y_end_point = y + size
    canvas.create_rectangle(x, y, x_end_point, y_end_point, fill=color)

create_size_color_rectangle(140, 140, 20, 'green')
create_size_color_rectangle(120, 100, 40, 'red')
create_size_color_rectangle(50, 100, 60, 'blue')
create_size_color_rectangle(20, 100, 80, 'purple')

canvas.pack()
mainloop()
