from tkinter import *

root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()

def draw_square(offset, size):
   square = canvas.create_rectangle(offset, offset, offset + size, offset + size, fill='#b145f3')
size = 10
offset = 10

count = 0
while count < 6:
   draw_square(offset, size)
   size = size + 10
   offset = offset + size - 10
   count += 1

root.mainloop()
