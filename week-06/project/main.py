from tkinter import *
from mainboard import *
from characters import Hero
from game import *

canvas_width = 720
canvas_height = 750
master = Tk()
canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()

game = Game(canvas)
game.drawall()

master.bind('<KeyPress>', game.keyroute)

master.mainloop()
