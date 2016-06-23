from drawable import *

class Charachter(object):
    def __init__(self, healthp, defendp, strikep):
        self.healthp = healthp
        self.defendp = defendp
        self.strikep = strikep

class Hero(Drawable, Charachter):
    def __init__(self, x, y):
        super ().__init__(x, y)
        self.imageofelem = PhotoImage(file = 'pic/hero-down.gif')

    def drawchar(self, canvas):
        self.drawobjects(canvas)

    def move_down(self):
        self.imageofelem = PhotoImage(file = 'pic/hero-down.gif')
        self.y += 1
        print(self.y)

    def move_up(self):
        self.imageofelem = PhotoImage(file = 'pic/hero-up.gif')
        self.y -= 1
        print(self.y)

    def move_right(self):
        self.imageofelem = PhotoImage(file = 'pic/hero-right.gif')
        self.x += 1
        print(self.x)

    def move_left(self):
        self.imageofelem = PhotoImage(file = 'pic/hero-left.gif')
        self.x -= 1
        print(self.x)

    def get_currentposition(self):
        return [self.x, self.y]

class Skeleton(Drawable, Charachter):
    def __init__(self, x, y):
        super ().__init__(x, y)
        self.imageofelem = PhotoImage(file = 'pic/skeleton.gif')

    def drawchar(self, canvas):
        self.drawobjects(canvas)

class Boss(Drawable, Charachter):
    def __init__(self, x, y):
        super ().__init__(x, y)
        self.imageofelem = PhotoImage(file = 'pic/boss.gif')

    def drawchar(self, canvas):
        self.drawobjects(canvas)
