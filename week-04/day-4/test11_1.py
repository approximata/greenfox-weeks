
from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)

def createfractal(w, h):
    x1 = [w / 3, (w / 3) * 2, 0, 0]
    y1 = [0, 0,  w / 3, (w / 3) * 2]
    x2 = [w / 3, (w / 3) * 2, w, w]
    y2 = [w, w,  w / 3, (w / 3) * 2]

    if len(x1) == 0:
        canvas.create_line(x1[len(0)], y1[len(0)], x2[len(0)], y2[len(0)])
    else:
        canvas.create_line(x1[len(x1)], y1[len(x1)], x2[len(x1)], y2[len(x1)])
        createfractal(canvas.create_line(x1[len(x1)-1], y1[len(x1)-1], x2[len(x1)-1], y2[len(x1)-1]))

createfractal(300, 300)

canvas.pack()
mainloop()
