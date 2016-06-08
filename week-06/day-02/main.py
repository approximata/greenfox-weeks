from tkinter import *
from mainboard import *
from characters import *

canvas_width = 720
canvas_height = 720
master = Tk()
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack()


drawerpen = Drawer(w)

boardlevel1 = Mainboard(drawerpen)
boardlevel1.createmap()

greenHero = Hero(drawerpen)
greenHero.startpoint()

def move_down_press_key(event):
        greenHero.move_down()

master.bind("<Down>", move_down_press_key)

master.mainloop()
