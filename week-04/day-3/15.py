# create a 300x300 canvas.
# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
def create_line(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, fill= 'blue')

def create_lines_between_points(list):
    for i in range(len(list)-1):
            create_line(list[i][0], list[i][1], list[i+1][0], list[i+1][1])
            create_line(list[len(list)-1][0], list[len(list)-1][1], list[0][0], list[0][1])

reclist = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]
create_lines_between_points(reclist)

canvas.pack()
mainloop()
