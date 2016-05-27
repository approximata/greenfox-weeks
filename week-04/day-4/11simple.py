
from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)

def createsquare(w, xs, ys):

    canvas.create_rectangle(xs, ys, xs + w, ys + w, fill='yellow')

def createfractal(w, xs, ys):
    createsquare(w, xs, ys)
    if w < 10:
        pass
    else :
        createfractal(w / 3, xs + w / 3, ys)
        createfractal(w / 3, xs + 2 * w / 3, ys + w / 3)
        createfractal(w / 3, xs, ys + w / 3)
        createfractal(w / 3, xs + w / 3, ys + 2 * w / 3)

createfractal(300, 0, 0)

canvas.pack()
mainloop()
