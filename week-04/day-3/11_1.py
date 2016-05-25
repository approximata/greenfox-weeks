from tkinter import *

root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()

def draw_square(offset, size):
   square = canvas.create_rectangle(offset, offset, offset + size, offset + size, fill='#b145f3')
size = 10
offset = 10
for i in range(19):
   draw_square(offset + i * 10, size)

root.mainloop()
