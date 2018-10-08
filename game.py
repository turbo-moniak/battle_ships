from player import Player1, Player2
from board import Own, Enemy, Board
from game_operations import start_game, sink_ships
from board_operations import print_boards


class Game(object):
    def __init__(self):
        self.player = Player1()
        self.board_player = Own()#stores player1 fleet
        self.empty_board_player = Board()#shows hit player2 ships

        self.enemy = Player2()
        self.board_enemy = Enemy()#stores player2 fleet
        self.empty_board_enemy = Board()#shows hit player1 ships


game = Game()
start_game(game)
print(game.player.fleet)
sink_ships(game)



















