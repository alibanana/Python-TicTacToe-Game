class GameStatus():
    def __init__(self):
        self.menu = 0
        self.pointer = 0
        self.turn = 0
        self.win = 0

    def reset(self):
        self.pointer = 0
        self.turn = 0
        self.win = 0