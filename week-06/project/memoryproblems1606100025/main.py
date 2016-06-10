from tkinter import *
from mainboard import *
from drawable import Hero
# from gamescreen import GameScreen

canvas_width = 720
canvas_height = 720
master = Tk()
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack()

greenhero = Hero(0, 0)
boardlevel1 = Mainboard(w, greenhero)


def keypressed(event):
#     boardlevel1.move_down(w)
# master.bind("<Down>", move_down_press_key)
    boardlevel1.keyroute(event)
    boardlevel1.createmap(w)
    boardlevel1.createhero(w)
master.bind("<KeyPress>", keypressed)

# def move_up_press_key(event):
#     greenHero.move_up()
# master.bind("<Up>", move_up_press_key)
#
# def move_right_press_key(event):
#     greenHero.move_right()
# master.bind("<Right>", move_right_press_key)
#
# def move_left_press_key(event):
#     greenHero.move_left()
# master.bind("<Left>", move_left_press_key)

master.mainloop()

# print(greenHero.currentposition())
# print(greenHero.border_in())
