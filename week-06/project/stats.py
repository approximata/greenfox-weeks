from drawable import *

class Stats(Drawable):
    def __init__(self, x, y):
        super ().__init__(x, y)

    def statsprint(self, canvas):
        self.drawtext(canvas)
