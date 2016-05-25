from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
def create_line(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, fill= 'blue')

w = 300
half = w // 2

def create_lines_vasarely():
    for i in range(0, half, 5):
        create_line(half, i, half + i, half)
        create_line(half, i, half - i, half)
        create_line(i, half, half, half + i)
        create_line(half, 2 * half - i, half + i, half)

create_lines_vasarely()
canvas.pack()
mainloop()
