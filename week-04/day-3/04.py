# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
def create_line(x, y):

    centerx = 150
    centery = 150

    return canvas.create_line(x, y, centerx, centery, fill= 'red')

create_line(32, 21)
create_line(55, 67)
create_line(43, 45)
canvas.pack()
mainloop()
