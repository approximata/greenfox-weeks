from tkinter import *
from mainboard import *
from drawable import Hero
from game import *
# from gamescreen import GameScreen

canvas_width = 720
canvas_height = 720
master = Tk()
canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()

game = Game(canvas)
game.drawall()


master.bind('<KeyPress>', game.keyroute)

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
