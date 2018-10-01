from board_operations import create_board

coordinates_mapping = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}
board_size = 11


class Board(object):

    def __init__(self):

        self.size = board_size
        self.board = create_board(board_size)


class Own(Board):
    def __init__(self):
        Board.__init__(self)


class Enemy(Board):
    def __init__(self):
        Board.__init__(self)






