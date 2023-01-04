class Piece:
    def __init__(self, position, orientation):
        self.position = position
        self.orientation = orientation

    def move(self, position, orientation):
        self.position = position
        self.orientation = orientation

class Cube:
    def __init__(self):
        pass
