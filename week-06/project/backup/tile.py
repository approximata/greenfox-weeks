class Tiles():
    def __init__(self, size):
        self.size = size

class Floor(Tiles):
    def __init__(self, size):
        self.size = size

class Wall(Tiles):
    def __init__(self, size):
        self.size = size
        
