from player import Player1, Player2
from board import Own, Enemy, Board
from game_operations import start_game, sink_ships
from ship import coordinates_mapping


class Game(object):
    def __init__(self):
        self.player = Player1()
        self.board_player = Own()
        self.empty_board_player = Board()

        self.enemy = Player2()
        self.board_enemy = Enemy()
        self.empty_board_enemy = Board()


game = Game()
start_game(game)
# print(game.player.fleet)
# sink_ships(game, coordinates_mapping)

















