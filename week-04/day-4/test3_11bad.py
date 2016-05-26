
from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)

def createlinesinsquare(w, xs, ys):

    x1 = [xs + w / 3, ys + (w / 3) * 2, xs + 0, ys + 0]
    y1 = [xs + 0, ys + 0,  xs + w / 3, ys + (w / 3) * 2]
    x2 = [xs + w / 3, ys + (w / 3) * 2, xs + w, ys + w]
    y2 = [xs + w, ys + w,  xs + w / 3, ys + (w / 3) * 2]

    # canvas.create_line(x1[0], y1[0], x2[0], y2[0], fill='red')
    # canvas.create_line(x1[1], y1[1], x2[1], y2[1], fill='green')
    # canvas.create_line(x1[2], y1[2], x2[2], y2[2], fill='blue')
    # canvas.create_line(x1[3], y1[3], x2[3], y2[3], fill='yellow')

    canvas.create_line(x1[0], y1[0], x2[0], y2[0], fill='purple')
    canvas.create_line(x1[1], y1[1], x2[1], y2[1])
    canvas.create_line(x1[2], y1[2], x2[2], y2[2])
    canvas.create_line(x1[3], y1[3], x2[3], y2[3])



createlinesinsquare(300, 0, 0)

canvas.pack()
mainloop()
