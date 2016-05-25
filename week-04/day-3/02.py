# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.
from tkinter import *
root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()
line_top = canvas.create_line(50, 50, 250, 50, fill= 'red')
line_left = canvas.create_line(250, 50, 250, 250, fill= 'green')
line_bottom = canvas.create_line(250, 250, 50, 250, fill= 'blue')
line_rigth = canvas.create_line(50, 250, 50, 50, fill= 'purple')
mainloop()
root.mainloop()
