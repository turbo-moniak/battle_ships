from player import Player1, Player2
from board import Own, Enemy, Board


class Game(object):
    def __init__(self):
        self.player = Player1()
        self.board_player = Own()
        self.empty_board_player = Board()

        self.enemy = Player2()
        self.board_enemy = Enemy()
        self.empty_board_enemy = Board()

















