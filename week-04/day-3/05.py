# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
def create_line(x, y):

    x_end_point = x + 50
    y_end_point = y

    return canvas.create_line(x, y, x_end_point, y_end_point, fill= 'green')

create_line(32, 21)
create_line(55, 67)
create_line(43, 45)
canvas.pack()
mainloop()
