from tkinter import *

class Drawer():
    def __init__(self, canvas):
        self.canvas = canvas
    def drawobjects(self, drawable):
        self.canvas.create_image(drawable['x'] * 72, drawable['y'] * 72, anchor = NW, image = drawable['type'])
