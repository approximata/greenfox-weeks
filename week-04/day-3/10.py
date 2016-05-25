# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
def create_size_center_rectangle(size):

    x = 150 - (size / 2)
    y = 150 - (size / 2)
    x_end_point = x + size
    y_end_point = y + size

    square = canvas.create_rectangle(x, y, x_end_point, y_end_point, fill='green')

size = 10

# def random_color():
#     rgbl=[255,0,0]
#     random.shuffle(rgbl)
#     return tuple(rgbl)

def create_many_rectangle(numberofrectange):
    for i in range(numberofrectange - 1, 0, -1):
        create_size_center_rectangle(size + 10 * i)

create_many_rectangle(20)


canvas.pack()
mainloop()
