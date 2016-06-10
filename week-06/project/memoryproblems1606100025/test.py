class Mainboard():
    def __init__(self):
        self.board = [[0,0,1,0,0,1,0,0,0,0],
                [0,0,1,0,0,1,1,1,0,1],
                [0,1,0,0,0,1,1,1,0,1],
                [0,1,0,0,0,1,0,0,0,1],
                [0,1,1,1,1,1,0,1,0,1],
                [0,0,0,0,0,0,0,1,0,1],
                [1,1,1,1,1,1,1,1,0,1],
                [1,1,0,0,0,1,1,1,0,1],
                [1,1,0,0,0,0,0,0,0,0],
                [1,1,0,0,0,1,1,1,0,1]]
        # self.floor = Floor(0, 0)
        # self.wall = Wall(0, 0)
        self.map = []
        # self.canvas = canvas
        # self.floor = PhotoImage(file = 'floor.gif')
        # self.wall = PhotoImage(file = 'wall.gif')
        # self.drawerpen = drawerpen
        # self.hero = Hero(drawerpen)
        # self.hero = hero
        # self.hero-down = PhotoImage(file = 'hero-down.gif')

    def creatmapvalues(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[j][i] == 0:
                    self.map.append(Floor(i, j))
                elif self.board[j][i] == 1:
                    self.map.append(Wall(i, j))
        return map

main = Mainboard()
print(main.creatmapvalues())
