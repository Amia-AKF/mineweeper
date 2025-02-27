class Cell:
    def __init__(self):
        self.is_mine = False
        self.adjacent_mines = 0
        self.is_open = False
        self.is_flagged = False
        self.cell = None
        self.text = None

    