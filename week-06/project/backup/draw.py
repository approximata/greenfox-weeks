from tkinter import *

class Drawer():
    def __init__(self, canvas):
        self.canvas = canvas
    def drawobjects(self, drawable):
        self.canvas.create_image(drawable['x'] * 72, drawable['y'] * 72, anchor = NW, image = drawable['type'])

    # def drawlist(self, drawable, type):
    #     self.canvas.delete('all')
    #     self.canvas.create_image(drawable[0] * 72, drawable[1] * 72, anchor = NW, image = drawable.type)
